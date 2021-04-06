'''price of house is $1M. If buyer has good credit,they need to put down 10% otherwise they need to put down
20%. Print the down payment.'''
price=1000000
credit_type=input('Enter the credit type:')
if credit_type=="good credit":
    down_payment=(10/100)*price
elif credit_type=="bad credit":
    down_payment=(20/100)*price
else:
    print("the correct credit type.")
print(f'the down payment is {down_payment}%')