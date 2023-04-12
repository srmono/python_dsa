# return total cart values

products_in_cart = [
    {
        "id": 1,
        "name": "mobile",
        "price": 20000,
        "qty":2
    },
    {
        "id": 2,
        "name": "power_bank",
        "price": 1000,
        "qty": -1
    },
    {
        "id": 3,
        "name": "mobile_pouch",
        "price": 250
    }
]

# get product in list
# print(products_in_cart[0])

# # get price from product in list
# print(products_in_cart[0]["price"])

def get_total_cart_value(lop):
    sum = 0
    for prod in lop:
        # print(prod)
        # print(prod["price"])
        sum += prod["price"]
    print("Total cart value: ", sum )
        
get_total_cart_value(products_in_cart)

# def cart(product):
#     sum=0
#     for i in range(len(product)):
#         sum +=product[i]['price']
#     print("total_value", sum)
    
# cart(products_in_cart)
