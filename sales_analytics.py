"""
=============================================================
  BUSINESS SALES ANALYTICS — Task1_Bussiness_sales_analysis
=============================================================
"""

# ── 0. IMPORTS ────────────────────────────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import warnings
import os

warnings.filterwarnings("ignore")

# Method 1 (BEST)
FILE = r"C:\Users\USER\Downloads\Task1 Bussiness sales analysis.xlsx"
# Check file exists
if not os.path.exists(FILE):
    print("❌ File not found. Check file name/path.")
    exit()

# ─────────────────────────────────────────────────────────
# STEP 1 — LOAD & INSPECT DATA
# ─────────────────────────────────────────────────────────
print("=" * 60)
print("STEP 1 : LOAD & INSPECT DATA")
print("=" * 60)

df = pd.read_excel(FILE)

print("\n✅ File loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumns & Data Types:\n", df.dtypes)
print("\nFirst 3 Rows:\n", df.head(3))
print("\nSummary:\n", df.describe().round(2))

# ─────────────────────────────────────────────────────────
# STEP 2 — DATA CLEANING
# ─────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 2 : DATA CLEANING")
print("=" * 60)

print("\nMissing Values:\n", df.isnull().sum())

df.drop_duplicates(inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month
df["Month_Name"] = df["Date"].dt.strftime("%b")
df["Quarter"] = df["Date"].dt.quarter.map({1:"Q1",2:"Q2",3:"Q3",4:"Q4"})

# ─────────────────────────────────────────────────────────
# STEP 3 — KPI
# ─────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("STEP 3 : KPI")
print("=" * 60)

total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()

print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)

# ─────────────────────────────────────────────────────────
# STEP 4 — GROUPINGS
# ─────────────────────────────────────────────────────────
product_stats = df.groupby("Product")["Revenue"].sum().sort_values()
region_stats = df.groupby("Region")["Revenue"].sum()
monthly = df.groupby("Month_Name")["Revenue"].sum()

# ─────────────────────────────────────────────────────────
# STEP 5 — VISUALIZATION
# ─────────────────────────────────────────────────────────
plt.figure(figsize=(15,10))

# Product Revenue
plt.subplot(2,2,1)
product_stats.plot(kind='barh', title="Revenue by Product")

# Region Pie
plt.subplot(2,2,2)
region_stats.plot(kind='pie', autopct='%1.1f%%', title="Revenue by Region")

# Monthly Trend
plt.subplot(2,2,3)
monthly.plot(kind='line', marker='o', title="Monthly Revenue")

# Scatter Plot
plt.subplot(2,2,4)
plt.scatter(df["Revenue"], df["Profit"])
plt.title("Revenue vs Profit")
plt.xlabel("Revenue")
plt.ylabel("Profit")

plt.tight_layout()

# Save Dashboard
out_path = r"C:\Users\USER\Downloads\sales_dashboard.png"
plt.savefig(out_path)

plt.show()

print(f"\n✅ Dashboard saved at: {out_path}")
print("\n✅ ANALYSIS COMPLETED SUCCESSFULLY!")
