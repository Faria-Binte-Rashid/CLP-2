import matplotlib.pyplot as plt
weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
temp_values = [18, 21, 19, 23, 22, 26, 27]
plt.plot(weekdays, temp_values, marker='s', linestyle='--', color='r')
plt.xlabel("Weekdays")
plt.ylabel("Temperature (°C)")
plt.title("Weekly Temperature Trends")
plt.show()
