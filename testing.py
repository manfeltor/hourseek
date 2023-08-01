#! python3

import pandas as pd, re

prbRe = re.compile(r"(\d{1,2}[.:]\d{1,2}|\d{1,4}) [AayY] (\d{1,2}[.:]\d{1,2}|\d{1,4})")  # codigo Regex
def hourleek(df: pd.DataFrame, column: str) -> pd.DataFrame:
    finalList = []
