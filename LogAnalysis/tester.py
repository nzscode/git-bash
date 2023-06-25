basket = [("apples", 5), ("cantaloupe", 9), ("dates", 3), ("apples", 10), ("pears", 8)]
fruits = {
    "apples": 2,
    "oranges": 5,
    "pears": 3
}

# for fruit in fruits:
#     fruits[fruit] += 1
#
# print(fruits)

fruit_list = {}
for i in range(len(basket)):
    basket_item = basket[i][0]
    if basket_item in fruits:
        fruits[basket_item] += int(basket[i][1])
    elif basket_item not in fruits:
        fruits[basket_item] = int(basket[i][1])

print(fruits)