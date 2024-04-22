import utils

print(f"create new csv file,\n"
      f"Add new Item\n"
      f"Display contents\n"
      f"Update Item\n"
      f"Delete Item\n"
      f"Search Item\n")

def main():
    try:    
        action = input("choose an option please\n").strip().lower()
   
    #create the csv file
        if action == "create": 
            file_path = input("CSV file name: ")
            file_path = file_path + ".csv"
            utils.create_csv(file_path)
    
        elif action == "add":
            file_path = input("csv file_name: ").strip()
            item = input("Item name: ")
            quantity = input("quantity of item: ")
            price = float(input("whats the price: "))
            utils.add_item(file_path, item, quantity, price)
    
        elif action == "display":
            file_path = input("file name: ")
            utils.read_items(file_path)

        elif action == "delete":
            file = input("file name: ")
            record = input("Row number to be removed: ")
            utils.delete_row(file, record)

        elif action == "search":
            file_path = input("what is the csv file? ")
            column = input("What field or column do you want to search? ").lower()
            op = input("Operator:\ngt = '>'\nlt = '<'\neq = '=='\nnq = '!='\ngt_eq = '>='\nlt_eq = '<='\n- ").lower()
            query = input("Query: ")
            utils.search_item(file_path, column, op, query)

        elif action == "update":
            file_path = input("csv file: ")
            utils.update(file_path) 

        else:
            print("invalid command, please choose from the options above")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
