import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/creditcard.csv")

def run():
    print("✅ Project started")
    print("Looking for dataset at:", DATA_PATH)

    if not DATA_PATH.exists():
        print("❌ creditcard.csv not found inside /data folder.")
        return

    df = pd.read_csv(DATA_PATH)
    print("✅ Dataset loaded!")
    print("Shape:", df.shape)
    print(df.head())