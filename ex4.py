# Ex4 - Dictionary or object
fruit_stock = [
    {'name': 'banana', 'quality': 1},
    {'name': 'coconut', 'quality': 8},
    {'name': 'mango', 'quality': 10},
    {'name': 'orange', 'quality': 0},
    {'name': 'apple', 'quality': 5},
]
#1 - Display fruit that has in stock
for fruit in fruit_stock:
    if fruit['quality'] > 0:
        print(fruit)
#2 - Display fruit that has more than 5 in stock
for fruit in fruit_stock:
    if fruit['quality'] > 5:
        print(fruit)
#3 - Increase quality of fruit that has less than 10 in stock to 20
for friut in fruit_stock:
    if friut["quality"]<10:
        friut["quality"]=20
    print(friut)
        