import operator
fruits = {
    "Tangerines": [12, "orange"],
    "Bananas": [3, "yellow"],
    "Olives": [9, "black"],
    "Grapes": [5, "purple"],
    "Kiwi": [2, "green"],
    "Avocado": [8, "green"],
}
sorted_fruits = sorted(fruits.items(), key=operator.itemgetter(0), reverse=True)
# print(sorted_fruits)
fruits_list = []
# for fruit in fruits:
#     fruits_list.append([fruit, fruits[fruit][0], fruits[fruit][1]])

# fruits_list.sort(key=lambda a: a[2], reverse=True)
for fruit in sorted_fruits:
    fruits_list.append([fruit[0], fruit[1][0], fruit[1][1]])
fruits_list.insert(0, ["Fruits", "Count", "Color"])
print(fruits_list)
# print(sorted_fruits[0][0])