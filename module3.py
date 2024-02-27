sales_tax = .08
tip = .18
subtotal = float(input('Please enter the charge for the food: '))
tax_amount = subtotal * sales_tax
tip_amount = subtotal * tip
total = subtotal + tax_amount + tip
print('Subtotal: $' + str(subtotal))
print('Tax: $' + str(tax_amount))
print('Tip: $' + str(tip_amount))
print('Total: $' + str(total))