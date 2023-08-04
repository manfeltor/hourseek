#! python3

import pandas as pd, re

prbRe = re.compile(r"(\d{1,2}[.:]\d{1,2}|\d{1,4}) [AayY] (\d{1,2}[.:]\d{1,2}|\d{1,4})")  # codigo Regex
def hourleek(df: pd.DataFrame, column: str) -> pd.DataFrame:
    raw = df[column]
# de lo que estoy deduciendo del original, tengo que separar las columnas en las cuales este contenido el sabado
# y separarlas del resto del rex, sera viable?
    for i in raw:
        if "sab" in i.lower():
            i = i[:i.lower().index("sab")]
            j = i[i.lower().index("sab"):]
        if "dom" in i.lower():
            i = i[:i.lower().index("dom")]
            j = i[i.lower().index("dom"):]
