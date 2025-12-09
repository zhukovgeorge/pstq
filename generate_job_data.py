# generate_job_data.py
import pandas as pd
from pathlib import Path

EXCEL_PATH = Path("LIS_Diagnostics_moyen_terme_2024-2028_516_professions.xlsx")
OUT_PATH = Path("job_data.py")


def esc(s: str) -> str:
    """Escape single quotes for embedding in single-quoted Python strings."""
    return s.replace("\\", "\\\\").replace("'", "\\'")


def main():
    df = pd.read_excel(EXCEL_PATH)

    lines = []
    lines.append("# job_data.py")
    lines.append("# Diagnostics de main-d'œuvre (2024-2028)")
    lines.append("# Source: LIS_Diagnostics_moyen_terme_2024-2028_516_professions.xlsx")
    lines.append("")
    lines.append("JOBS = [")

    for _, row in df.iterrows():
        noc = str(row["CNP 2021"]).strip()
        title_fr = str(row["Titre de la profession (FR)"]).strip()
        title_en = str(row["Profession title (EN)"]).strip()
        diagnosis = str(row["Diagnostic"]).strip()
        category = str(row["Category"]).strip()
        sub_category = str(row["Sub-Category"]).strip()

        lines.append(
            "    {"
            f"'NOC': '{esc(noc)}', "
            f"'Title (FR)': '{esc(title_fr)}', "
            f"'Title (EN)': '{esc(title_en)}', "
            f"'Diagnosis': '{esc(diagnosis)}', "
            f"'Category': '{esc(category)}', "
            f"'Sub category': '{esc(sub_category)}'"
            "},"
        )

    lines.append("]")
    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
