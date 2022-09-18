import csv

from datetime import datetime

current_date_and_time = datetime.now()

print(f'Inkom Emporium')

print(f"{current_date_and_time:%A %I:%M %p}")

PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

def main():
    PRODUCT_NUM_INDEX = 0
    QUANTITY_INDEX = 1
    products_dict = read_dict("products.csv",PRODUCT_NUM_INDEX)
    print(f'All Products')
    print(products_dict)
    
    
    with open("request.csv", "rt") as request_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(request_file)

        # The first row of the CSV file contains column
        # headings and not data about a dental office,
        # so this statement skips the first row of the
        # CSV file.
        next(reader)
        for row_list in reader:
            product_num = row_list[PRODUCT_NUM_INDEX]   
            request_quantity = row_list[QUANTITY_INDEX]  
            
                       
            print(f'{product_num},{request_quantity},')     

          
    
    
    

def read_dict(filename, key_column_index):
    
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            key = row_list[key_column_index]

            dictionary[key] = row_list
    return dictionary        

if __name__ == "__main__":
    main()    