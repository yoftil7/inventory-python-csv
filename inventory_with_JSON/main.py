import utils

print("please choose an action to proceed!")
print("- Create or c")
print("- Add or a")
print("- Read or r")
print("- Delete or d")
print("- Search or s")
print("- update or u")

def main():
    action = input("-:").strip().lower()

    if action == "create" or action == "c":
        file_path = input("Json file name: ")
        utils.create(file_path)
        print(f"{file_path}.json created successfully!")

    elif action == "add" or action == "a":
        file_path = input("json file: ")
        data = input("Enter JSON data: ")
        utils.write(file_path, data)
        print("JSON data has been successfully writen to", file_path)

    elif action == "read" or action == "r":
        file_path = input("JSON file: ")
        utils.read(file_path)

    elif action == "delete" or action == "d":
        file_path = input("Json file name: ")
        key = input("key: ")
        value = input("value: ")
        utils.delete(file_path, key, value)
    
    elif action == "update" or action == "u":
        file_path = input("JSON file name: ")
        key = input("Key: ").strip()
        old_val = input("Existing value: ").strip()
        new_val = input("New_value: ")
        utils.update(file_path, key, old_val, new_val)
    
    elif action == "search" or action == "s":
        file_path = input("JSON file name: ")
        search_key = input("search key: ")
        search_value = input("query: ")
        utils.search(file_path, search_key, search_value)
    else:
        print("please chooses a valid action to continue")




if __name__ == "__main__":
    main()
