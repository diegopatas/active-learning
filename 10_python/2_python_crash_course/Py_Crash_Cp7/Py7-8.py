# Program of Sandwiches order
w_mess = "Welcome to the Sandwich factory!"
o_mess = "What sandwich do you want to order?"
o_mess += "(Type 'ok' to finish): "

sandwich_orders = []
finished_sandwiches = []

print(w_mess)
active = True
while active:
    order = input(o_mess).lower()
    if order == 'ok':
        active = False
    else:
        sandwich_orders.append(order)
        print(f"Nice, you ordered a {order.title()}!\n")

while sandwich_orders:
    sand_prep = sandwich_orders.pop()
    print(f"I made your {sand_prep.title()} sandwich...")
    finished_sandwiches.append(sand_prep)

print("\nThe following sandwiches have been made:")
for s_i in finished_sandwiches:
    print(f"\t{s_i.title()}!")

print(f"Have a good meal. :) ")