# Ex1 - Object
# object = {
#     {"name": " banana","price":2},
#     {"name": "coconut","price":4},
#     {"name": "mango","price":3},
# }
#Question - Add items to object with difference price
def add(name, price):
    item = {"name": name, "price": price}
    list.append(item)
    return list

list = []
add(input(" fruit name: "), int(input("fruit price: ")))
add(input("fruit name: "), int(input("fruit price: ")))
add(input("fruit name: "), int(input("fruit price: ")))
for items in list:
    print(items)

