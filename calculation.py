#Ask the user to choose for the policy type and return the policy type
def policyType():

#Ask until the user enter a valid option
    while True:
        no=int(input("""

You can choose between 3 types of policies:

    1.Car insurance
    2.Home insurance 
    3.Mobile phone insurance

Please enter the corresponding number :
"""))
        if no < 1 or no > 3:
         print("Error. Please enter valid option: \n")
        else:
            return no



def insurancePrice(pTypeInsurance,pDuration):
    #Returns how much will the insurance cost the user
    #pTypeInsurance : policy type
    #pDuration : duration

    #if the insurance is a car insurance
    if pTypeInsurance==1:
        pInsurancePrice=pDuration*500

#if the insurance is a home insurance  
    elif pTypeInsurance==2:
        pInsurancePrice=pDuration*1000

#if the insurance is a Mobile Phone insurance
    elif pTypeInsurance==3:
        pInsurancePrice=pDuration*120
    
    return pInsurancePrice


def paymentType(netTotal):
#Ask user to choose the payment type and return the net total
#netTotal : Price of the insurance before transaction fee
#fees : transaction fee
    while True:
        pay=int(input("""\nYou can choose between 3 types of payment type:
 
    1.Bank transfer
    2.PayPal
    3.Credit card

Please choose your payment method: \n"""))
        if pay < 1 or pay > 3:
             print("Error. Please enter valid option: ")
        else:
             print()
             break
    
        netTotal =0.0
#if the payment type is Bank transfer
    if pay == 1:
        netTotal = 0
        return netTotal
#if the payment type is Paypal
    elif pay == 2:
        netTotal = netTotal*0.1
        return netTotal
    elif pay == 3:
#if the payment type is Credit card
        netTotal = netTotal*0.2

    return netTotal
