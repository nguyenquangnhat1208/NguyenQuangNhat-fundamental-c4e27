price = {"banana":4,"apple":2,"orange":1.5,"pear":3}
stock = {"banana":6,"apple":0,"orange":32,"pear":15}
total = 0 
for k in price.keys():
    print(k)
    print("price:", price[k])
    print("stock:",stock[k])
    total = total + price[k] * stock[k]
print("total : ",total)


