# Program Sandwich Shop
welc_mess = "Welcome to the Sandwich Food Truck!"
ord_mess = "\nWhat sandwich would you like to order?"
ord_mess += "(type 'ok' to finish): "

sand_orders = []
finished_sand = []

print(welc_mess)
active = True
while active:
    order = input(ord_mess).lower()
    if order == 'ok':
        active = False
    else:
        sand_orders.append(order)
        print(f"You have ordered a {order.title()} sandwich, nice!")

if 'pastrami' in sand_orders:
    while 'pastrami' in sand_orders:
        sand_orders.remove('pastrami')
    print(f"Sorry, we ran out of Pastrami.")

# Control
print(sand_orders)

while sand_orders:
    swap = sand_orders.pop()
    print(f"We have made your {swap.title()}...")
    finished_sand.append(swap)

print(f"\nThe following sandwiches have been made:")
for s_i in finished_sand:
    print(f"\t{s_i.title()} sandwich!")