#formatted_number=format(number,".2f")#

#makes sure to define floats so it can multiply it, this is the fix to the error on line 7#
purchaseAmount = float(input("what is the Purchase Amount:"))
SalesTax=float(input("what is the sales Tax rate (as a decimal):"))

#total=purchaseAmount*SalesTax TypeError: can't multiply sequence by non-int of type 'str'#
total=purchaseAmount*SalesTax/100

total=format(float(total),".2f")


print("Sales Tax is:",total)