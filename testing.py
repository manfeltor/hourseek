#! python3

import pandas as pd, re

prbRe = re.compile(r"(\d{1,2}[.:]\d{1,2}|\d{1,4}) [AayY] (\d{1,2}[.:]\d{1,2}|\d{1,4})")  # codigo Regex
def hourleek(df: pd.DataFrame, column: str) -> pd.DataFrame:
    matches = df[column].str.extract(prbRe, expand=True)
    new_column_names = [f"{column_name}_group{i}" for i in range(1, len(matches.columns) + 1)]