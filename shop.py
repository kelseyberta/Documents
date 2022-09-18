


print('Welcome to the shopping cart program')
print('Please select one of the following:')

items = {}
total = 0

add_item = 1
view_cart = 2
remove_item = 3
compute_total= 4
quit = 5
print (f'{add_item} Add Item')
print (f'{view_cart} View Cart')
print (f'{remove_item} Remove Item')
print (f'{compute_total} Compute Total')
print (f'{quit} Quit')

option = int(input('Please enter an action: '))

while option != 5:
    
    if option ==1:
        item = input('What item would you like to add?')
        price = float(input("Price?"))
        print(f"'{item}' at ${price:.2f} has been added to your cart")
        items[item] = price
        price += total
        
        
    if option == 2:
        x = 0 
        for item in items:
            x += 1
            print(f'The contents of your cart are: {x}). {item} - ${price:.2f}')

    if option == 3:
        remove = input('What item would you like to remove?')
        del items[remove]
        print(f'{remove} has been removed from the list')



    if option == 4:
        total = 0
        for item in items:
            total +=items[item]
       
        print (float(f'The total of your cart is: ${total:.2f}'))
    
if option == 5:
    print('thank you for shopping')