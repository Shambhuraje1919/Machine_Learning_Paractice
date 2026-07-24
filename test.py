# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- DATA --------------------
basic = pd.DataFrame({
    "name": ["Amit", "Ravi", "Neha", "Shambhu", "Sam", "Ram"],
    "age": [21, 22, 20, 22, 34, 44]
})

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

print("\nStatistical Summary:\n")
print(df.describe())

# -------------------- VISUALIZATION --------------------
plt.figure(figsize=(8, 4))
sns.barplot(data=df, x="name", y="marks", palette="viridis")
plt.title("Marks by Student")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("marks_by_student.png")

plt.figure(figsize=(6, 4))
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
plt.savefig("age_vs_marks.png")

marks_clean = df["marks"].dropna()

plt.figure(figsize=(6, 4))
plt.hist(marks_clean, bins=5, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("marks_distribution.png")

print("Saved plots: marks_by_student.png, age_vs_marks.png, marks_distribution.png")