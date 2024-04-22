import json
import os


def create(file_path):
    try:
        if not os.path.exists(file_path):
            with open(file_path, "w") as json_file:
                json.dump([{}], json_file, indent=4)
                print(f"JSON file '{file_path}' created successfully")
        else:
            print(f"{file_path} alraedy exists!")
    except (IOError, OSError, PermissionError, FileExistsError) as e:
        print(f"An error occurred while creating the file: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data: {e}")


def write(file_path, data):
    try:
        if not os.path.exists(file_path):
            print("no such file", file_path)
            return
        with open(file_path, "r+") as json_file:
            json_new_data = json.loads(data)
            json_data = json.load(json_file)
            json_data.append(json_new_data)
            json_file.seek(0)
            json.dump(json_data, json_file, indent=4)
            json_file.truncate()
            print("JSON data write successfull!")
    except ValueError as e:
        print("Invalid JSON format. Please try again.")
    except Exception as e:
        print("An error occurred:", e)


def read(file_path):
    try:
        if not os.path.exists(file_path):
            print("Such file dont exist!")
            return

        with open(file_path, "r") as json_file:
            content = json.load(json_file)
            print(f"JSON file: '{file_path}'\nContent:")
            print(content)
    except Exception as e:
        print("An error occured: ", e)


def delete(file_path, key, value):
    try:
        if not os.path.exists(file_path):
            print("no such file", file_path)
            return
        filtered_data = []
        item_deleted = False
        with open(file_path, "r+") as json_file:
            data = json.load(json_file)
            for item in data:
                if not item_deleted and item.get(key) == value:
                    item_deleted = True
                    continue
                filtered_data.append(item)
                    

        with open(file_path, "w") as json_file:
            json.dump(filtered_data, json_file, indent=4)
            print(f"'{key}':'{value}' is deleted successfully!")
    except ValueError as e:
        print("Invalid json format")
    except Exception as e:
        print("Error: ", e)


def update(file_path, key, old_val, new_val):
    try:
        if not os.path.exists(file_path):
            print("No such file!", file_path)
            return

        with open(file_path, "r+") as json_file:
            data = json.load(json_file)
            for item in data:
                if item.get(key) == old_val:
                    item[key] = new_val
                    break
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            print(f"{key} is updated to {new_val}!")
    except ValueError as e:
        print("Invalid JSON format!")
    except Exception as e:
        print("Error: ", e)

 
 
def search(file_path, search_key, search_value):
    try:
        if not os.path.exists(file_path):
            print("No such JSON file!")
            return
        search_results = []
        op = None
        if search_key == "age":
            op = input("Operator:\ngt = '>'\nlt = '<'\neq = '=='\nnq = '!=    '\ngt_eq = '>='\nlt_eq = '<='\n- ").lower()
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            for item in data:
                if search_key in ["first_name", "last_name", "city"] and item.get(search_key) == search_value:
                    search_results.append(item.get(search_key))
                elif search_key == "age":
                    if op == "gt" and item.get(search_key) > int(search_value):
                        full_name = item.get("first_name", "") + " " + item.get("last_name", "") 
                        search_results.append(full_name)
                    elif op == "lt" and item.get(search_key) < int(search_value):
                        full_name = item.get("first_name", "") + " " + item.get("last_name", "") 
                        search_results.append(full_name)
                    elif op == "eq" and item.get(search_key) == int(search_value):
                        full_name = item.get("first_name", "") + " " + item.get("last_name", "") 
                        search_results.append(full_name)
                    elif op == "neq" and item.get(search_key) != int(search_value):
                        full_name = item.get("first_name", "") + " " + item.get("last_name", "") 
                        search_results.append(full_name)
                    elif op == "gt_eq" and item.get(search_key) >= int(search_value):
                        full_name = item.get("first_name", "") + " " + item.get("last_name", "") 
                        search_results.append(full_name)
                    elif op == "lt_eq" and item.get(search_key) <= int(search_value):
                        full_name = item.get("first_name", "") + " " + item.get("last_name", "") 
                        search_results.append(full_name)
                else:
                    continue

        if not search_results:
            print("No matching records found.")
        else:
            print("Search results:")
            print(search_results)

    except ValueError as e:
        print("Invalid input:", e)
    except Exception as e:
        print("Error:", e)







