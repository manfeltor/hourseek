#! python3
import testing
import imp1

def rall(fpth: str, col: str):
    df = imp1.openfile(fpth)
    testing.hourleek(df, col)


a = rall(r"C:\Users\ftorres\Documents\py\test.xlsx", "observaciones")
