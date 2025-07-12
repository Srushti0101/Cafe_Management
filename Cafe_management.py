menu = {
    "Pizza" : 80,
    "Pasta" : 50,
    "Burgar" : 60,
    "Salad" : 70,
    "Coffee" : 80
}

print("\nWelcome To My Restaurant :")
for key,val in menu.items():
    print(key,"=",val)

order_total = 0

item_1 = input("Enter the name of item you want to order :")

if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been  added  to your order.")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("\nDo you want to add another item? (Yes/No) : ")

if another_order == "Yes":
    item_2 = input("\nEnter the name of second  item = ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"Item {item_2} has been  added  to order.\n")
    else:
        print(f"Ordered item {item_1} is not available!\n")

print(f"\nThe total amount of items to pay is {order_total}.\n")