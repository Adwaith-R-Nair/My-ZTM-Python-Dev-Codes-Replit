basket = ["Banana", "Apples", "Oranges", "Blueberries"]

new_basket = basket.remove("Banana")
print(basket)
print(new_basket)

new_basket = basket.pop()
print(basket)
print(new_basket)

new_basket = basket.append("Kiwi")
print(basket)
print(new_basket)

new_basket = basket.insert(0, "Apples")
print(basket)
print(new_basket)

count = basket.count("Apples")
print(count)

new_basket = basket.clear()
print(basket)
print(new_basket)