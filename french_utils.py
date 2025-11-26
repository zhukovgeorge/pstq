# french_utils.py

def get_tef_tefaq_band(score):
    """
    Calculates the NCLC/EQNCF Level based on the modern TEF/TEFAQ 0-699 scale.
    Based on the official chart:
    0-99: <A1
    100-199: A1 (Level 1-2)
    200-299: A2 (Level 3-4) -> Note: Level 4 starts at 260
    300-399: B1 (Level 5-6)
    400-499: B2 (Level 7-8)
    500-599: C1 (Level 9-10)
    600-699: C2 (Level 11-12)
    """
    if score < 100: return 0
    if score < 200: return 1  # A1

    # A2 Range (200-299)
    if 200 <= score < 260: return 3 # A2 Low
    if 260 <= score < 300: return 4 # A2 High (Per image footnote)

    # B1 Range (300-399)
    if 300 <= score < 350: return 5 # B1 Low
    if 350 <= score < 400: return 6 # B1 High

    # B2 Range (400-499)
    if 400 <= score < 450: return 7 # B2 Low (This is where your 415 falls)
    if 450 <= score < 500: return 8 # B2 High

    # C1 Range (500-599)
    if 500 <= score < 550: return 9
    if 550 <= score < 600: return 10

    # C2 Range (600-699)
    if 600 <= score < 650: return 11
    if score >= 650: return 12

    return 0

# TCF remains separate as it uses a different scoring system
TCF_MAP = {
    'Compréhension orale': [
        (0, 330, 0), (331, 368, 4), (369, 397, 5), (398, 457, 6),
        (458, 502, 7), (503, 522, 8), (523, 548, 9), (549, 579, 10), (580, 599, 11), (600, 699, 12)
    ],
    'Expression orale': [
        (0, 5, 0), (6, 6, 4), (7, 9, 5), (10, 11, 6),
        (12, 13, 7), (14, 15, 8), (16, 17, 9), (18, 19, 10), (20, 20, 12)
    ],
    'Compréhension écrite': [
        (0, 341, 0), (342, 374, 4), (375, 405, 5), (406, 452, 6),
        (453, 499, 7), (500, 523, 8), (524, 548, 9), (549, 579, 10), (580, 599, 11), (600, 699, 12)
    ],
    'Expression écrite': [
        (0, 5, 0), (6, 6, 4), (7, 9, 5), (10, 11, 6),
        (12, 13, 7), (14, 15, 8), (16, 17, 9), (18, 19, 10), (20, 20, 12)
    ]
}

def get_band(test_type, skill, score):
    """
    Returns the NCLC level based on the test type and raw score.
    """
    # TEF Canada and TEFAQ now utilize the same 0-699 scale
    if test_type in ['TEF Canada', 'TEFAQ']:
        return get_tef_tefaq_band(score)

    # TCF Logic
    if test_type == 'TCF Canada':
        mapping = TCF_MAP
        if skill not in mapping: return 0
        for (low, high, band) in mapping[skill]:
            if low <= score <= high: return band
        if score > mapping[skill][-1][1]: return mapping[skill][-1][2]

    return 0

def get_next_threshold_tef(score):
    """
    Returns (next_level_score, points_needed, progress_percent, current_band_floor).
    Used for the progress bar visualization.
    """
    # The start points of every level in the 0-699 scale
    # Level:  1    3    4    5    6    7    8    9    10   11   12
    steps = [100, 200, 260, 300, 350, 400, 450, 500, 550, 600, 650]

    # 1. Handle Max Score (Level 12)
    if score >= 650:
        return (None, 0, 100, 650)

    # 2. Find where we sit
    next_step = 100 # Default
    current_floor = 0

    for step in steps:
        if score < step:
            next_step = step
            break
        current_floor = step

    points_needed = next_step - score

    # Calculate percentage progress within the current band
    # e.g., Floor 400, Next 450, Score 415.
    # Range is 50. Progress is 15. Pct = 30%.
    band_range = next_step - current_floor
    if band_range == 0: band_range = 1 # Safety

    progress = score - current_floor
    pct = (progress / band_range) * 100

    return (next_step, points_needed, pct, current_floor)


def get_next_threshold_tcf(skill, score):
    """
    Returns (next_level_score, points_needed, progress_percent, current_band_floor, max_scale).
    Handles the HYBRID scale of TCF Canada:
    - Listening/Reading: 0-699
    - Speaking/Writing: 0-20
    """
    # 1. DEFINE SCALES
    if skill in ['Expression orale', 'Expression écrite']:
        # 0-20 Scale
        # Levels: <4(0-5), 4(6), 5(7-9), 6(10-11), 7(12-13), 8(14-15), 9(16-17), 10(18-19), 11+(20)
        # Note: These buckets are tight!
        steps = [6, 7, 10, 12, 14, 16, 18, 20]
        max_scale = 20
    else:
        # 0-699 Scale (Listening/Reading)
        # TCF thresholds are different from TEF!
        # Lvl 7 starts at: List(458), Read(453). Let's average/approx or use specific if needed.
        # Simplified Steps for TCF Receptive (Generic approximation for visualization):
        # 4(331), 5(369), 6(398), 7(458), 8(503), 9(523), 10(549), 11(580), 12(600)
        steps = [331, 369, 398, 458, 503, 523, 549, 580, 600]
        max_scale = 699

    # 2. FIND POSITION
    if score >= steps[-1]:
        return (None, 0, 100, steps[-1], max_scale)

    next_step = steps[0]
    current_floor = 0

    for step in steps:
        if score < step:
            next_step = step
            break
        current_floor = step

    # 3. CALCULATE PROGRESS
    points_needed = next_step - score
    band_range = next_step - current_floor
    if band_range == 0: band_range = 1

    progress = score - current_floor
    pct = (progress / band_range) * 100

    return (next_step, points_needed, pct, current_floor, max_scale)
