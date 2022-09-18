def main():
    end_program = 'no'
    integer_choice = 0
    total_budget = 1000
    while end_program == 'no':
        print ('Welcome to the Budget Program')
        print ('Menu Selections: ')
        print ('1-Add an Expense: ')
        print ('2-Remove an Expense: ')
        print ('3-Add Revenue: ')
        print ('4-Remove Revenue: ')
        print ('5-Check Your Budget Balance: ')
        print ('6-Exit' )
        user_input = input('enter your selection: ')
        if user_input != "":
            choice=int(user_input)
        if choice == 1:
            expense = int(input ('Enter your expense amount: $'))
            monthly = int(input ('How many times per month: '))
            total_budget = add_expense(total_budget)
        elif choice == 2:
            expense = int(input ('Enter expense amount you want to remove: $'))
            monthly = int(input ('How many times per month: '))
            total_budget = remove_expense(total_budget)
        elif choice == 3:
            revenue = int(input ('Enter new monthly income: $'))
            total_budget = add_revenue(total_budget)
        elif choice == 4:
            revenue = int(input ('Enter monthly income amount to be removed: $'))
            total_budget = remove_revenue(total_budget)
        elif choice == 5:
            print (f'Your balance is',{total_budget})
        elif choice == 6:
            end_program = 'yes'
            print ('Goodbye')
        elif choice > 6:
            print ('Invalid selection, please try again')
        else:
            print ('Invalid selection, please try again')


def add_expense(total_budget, expense, monthly):
    total_expense = expense * monthly
    if total_expense >= total_budget:
        print ('You have exceeded your budget amount.'),total_budget
    else:
        total_budget= total_budget - total_expense
        print (f'Your remaining budget is: ${total_budget}')
        choice=int(input('enter your selection: '))
    return total_budget



def remove_expense (total_budget, expense, monthly):
   
    total_expense = expense * monthly

    total_budget=total_expense+total_budget
    print(f'your remaining budget is: ${total_budget}' )
    return total_budget

def add_revenue (total_budget,revenue):
    total_budget = total_budget+revenue
    print (f'your new budget is: ${total_budget}') 
    return total_budget 

def remove_revenue (total_budget,revenue):
    total_budget = total_budget - revenue
    if revenue >=total_budget:
        print (f'You owe :${total_budget}')
    else:
        print (f'Your new budget is: ${total_budget}') 
    return total_budget

if __name__ == "__main__":
    main()  

