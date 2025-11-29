
def salary(income):
    rate='39%'
    if income>=0 and income<=15600:
        rate='10.5%'
    elif income>= 15601 and income<=53500:
        rate ='17.5%'
    elif income>= 53501 and income<=78100:
        rate= '30%'
    elif  income>= 78101 and income<=180000:
        rate= '33%'
    else :
        rate= '39%'
    return rate
    
if __name__ == "__main__":
    while(True):
        try:
            income = int(input("Enter a positive number: "))
            print(salary(income))
            if(income>90000000):
                break
        except ValueError:
            print("Please input a number again")
       
       

