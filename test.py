<<<<<<< HEAD
# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np

# Original example dataframes
data = {
    "name": ["Amit", "Ravi", "Neha", "SAm"],
    "age": [21, 22, 20, 22],
    "marks": [85, 90, 78, 99]
}
=======
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- DATA --------------------
basic = pd.DataFrame({
    "name": ["Amit", "Ravi", "Neha", "Shambhu", "Sam", "Ram"],
    "age": [21, 22, 20, 22, 34, 44]
})
>>>>>>> fd911962 (Data Visulazation With Practice Set Done:zap:)

result = pd.DataFrame({
    "name": ["Shambhu", "Sam", "Ram"],
    "marks": [90, 99, 94],
    "result": ["Pass", "Fail", "Pass"],
    "grade": ["A", "B", "A"]
})

# -------------------- MERGE --------------------
df = pd.merge(basic, result, on="name", how="left")

# -------------------- FEATURE ENGINEERING --------------------
df["computed_result"] = np.where(df["marks"] >= 40, "Pass", "Fail")

df["inconsistency"] = np.where(
    (df["result"].notna()) & (df["result"] != df["computed_result"]),
    "Mismatch",
    "OK"
)

# -------------------- INSIGHTS --------------------
print("\nFinal Dataset:\n")
print(df)

<<<<<<< HEAD
data2 = {
    "name": ["sohit", "Ram", "Kisho"],
    "age": [22, 23, 23],
    "Marks": [22, 25, 88]
}

df1 = pd.DataFrame(data2)
print(df1)

# --- New: sample price data + seaborn plots ---
# Generate sample time-series price data for two products
np.random.seed(42)
dates = pd.date_range(start='2026-01-01', periods=10, freq='D')
prices = []
for item in ['Product_A', 'Product_B']:
    base = 100 if item == 'Product_A' else 120
    series = base + np.cumsum(np.random.normal(0, 2, size=len(dates)))
    for d, p in zip(dates, series):
        prices.append({'date': d, 'item': item, 'price': round(float(p), 2)})

# Create dataframe of prices
df_prices = pd.DataFrame(prices)
print("\nPrice data sample:")
print(df_prices.head())

# Plot price over time using seaborn
sns.set(style='darkgrid')
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_prices, x='date', y='price', hue='item', marker='o')
plt.title('Price over time (sample data)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.tight_layout()
plt.savefig('prices_plot.png')
print("Saved prices_plot.png")
plt.tight_layout()
plt.xlabel("New")
plt.savefig('prices_dist.png')
print("Saved prices_dist.png")
# Plot price distribution
plt.figure(figsize=(8, 4))
sns.histplot(data=df_prices, x='price', hue='item', kde=True, element='step')
plt.title('Price distribution (sample data)')


# If running interactively, show the plots
try:
    plt.show()
except Exception:
    # In non-interactive environments, plt.show() may fail; that's fine because we saved the files
    pass
=======
print("\nStatistical Summary:\n")
print(df.describe())

# -------------------- VISUALIZATION --------------------
plt.figure(figsize=(8,4))
sns.barplot(data=df, x="name", y="marks", palette="viridis")
plt.title("Marks by Student")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(
    data=df,
    x="age",
    y="marks",
    hue="computed_result",
    style="inconsistency",
    s=120
)
plt.title("Age vs Marks (Logic Checked)")
plt.tight_layout()
plt.show()

marks_clean = df["marks"].dropna()

plt.figure(figsize=(6,4))
plt.hist(marks_clean, bins=5, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
>>>>>>> fd911962 (Data Visulazation With Practice Set Done:zap:)
