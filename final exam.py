print("Welcome to Inventory List Analyzer!")

items = []
categories = set()
quantity = {}


while True:
    name = input("\nEnter item name: ").strip()
    cat = input("Enter category: ").strip().lower()
    qty = int(input("Enter quantity: "))

    items.append((name, cat, qty))
    categories.add(cat)
    quantity[name] = qty

    more = input("\nDo you want to add more items? (y/n): ")
    if more == "n":
        break


q = []

for item in items:
    q.append(item[2])

print("\n========== INVENTORY SUMMARY ==========")

print("Total Different Items:", len(items))
print("Total Quantity in Stock:", sum(q))
print("Average Quantity:", sum(q) / len(q))
print("Minimum Quantity:", min(q))
print("Maximum Quantity:", max(q))


for item in items:
    if item[2] == max(q):
        print("Most Stocked Item:", item[0], "(", item[2], "units)")
    if item[2] == min(q):
        print("Least Stocked Item:", item[0], "(", item[2], "units)")


print("\nUnique Categories:", categories)


items.sort(key=lambda x: x[2], reverse=True)

print("\nItems Sorted by Quantity:")

i = 1
for item in items:
    print(i, ".", item[0], "-", item[2], "units")
    i = i + 1


print("\nCategories in Alphabetical Order:")

i = 1
for cat in sorted(categories):
    print(i, ".", cat)
    i = i + 1


search = input("\nSearch item or category: ").lower()

for item in items:
    if search in item[0].lower() or search in item[1]:
        print("Found:", item[0], "-", item[1], "-", item[2])

print("\n============ END OF REPORT ============")
