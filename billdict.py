shopping_items = {"eggs": 1.85, "bread": 1.50, "peppers": 0.90}
# print only values -

print(shopping_items.values())

# print the total bill -

total_bill = 0

for i in shopping_items.values():
    total_bill = total_bill + i

print(total_bill)
# print item with it's cost - ' \

print(shopping_items)

# create a function called food_bill and return above outcome

def food_bill(shopping_items):
    bill = 0

    for j in shopping_items.values():
        bill = bill + j

    return bill

print(food_bill(shopping_items))