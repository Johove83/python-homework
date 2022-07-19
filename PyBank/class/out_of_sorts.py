import pandas as pd
from pathlib import Path
%matplotlib inline

csv_path = Path("tsla_google_finance.csv")
tsla_df = pd.read_csv(csv_path)
tsla_df.head()