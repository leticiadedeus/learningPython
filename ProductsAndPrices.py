shopp = cK = c = lowerP = 0
lowerPname = ''
while True:
    name = str(input('Product: '))
    price = float(input('Price: '))
    if c == 0:
        lowerPname = name
        lowerP = price
    if price > 1000:
        cK += 1
    if price < lowerP:
        lowerPname = name
        lowerP = price
    shopp = shopp + price
    c += 1
    yn = input('insert more products?(y/n): ')
    if yn == 'n':
        break
print(f'Total of the shopping: {shopp}')
print(f'More than 1000 products: {cK}')
print(f'The lower price of a product is the {lowerPname}')
