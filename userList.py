
def isfloat(num): #Verify if the input is a float or a number
    try:
        float(num)
        return True
    except ValueError:
        return False

def premiumInsurance(): #Calculate the premium insurance part
    while True:
        premiumList = []

        print('\n______________________________________________________ ')
        print()
        print('          INSURANCE PREMIUM CALCULATOR \n ')
        maxLengthList = float(input('   How many Insurance Policy shall we calculate: '))

        while len(premiumList) < maxLengthList:
            item = input("\n    Enter the premium insurrance: ")
            if not isfloat(item):
                print("     You can only enter a number. Try again.")
                premiumList=['0']
                break
            else:
                item=float(item)
                premiumList.append(item)

        if premiumList == ['0']:
            continue
        
        print()
        print('\n_________________________________________________________ \n')
        print('     Your Premium Insurance are : ', premiumList,'\n')
        print('     The sum of Premium Insurance is : €', sum(premiumList),'\n')
        print('     The greatest value is : €', max(premiumList),'\n')
        print('     The average Premium Insurance is : €', round(sum(premiumList)/len(premiumList),2),'\n')
        print('_________________________________________________________ \n')
        exit()


