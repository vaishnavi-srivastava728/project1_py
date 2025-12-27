# Expense Tracker Project

l=[] # List of dictionaries for all expenses
print("Welcome to ExpenseUp!!")

while(True):
    print("======MENU======")
    print("1. Add Expenses")
    print("2. View all expenses")
    print("3. View total expenses")
    print("4. Exit")

    choice= eval(input("Enter your choice:"))

# Add Expenses
    if(choice==1):
        date=input("Enter the date of expense:")
        category=input("Enter the category of expense:")
        description=input("Enter more details")
        amount=float(input("Enter the amount spent:"))

        expense={"date":date,"category":category,"description":description,"amount":amount}
        l.append(expense)
        print("Expenses Added Sucessfully.")

# View all Expenses
    elif(choice==2):
        if(len(l)==0):
            print("Congratulation you have done no expenses yet")
        else:
            print("Following is the list of all your expenses:")
            count=1
            for i in l:
                print("Expense no.",count,"=",i["date"],i["category"],i["description"],i["amount"])
                count=count+1

# View total Expenses
    elif(choice==3):
        sum=0
        for i in l:
            sum = sum + i["amount"]

        print("Total expenses are:",sum)

# Exit
    elif(choice==4):
        print("Thankyou for choosing ExpenseUp:)")
        break

# wrong choice case
    else:
        print("Please enter a valid choice" )
