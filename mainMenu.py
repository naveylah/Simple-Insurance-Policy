import calculation
import userList

print('\n______________________________________________________ \n')
print("         WELCOME TO ALASKA INSURANCE COMPANY  \n")

userName=input("\nPlease enter your name: ")
#ask the user for their name

duration = float(input("\nPlease enter the duration of the insurrance policy (in years):\n "))
#ask the user for the duration of the insurance policy (in years)

policyType = calculation.policyType()
# ask the user for the type of policy

insurancePrice= calculation.insurancePrice(policyType, duration) 
#calculate the insurance price according to the policy type and its duration

paymentType = calculation.paymentType(insurancePrice)
#ask the user for the type of payment
#calculate transaction fees according to the type of payment and the price of the insurance 

totalPrice = insurancePrice + paymentType
#calculate the total price additioning the insurance price and the transaction fee


print('\n______________________________________________________ \n')
# print receipt


print("     Username:   ", userName)
print()
print('     Duration (in years) :   ', duration)
if policyType == 1:
    print("     Policy type :   Car Insurance")
elif policyType ==2:
    print("     Policy type :   Home Insurance")
elif policyType == 3:
    print("     Policy type :   Mobile phone Insurance")

if paymentType == 1:
    print("     Payment type :   Bank Transfer")
elif paymentType ==2:
    print("     Payment type :   Paypal")
elif paymentType == 3:
    print("     Payment type :   Credit Card")

print("     The price of the insurance is : €", totalPrice)
print('\n______________________________________________________ ')


print('\nDo you want to try our new insurance premium calculator?')
# premium insurance calculator


answer=input('Yes or No: \n')

if answer=='Yes' or answer=='yes':
    userList.premiumInsurance()
else:
    print('Too bad, you are missing out buddy!')