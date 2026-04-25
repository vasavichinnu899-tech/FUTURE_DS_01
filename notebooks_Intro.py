import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Dataset
df = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "Revenue": [41000,47000,63000,56000,59000,55000,74000,82000,51000,2000,71000,34000],
    "Profit":  [15000,18000,20000,16000,18000,19000,22000,27000,14000,500,21000,9000]
})

# 🔥 Add Profit Margin column (NEW)
df["Profit_Margin"] = (df["Profit"] / df["Revenue"]) * 100

print(df)

# -------------------------------
# 📊 Monthly Revenue vs Profit
x = np.arange(len(df["Month"]))

plt.figure()
plt.bar(x-0.2, df["Revenue"], width=0.4, label="Revenue")
plt.bar(x+0.2, df["Profit"], width=0.4, label="Profit")

plt.xticks(x, df["Month"])
plt.xlabel("Month")
plt.ylabel("Amount")
plt.title("Monthly Revenue vs Profit")
plt.legend()
plt.show()

# -------------------------------
# 📊 Revenue by Product (sorted 🔥)
products = ["Camera","Tablet","Headphones","Laptop","Phone","Printer"]
revenue = [176500,123700,105600,101900,71200,55200]

sorted_data = sorted(zip(revenue, products))
revenue_sorted, products_sorted = zip(*sorted_data)

plt.figure()
plt.barh(products_sorted, revenue_sorted)
plt.title("Revenue by Product")
plt.xlabel("Revenue")
plt.show()

# -------------------------------
# 📊 Revenue by Region
regions = ["East","South","West","North"]
values = [37.9,26.5,21.5,14.1]

plt.figure()
plt.pie(values, labels=regions, autopct='%1.1f%%')
plt.title("Revenue by Region")
plt.show()

# -------------------------------
# 📊 Orders by Payment
payment = ["Credit Card","UPI","Cash","Net Banking","Debit Card"]
orders = [26,22,21,18,13]

plt.figure()
plt.barh(payment, orders)
plt.title("Orders by Payment Channel")
plt.xlabel("Orders")
plt.show()

# -------------------------------
# 📊 Revenue by Category
categories = ["Electronics","Accessories","Office Supplies"]
values = [470000,105000,55000]

plt.figure()
plt.bar(categories, values)
plt.title("Revenue by Category")
plt.show()

# -------------------------------
# 📊 Profit Margin by Product (better calc)
profit_margin = [30,32,31,29,27,28]

plt.figure()
plt.barh(products, profit_margin)

avg = np.mean(profit_margin)
plt.axvline(avg, linestyle='--', label="Average")

plt.title("Avg Profit Margin by Product")
plt.legend()
plt.show()

# -------------------------------
# 📊 Quarterly Revenue & Profit
quarters = ["Q1","Q2","Q3","Q4"]
rev_q = [150000,170000,210000,110000]
profit_q = [52000,54000,63000,32000]

plt.figure()
plt.bar(quarters, rev_q, label="Revenue")
plt.plot(quarters, profit_q, marker='o', label="Profit")

plt.legend()
plt.title("Quarterly Revenue & Profit")
plt.show()

# -------------------------------
# 📊 Heatmap
heat_data = np.array([
    [93709,29754,16409,38603],
    [14350,0,38450,52774],
    [22001,18272,42778,18871],
    [25508,9490,24185,11982],
    [38224,12436,694,3823],
    [46384,19355,45666,12292]
])

regions = ["East","North","South","West"]

plt.figure()
plt.imshow(heat_data)

plt.xticks(np.arange(len(regions)), regions)
plt.yticks(np.arange(len(products)), products)

for i in range(len(products)):
    for j in range(len(regions)):
        plt.text(j, i, heat_data[i][j], ha='center', va='center')

plt.title("Revenue: Product x Region")
plt.colorbar()
plt.show()

# -------------------------------
# 📊 Units Sold
units = [210,155,140,130,98,50]

plt.figure()
plt.bar(products, units)
plt.title("Units Sold by Product")
plt.show()

# -------------------------------
# 📊 Profit Distribution
plt.figure()
plt.hist(profit_margin, bins=6)

avg = np.mean(profit_margin)
plt.axvline(avg, linestyle='--')

plt.title("Profit Margin Distribution")
plt.show()

# -------------------------------
# 📊 Scatter Plot
np.random.seed(0)
rev = np.random.randint(1000, 20000, 50)
profit = rev * np.random.uniform(0.1, 0.5, 50)

plt.figure()
plt.scatter(rev, profit)

plt.xlabel("Revenue")
plt.ylabel("Profit")
plt.title("Revenue vs Profit")
plt.show()

# -------------------------------
# 📊 KPI SCORECARD (improved 🔥)
print("\n----- KPI SCORECARD -----")
print("Total Revenue :", df["Revenue"].sum())
print("Total Profit  :", df["Profit"].sum())
print("Average Margin (%) :", round(df["Profit_Margin"].mean(),2))
print("Best Month :", df.loc[df["Revenue"].idxmax(), "Month"])
print("Worst Month :", df.loc[df["Revenue"].idxmin(), "Month"])
