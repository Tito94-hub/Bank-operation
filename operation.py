
#initialize bank operation

import random

database = {} #dictionary

def init():

    isValidOptionSelected  = False
    print("Welcome to bankPHP")

    While isValidOptionSelected == False:

    haveAccount = int(input("Do you have an account with us: 1(yes) 2(no) \n"))

    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")


    def login():
        print("this is the login function")

    def register():
        print("this is register function")

    def bankOperation():
        print("some operations")

    def generationAccountNumber():

        print("Generating Account Number")
        return random.randrange(1111111111,9999999999)


    #### ACTUAL BANKING SYSTEM #####

    print(generationAccountNumber())
    # init()