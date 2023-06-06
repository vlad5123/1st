'''
try:
    your_code
expect type_of_the_error:
    your_code
'''
while(True):
    try:
        digit1=input("Enter digit1: ")
        digit2=input("Enter digit2: ")
        print(digit1/digit2)
    except Exception as ex:
        yes = input(f"{ex}\n"
                    f"You have to enter digit2 not equal 0!\n"
                    f"Do you want try to continue? Y/N:")
        if(yes.lower() == "n"):
            break




class BuildingError(Exception):
def __init__(self, amount = 0, limit = 0 ):
self.Amount = amount
self.Limit = limit
def __str__(self):
return f"Amount: {self.Amount} is greater than limit: {self.Limit}" 