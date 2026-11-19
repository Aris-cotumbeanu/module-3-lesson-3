def claculate_change(paid, price):
    change = paid - price
    return change

snack_price = 25
print("=====SNACK VENDING MACHINE=====")
print(f"This snack costs {snack_price}units.")
print("acepted coins:1,5,10,25\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert coin(1, 5, 10, or 25: "))

    if coin!=1 and coin!=5 and coin!=10 and coin!=25:
        print("Invalid coin. Please insert a valid coin.")
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"inserted: {coin}. total so far: {total_inserted}\n")


    if total_inserted >= snack_price:
        print("enough money inserted!\n")
        break

change_due = claculate_change(total_inserted, snack_price)

print("dispensing snack...")

if change_due == 0:
    pass
else:
    print(f"here is your change: {change_due}units.")

print("\n=====purchase summary=====")
print("snack_price: ", snack_price)
print("coins inserted: ", coins_inserted)
print("total paid: ", total_inserted)
print("change given: ", change_due)
print("===========================")
print("Thank you for your purchase!")