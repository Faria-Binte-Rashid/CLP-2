import matplotlib.pyplot as plt
regions = ["North", "South", "East", "West"]
revenue = [5000, 7000, 6000, 8000]
plt.bar(regions, revenue, color='blue')
plt.xlabel("Regions")
plt.ylabel("Sales Revenue ($)")
plt.title("Sales Revenue by Region")
plt.show()
