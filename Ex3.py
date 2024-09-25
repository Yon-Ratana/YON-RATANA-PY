# Ex3 - Dictionary or object
fruit_stock = [
    {'name': 'banana', 'quality': 30},
    {'name': 'coconut', 'quality': 10},
    {'name': 'mango', 'quality': 20},
    {'name': 'orange', 'quality': 42},
    {'name': 'apple', 'quality': 25},
]
# 1 - Update orange quality to 100
# fruit_stock[3]['quality']= 100
# print(fruit_stock)


#2 - Count the quality of fruit in stock
# fruit_stock = [
#     {'name': 'banana', 'quality': 30},
#     {'name': 'coconut', 'quality': 10},
#     {'name': 'mango', 'quality': 20},
#     {'name': 'orange', 'quality': 42},
#     {'name': 'apple', 'quality': 25},
# ]
# quality = 0
# for fruit in fruit_stock:
#     quality += fruit['quality']
# print( quality)

#3 - Which fruit have less in stock

# def min(array):
#     min_quality = array[0]["quality"]
#     min_fruit = array[0]["name"]
#     for fruit in array:
#         if fruit["quality"] < min_quality:
#             min_quality = fruit["quality"]
#             min_fruit = fruit["name"]
#     return min_quality, min_fruit
# print(min(fruit_stock))

#4 - Which fruit has the most in stock

most = fruit_stock[0]["quality"]
name = ""
for i in fruit_stock:
    if i["quality"] > most:
        most = i["quality"]
        name = i["name"]
total=  name + " "+ str(most)
print(total)

