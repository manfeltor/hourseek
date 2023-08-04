#! python3

import pandas as pd, re, sqlite3


def openfile(fpath):

    r"""turns file into pd data frames.
    this function imports file from given file path as string and returns a pandas data frame for the rest of the code.

    suports "xls", "xlsx", "xlsm", "xlsb", "odf", "ods", "odt" extentions for worksheets
    as well as csv, json, db and htmln for others.

    example:
    openfile("C:\Users\user1\folder...... \myfile.xlsx)
    would return the same database as the file, but pandas library workable.

    please make sure of this:
    * your file does not have corrupted info
    * the column header of the column that contains the time-lapse has a valid header
    written in ASCII characters"""

    xlExtensions = ("xls", "xlsx", "xlsm", "xlsb", "odf", "ods", "odt")
    prex = re.compile(r"(?P<ext>\w+).(\w+)")
    match1 = prex.search(fpath[::-1])
    fextension = match1.group("ext")[::-1]
    if fextension in xlExtensions:
        df = pd.read_excel(fpath)
    elif fextension == "csv":
        df = pd.read_csv(fpath)
    elif fextension == "json":
        df = pd.read_json(fpath)
    elif fextension == "db":
        cone = sqlite3.connect(fextension)
        df = pd.read_sql(fpath, cone)
    elif fextension == "html":
        df = pd.read_html(fpath)
    else:
        raise ValueError("File extension not supported. Please provide a valid file.")
    return df
