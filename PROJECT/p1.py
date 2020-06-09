# Project 1
# Irvan Tristian - 0447356121-105

priority = 0
email = 'irvantristian@gmail.com'

# Filter a list by first letter 
def letter_catalog(items, letter='A'):
    return [item for item in items if item[0] == letter]

# Return a dict from a list with fruit as key and fruit-counter as value 
def counter_item(items):
    return {item: items.count(item) for item in items}

# Calculate total price
def total_price(dcounter, fprice):
    return sum(dcounter[d] * fprice[d] for d in dcounter)

# Calculate discounted price
def discounted_price(total, discount, minprice=100):
    if total < minprice:
        return total
    return total - (total * discount / 100)

# Print total fruit, price, total price, and discounted price 
def print_summary(items, fprice):
    f_dict = counter_item(items)
    for f in sorted(f_dict):
        print(f"{f_dict[f]} {f} : {f_dict[f] * fprice[f]}")
    total = total_price(f_dict, fprice)
    discount = discounted_price(total, 10, minprice=100)
    print(f"total : {total}\ndiscount price : {discount}")


# Fruit & its price lists
fruits = ['Apple', 'Avocado', 'Banana', 'Blackberries', 'Blueberries',
          'Cherries', 'Date Fruit', 'Grapes', 'Guava', 'Jackfruit', 'Kiwifruit']
prices = [6, 5, 3, 10, 12, 7, 14, 15, 8, 7, 9]

# Cart list
chart = ['Blueberries', 'Blueberries', 'Grapes', 'Apple', 'Apple',
         'Apple', 'Blueberries', 'Guava', 'Jackfruit', 'Blueberries', 'Jackfruit']

# Dict comprehensions to populate the fruit and its price
fruit_price = {fruit: price for fruit, price in zip(fruits, prices)}

if __name__ == "__main__":
    print_summary(chart, fruit_price)
