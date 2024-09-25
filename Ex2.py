# Adding new fruit: Orange with amount of 100

fruit_stock = {'banana': 3, 'coconut': 30, 'mango': 21}
fruit_stock['orange'] = 100
print(fruit_stock)


#2 - Find average all fruits

fruit_stock = {'banana': 3, 'coconut': 30, 'mango': 21}
total = sum(fruit_stock.values())
number = len(fruit_stock)
average = total / number
print(average)

#3 - Find total fruit in stock

fruit_stock = {'banana': 3, 'coconut': 30, 'mango': 21}
fruit = sum(fruit_stock.values())
print(fruit)

#4 - Now change fruit_stock to be input that you can input differneces fruit

def stock(fruit_stock):
    new_fruit={}
    for fruit in fruit_stock:
        if fruit == "mango":
            new_fruit["gape"]=20
        else:
            new_fruit[fruit]=fruit_stock[fruit]
    return new_fruit
fruit_stock = {'banana':3,'coconut':30,'mango':21}
print(stock(fruit_stock))


