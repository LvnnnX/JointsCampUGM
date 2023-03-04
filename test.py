import pandas as pd
import numpy as np
import pathlib

PATH = pathlib.Path(__file__).parent
DDIR = PATH / "Dataset"

df = pd.read_csv(f'{DDIR}/Telco-Customer-Churn.csv')

CWD = pathlib.Path.cwd()
print(CWD)