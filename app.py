import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("🚀 Financial Fraud Detection Analysis Started")

# Load dataset
df = pd.read_csv("data/creditcard.csv")

import os
import pandas as pd
import matplotlib.pyplot as plt

# ---------- ensure reports folder exists ----------
os.makedirs("reports", exist_ok=True)

# ---------- 1) Fraud vs Normal (bar chart) ----------
counts = df["Class"].value_counts().sort_index()   # 0 then 1
plt.figure()
plt.bar(["Normal", "Fraud"], [counts.get(0, 0), counts.get(1, 0)])
plt.title("Fraud vs Normal Transactions")
plt.xlabel("Class")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("reports/fraud_vs_normal.png", dpi=200)
plt.close()

# ---------- 2) Amount distribution (hist) ----------
plt.figure()
plt.hist(df["Amount"], bins=50)
plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("reports/amount_distribution.png", dpi=200)
plt.close()

# ---------- 3) Amount by class (overlay hist) ----------
normal_amt = df.loc[df["Class"] == 0, "Amount"]
fraud_amt  = df.loc[df["Class"] == 1, "Amount"]

plt.figure()
plt.hist(normal_amt, bins=50, alpha=0.7, label="Normal")
plt.hist(fraud_amt,  bins=50, alpha=0.7, label="Fraud")
plt.title("Amount Distribution: Fraud vs Normal")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("reports/fraud_amount.png", dpi=200)
plt.close()

print("✅ Saved 3 plots in reports/: fraud_vs_normal.png, amount_distribution.png, fraud_amount.png")

print("\nDataset Loaded Successfully!")
print("Total Rows:", len(df))
print("Total Columns:", len(df.columns))

fraud = df['Class'].value_counts()[1]
normal = df['Class'].value_counts()[0]

print(f"\nFraud Transactions: {fraud}")
print(f"Normal Transactions: {normal}")
print(f"Fraud Percentage: {(fraud/len(df))*100:.4f}%")

# ------------------ VISUALIZATION ------------------

import os
os.makedirs("reports", exist_ok=True)

# Fraud vs normal
plt.figure(figsize=(6,4))
sns.countplot(x='Class', data=df)
plt.title("Fraud vs Normal Transactions")
plt.xticks([0,1], ["Normal","Fraud"])
plt.savefig("reports/fraud_vs_normal.png")
plt.show()

# Amount distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Amount'], bins=50)
plt.title("Transaction Amount Distribution")
plt.savefig("reports/amount_distribution.png")
plt.show()

# Fraud only amount
fraud_df = df[df['Class']==1]

plt.figure(figsize=(8,5))
sns.histplot(fraud_df['Amount'], bins=50, color='red')
plt.title("Fraud Transaction Amount")
plt.savefig("reports/fraud_amount.png")
plt.show()

# Transaction amount distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Amount'], bins=50)
plt.title("Transaction Amount Distribution")
plt.show()

# Fraud transaction amount only
fraud_df = df[df['Class']==1]

plt.figure(figsize=(8,5))
sns.histplot(fraud_df['Amount'], bins=50, color='red')
plt.title("Fraud Transaction Amount Distribution")
plt.show()

import seaborn as sns

print("Creating professional charts...")

# correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.savefig("reports/correlation_heatmap.png")
plt.close()

# fraud percentage pie chart
fraud_counts = df["Class"].value_counts()
plt.figure()
plt.pie(fraud_counts, labels=["Normal","Fraud"], autopct="%1.2f%%")
plt.title("Fraud Percentage")
plt.savefig("reports/fraud_percentage.png")
plt.close()

print("All professional charts created!")