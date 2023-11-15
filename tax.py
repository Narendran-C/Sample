income = 34000
print("Given income:", income)

if income <= 12570:
    tax_payable = 0
elif 12570 < income < 50000:
    tax_payable = (income - 12570) * 20 / 100
else:
    tax_payable = 37430 * 20 / 100 + (income - 50000) * 40 / 100

print("Total tax to pay is", tax_payable)
print((income-tax_payable) / 12 - 180)
