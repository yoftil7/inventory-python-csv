#utills.py
import os

#create csv file
def create_csv(file_path):
    header_row = ["Item", "Quantity", "Price"]
    try:
        if not os.path.exists(file_path):
            with open(file_path, "w") as csvfile:
                csvfile.write("Row , " + " , ".join(header_row) + "\n")
            print(f"CSV file '{file_path}' created successfully!")
        else:
            print(f"CSV file '{file_path}' already exists.")

    except Exception as e:
        print(f"Error creating CSV file: {e}")



#Add item to csv file
def add_item(file_path, item, quantity, price):
    try:
        if not os.path.exists(file_path):
            print("Csv file does not exist! please create it first.")
            return
       
        row_num = 0
        with open(file_path, "r") as csvfile:
            lines = csvfile.readlines()
            if len(lines) == 1:
                row_num = 1
            elif lines:
                last_row = lines[-1].split(',')[0]
                row_num = int(last_row) + 1
            else:
                exit(-1)

            
        with open(file_path, "a") as csvfile:
            csvfile.write(f"{row_num},{item},{quantity},{price}\n")
        print("Item added successfully!")
    except Exception as e:
        print(f"Error adding item to inventory: {e}")


#Read csv file
def read_items(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"No such '{file_path}' file.")
        else:
            with open(file_path, "r") as csvfile:
               file_content =  csvfile.read()
            print(f"contents of '{file_path}'.")
            print(file_content)

    except Exception as e:
        print(f"Error displaying contents from file: {e}")



#Delete items from csv file      
def delete_row(file, record):
    try:
        with open(file, "r") as f:
            lines = f.readlines()

        with open(file, "w") as f:
            f.write(lines[0])  # Write the header back
            for line in lines[1:]:
                row_num, rest = line.strip().split(',', 1)
                if row_num != record:
                    f.write(f"{row_num},{rest}\n")
                else:
                    print(f"Row {record} successfully deleted.")
    
        # Adjust row numbers below the deleted row
        with open(file, "r") as f:
            lines = f.readlines()
    
        with open(file, "w") as f:
            f.write(lines[0])  # Write the header back
            for line in lines[1:]:
                row_num, rest = line.strip().split(',', 1)
                if int(row_num) > int(record):
                    new_row_num = str(int(row_num) - 1)
                    f.write(f"{new_row_num},{rest}\n")
                else:
                    f.write(f"{row_num},{rest}\n")

    except Exception as e:
        print(f"Error deleting row: {e}")


#Search items from csv file
def search_item(file_path, column, op, query):
    try:
        search_results = []

        with open(file_path, 'r') as f:
            header = next(f)
            for line in f.readlines():
                row = line.strip().split(',')

                row_item = row[1]
                row_quantity = int(row[2])
                row_price = float(row[3])

                if column == 'item':
                    if row_item.lower() == query.lower():
                        search_results.append(row)
                elif column == 'quantity':
                    if op == 'gt' and row_quantity > int(query):
                        search_results.append(row)
                    elif op == 'lt' and row_quantity < int(query):
                        search_results.append(row)
                    elif op == 'nq' and row_quantity != int(query):
                        search_results.append(row)
                    elif op == 'eq' and row_quantity == int(query):
                        search_results.append(row)
                    elif op == 'lt_eq' and row_quantity <= int(query):
                        search_results.append(row)
                    elif op == 'gt_eq' and row_quantity >= int(query):
                        search_results.append(row)
                elif column == 'price':
                    if op == 'gt' and row_price > float(query):
                        search_results.append(row)
                    elif op == 'lt' and row_price < float(query):
                        search_results.append(row)
                    elif op == 'nq' and row_price != float(query):
                        search_results.append(row)
                    elif op == 'eq' and row_price == float(query):
                        search_results.append(row)
                    elif op == 'lt_eq' and row_price <= float(query):
                        search_results.append(row)
                    elif op == 'gt_eq' and row_price >= float(query):
                        search_results.append(row)
                else:
                    print("Invalid column name")

        if not search_results:
            print("Not found!")
        else:
            print("Search results:")
            for result in search_results:
                print(result)

    except Exception as e:
        print(f"An error occurred: {e}")



#update items in csv file
def update(file_path):
    try:
        if not os.path.exists(file_path):
            print("No such CSV file")
            return

        lines = []
        found = False

        with open(file_path, "r") as f:
            header = f.readline().strip().split(",")
            lines.append(header)
            for line in f:
                row = line.strip().split(",")
                lines.append(row)

        row_number = int(input("Enter row number to update: "))
        column_name = input("Enter column name to update: ").strip()

        if 0 <= row_number < len(lines):
            column_name_lower = column_name.lower()
            header_lower = [col.lower() for col in header]
            if column_name_lower in header_lower:
                column_index = header_lower.index(column_name_lower)
                new_entry = input("Enter new entry: ")
                lines[row_number][column_index] = new_entry
                found = True
                print("Entry updated successfully")
            else:
                print("Column name not found")
        else:
            print("Invalid row number")

        if found:
            with open(file_path, "w") as f:
                for line in lines:
                    f.write(",".join(line) + "\n")

    except ValueError as e:
        print("Invalid input:", e)
    except Exception as e:
        print(f"Error: {e}")





