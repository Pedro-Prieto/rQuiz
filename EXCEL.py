#dtype=pd.StringDtype
#import subprocess
#subprocess.check_call(['python', '-m', 'pip', 'install', 'openpyxl'])
#import pip

import pandas as pd
#REGistro DF
registro = pd.read_csv(r'C:\FINAL\REGISTRO\REG.txt', sep=";", header=None)
registro.columns = ["F", " (0)S", "D/A", "T", "E", "P"]

registro.to_excel(r"C:\FINAL\REGISTRO\REG.xlsx", index = None, header=True)