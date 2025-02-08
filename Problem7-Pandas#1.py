import csv
with open('sales_data.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    revenue_per_product = {}

    for row in reader:
        product = row[0]
        quantity = int(row[1])
        price = float(row[2])

        revenue = quantity * price
        if product in revenue_per_product:
            revenue_per_product[product] += revenue
        else:
            revenue_per_product[product] = revenue

print(revenue_per_product)
