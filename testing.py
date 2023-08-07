#! python3

import pandas as pd, re


def hourleek(df: pd.DataFrame, column: str) -> pd.DataFrame:
    prbRe = re.compile(r"(\d{1,2}[.:]\d{1,2}|\d{1,4}) [AayY] (\d{1,2}[.:]\d{1,2}|\d{1,4})")  # codigo Regex
    raw = df[column]
    dic1 = {
        "lav_11": [],
        "lav_12": [],
        "lav_21": [],
        "lav_22": [],
        "sab_11": [],
        "sab_12": []
    }
# de lo que estoy deduciendo del original, tengo que separar las columnas en las cuales este contenido el sabado
# y separarlas del resto del rex, sera viable?
    for i in raw:
        i = str(i)
        mtch1 = prbRe.search(i)
        if mtch1 == None:
            dic1["lav_11"].append("sin match")
            dic1["lav_12"].append("sin match")
            dic1["lav_21"].append("sin match")
            dic1["lav_22"].append("sin match")
            dic1["sab_11"].append("sin match")
            dic1["sab_12"].append("sin match")
        else:
            if "sab" in i: