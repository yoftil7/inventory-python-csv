import json
import os


#create json file
def create(file_path):
    try:
        if os.path.exists(file_path):
            print(f"file '{file_path}' already exists")
        else:
            with open(file_path, "w") as json_file:
                json.dump([], json_file, indent=4)
                print(f"'{file_path}' have been successfully created")
    except Exception as e:
        print("error: ", e)


#write json content
def write(file_path, new_record_str):
    try:
        if not os.path.exists(file_path):
            print(f"json file '{file_path}' does not exist.")
            return
        
        with open(file_path, "r+") as json_file:
            record = json.load(json_file)
            new_record = json.loads(new_record_str)
            record.append(new_record)
            json_file.seek(0)
            json.dump(record, json_file, indent=4)
            json_file.truncate()
            print("success!")
    except ValueError as e:
        print("invalid input")
    except Exception as e:
        print("error: ", e)


#read json file
def read(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"No such file: {file_path}")
            return
        with open(file_path, "r") as json_file:
            records = json.load(json_file)
        
        print("file content")
        if not records == []:
            for record in records:
                print(json.dumps(record, indent=4))
        else:
            print(f"JSON file '{file_path}' is empty!")

    except Exception as e:
        print("Error: ", e)


# search records from json file
def search(file_path):
    try:
        key = input("Key: ").strip().lower()
        if key == "address":
            sub_key = input("country or city or street: ").strip().lower()
        with open(file_path, "r") as jf:
            record_list = json.load(jf)
        
            query = input("query: ").strip()
            search_results = []
            for row in record_list:
                if key == "address":
                    if sub_key not in row["address"]:
                        print("chose valid address please")
                    elif query.lower() == row["address"][sub_key]:
                        search_results.append(row)
                elif key == "first_name" and row["first_name"] == query.lower():
                    search_results.append(row)
                elif key == "last_name" and row["last_name"] == query.lower():
                    search_results.append(row)
                elif key == "age" and int(row["age"]) == int(query):
                    search_results.append(row)
                elif key == "country" and row["address"]["country"] == query.lower():
                    search_results.append(row)
                elif key == "city" and row["address"]["city"] == query.lower():
                    search_results.append(row)
                elif key == "street" and row["address"]["street"] == query.lower():
                    search_results.append(row)

            if not search_results:
                print(f"Record '{query}' dose not exist")
            else:
                for result in search_results:
                    print(result)

            return search_results       

    except ValueError as e:
        print("invalid search input", e)
    except Exception as e:
        print("Error: ", e)



#delete record from json
def delete(file_path, delete_id):
    try:
        if not os.path.exists(file_path):
            print(f"json file '{file_path}' does not exist")
            return
        found = False
        results = []
        removed_record = []
        with open(file_path, "r+") as json_file:
            record_list = json.load(json_file)
            
            for record in record_list:
                if int(record["id_number"]) != delete_id:
                    found = True
                    results.append(record)
                else:
                    removed_record.append(record)

            json_file.seek(0)
            json.dump(results, json_file, indent=4)
            json_file.truncate()
        if found:
            print(f"Record:  {removed_record}")
            print("Deleted successfully!")
        else:
            print(f"No record with ID Number: '{delete_id}'")

    except ValueError as e:
        print("Invalid input", e)
    except Exception as e:
        print("Error: ", e)


#update records
def update(file_path, id_num, key, new_value):
    try:
        if not os.path.exists(file_path):
            print(f"No such file, '{file_path}'!")
            return
        
        updated_records = []
        
        with open(file_path, "r+") as json_file:
            record_list = json.load(json_file)
            
            for record in record_list:
                if key not in record and key not in record["address"]:
                    print(f"The key '{key}' does not exist in the JSON file.")
                    return
                
                if "id_number" not in record:
                    print(f"NO key 'ID number: {id_num}'!")
                    return
                
                if int(record["id_number"]) == id_num:
                    print("Record: \n", record)
                    print("")
                    if key == "address":
                        sub_key = input("which address do you want to update? \n(country, city, street): ").strip().lower()
                        if sub_key not in record[key]:
                            print("Invalid sub-key for address.")
                            return
                        new_value = input("new value: ")
                        record[key][sub_key] = new_value
                    elif key in record["address"]:
                        new_value = input("new value: ")
                        record["address"][key] = new_value
                    else:
                        new_value = input("new value: ")
                        record[key] = new_value
                
                updated_records.append(record)
            
            json_file.seek(0)
            json.dump(updated_records, json_file, indent=4)
            json_file.truncate()
            
            print(f"{key} is updated to '{new_value}'.")
    
    except ValueError as e:
        print("Invalid input: ", e)
    except Exception as e:
        print("Error: ", e)






