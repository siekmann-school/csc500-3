sales_tax = .08
tip = .18
subtotal = float(input('Please enter the charge for the food: '))
subtotal = round(subtotal, 2)
tax_amount = round(subtotal * sales_tax, 2)
total_minus_tip = round(subtotal + tax_amount, 2)
tip_amount = round(total_minus_tip * tip, 2)
total = round(total_minus_tip + tip_amount, 2)
print('Subtotal: $' + str(subtotal))
print('Tax: $' + str(tax_amount))
print('Tip: $' + str(tip_amount))
print('Total: $' + str(total))