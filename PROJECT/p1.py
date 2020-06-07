# nama file p1.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded
# Isikan juga priority file

# untuk resubmisi, grader hanya akan mengambil priority yang paling besar
# jadi kalau anda ingin merevisi kode anda:
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0

priority = 0


#netacad email cth: 'abcd@gmail.com'
email='irvantristian@gmail.com'

# copy-paste semua #Graded cells di bawah ini

# PASTE KODE ANDA DISINI 
#Graded

# Manual, filter, list comprehension
def letter_catalog(items,letter='A'):
  # MULAI KODEMU DI SINI
  # ini kode saya dst TENTUNYA SUDAH DIKERJAKAN!
  return [item for item in items if item[0] == letter]

#Graded

def counter_item(items):
  # MULAI KODEMU DI SINI
  # ini kode saya dst TENTUNYA SUDAH DIKERJAKAN!
  return {item: items.count(item) for item in items}

#Graded

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = {fruit: price for fruit, price in zip(fruits, prices)} # ini kode saya dst TENTUNYA SUDAH DIKERJAKAN!

def total_price(dcounter,fprice):
  # MULAI KODEMU DI SINI
  # ini kode saya dst
  return sum(dcounter[d] * fprice[d] for d in dcounter)

#Graded

def discounted_price(total,discount,minprice=100):
  # MULAI KODEMU DI SINI
  # ini kode saya dst TENTUNYA SUDAH DIKERJAKAN!
  if total < minprice:
    return total
  return total - (total * discount / 100)


#Graded

def print_summary(items,fprice):
  # MULAI KODEMU DI SINI
  # ini kode saya dst TENTUNYA SUDAH DIKERJAKAN!
  f_dict = counter_item(items)
  for f in sorted(f_dict):
    print(f"{f_dict[f]} {f} : {f_dict[f] * fprice[f]}")
    total = total_price(f_dict, fprice)
    discount = discounted_price(total, 10, minprice=100)
  print(f"total : {total}\ndiscount price : {discount}")


print_summary(chart, fruit_price)
