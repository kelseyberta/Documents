print('Welcome to the shopping cart program')
print('Please select one of the following:')

items = []

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

option = input('Please enter an action: ')

if option == 1:
    item = input('What item would you like to add?')
    items.append(item)
    print(f"'{item}' has been added to your cart")
    print('Please select one of the following')
    print (f'{add_item} Add Item')
    print (f'{view_cart} View Cart')
    print (f'{remove_item} Remove Item')
    print (f'{compute_total} Compute Total')
    print (f'{quit} Quit')
    items.append(item)
    #need to figure out how to add prices to the items and store in the list
if option == view_cart:
    print('The contents of your cart are:')
    for item in items:
        print(item)
    print('Please select one of the following')
    print (f'{add_item} Add Item')
    print (f'{view_cart} View Cart')
    print (f'{remove_item} Remove Item')
    print (f'{compute_total} Compute Total')
    print (f'{quit} Quit')

if option == 3:
    print('What item would you like to remove?')
#need to figure out how to remove item from list
    print('Please select one of the following')
    print (f'{add_item} Add Item')
    print (f'{view_cart} View Cart')
    print (f'{remove_item} Remove Item')
    print (f'{compute_total} Compute Total')
    print (f'{quit} Quit')

if option == 4:
    print ('The total of your cart is:')
    #figure out how to add the prices
    print('Please select one of the following')
    print (f'{add_item} Add Item')
    print (f'{view_cart} View Cart')
    print (f'{remove_item} Remove Item')
    print (f'{compute_total} Compute Total')
    print (f'{quit} Quit')

if option == 5:
    print('goodbye.')


