import utils

print("Choose an action to continue")
print("create or c")
print("Add or a")
print("Read or r")
print("Delete or d")
print("search or s")
print("Update or u")
print("exit or e")

def main():
    file_path = input("Enter the file path: ").strip()
    
    while True:
        action = input("\nAction: ").strip().lower()
        
        if action == "create" or action == "c":
            utils.create(file_path)

        elif action == "add" or action == "a":
            new_record_str = input("New record: ")
            utils.write(file_path, new_record_str)

        elif action == "read" or action == "r":
            utils.read(file_path)

        elif action == "delete" or action == "d":
            delete_id = int(input("ID number: "))
            utils.delete(file_path, delete_id)

        elif action == "search" or action == "s":
            utils.search(file_path)

        elif action == "update" or action == "u":
            id_num = int(input("ID number: "))
            key = input("Key: ")
            new_value = None
         #   if key == "address":
          #      new_value = input("New value: ")
            utils.update(file_path, id_num, key, new_value)
        elif action == "exit" or action == "e":
            break

        else:
            print("Invalid action! please choose a valid action.")

        exit_choice = input("Do you want to continue or exit?  \n(Type any key to continue or 'exit' to exit.)\n").strip().lower()
        if exit_choice == "exit":
            break

if __name__ == "__main__":
    main()

