import json
import math

with open("car_sales.json", 'r') as car_sales:
    data = json.load(car_sales)


max_revenue = 0
best_seller = ""
best_seller_quantity = 0
best_seller_price = 0
best_seller_id = 0
car_makes = []
popular_models = {}
popular_year_sale = {}

for id in data:
    # print(f"id: {id['total_sales']}")
    price = id['price']
    price = price.strip('$')
    sales_total = id['total_sales']
    total_revenue = math.floor(float(price) * sales_total)
    # print(id["car"]["car_model"])
    if total_revenue > max_revenue:
        max_revenue = total_revenue
        best_seller = id['car']['car_make']
        best_seller_price = id['price']
        best_seller_id = id['id']

    model_name = id["car"]["car_model"]
    model_quantity_sold = id["total_sales"]
    if model_name in popular_models.keys():
        popular_models[model_name] += model_quantity_sold
    else:
        popular_models[model_name] = model_quantity_sold

    car_year = id["car"]["car_year"]
    if car_year in popular_year_sale:
        popular_year_sale[car_year] += id["total_sales"]
    else:
        popular_year_sale[car_year] = id["total_sales"]


sorted_popular_models = sorted(popular_models.items(), key=lambda x: x[1], reverse=True)
sorted_popular_years = sorted(popular_year_sale.items(), key=lambda x: x[1], reverse=True)

print(f"Best Seller: {best_seller}, Max Revenue: {max_revenue}, Car Price: {best_seller_price}, id: {best_seller_id}")
print(f"The {sorted_popular_models[0][0]} had the most sales: {sorted_popular_models[0][1]}")
print(f"The most popular year was {sorted_popular_years[0][0]} with {sorted_popular_years[0][1]} sales.")
