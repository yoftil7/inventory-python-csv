### Code structure

Please use the example shown below to structure any code you write

```
import sys
from optparse import OptionParser

def calculate_bmi(w, h):
    bmi = w/(h*h)
    bmi = round(bmi, 2)
    return bmi 


def main():

    usage = "\n%prog  [options]"
    parser = OptionParser(usage,version="%prog version___")
    parser.add_option("-k","--weight",action="store",dest="weight",help="weight in Kilograms")
    parser.add_option("-m","--height",action="store",dest="height",help="height in meters ") 
    (options,args) = parser.parse_args()
    for key in ([options.weight, options.height]):
        if not (key):
            parser.print_help()
            sys.exit(0)

    try:
        w = float(options.weight)
        h = float(options.height) 
        bmi = calculate_bmi(w, h)
        print ("Your BMI is %s" % (bmi))
    except Exception as err:
        print (err)

if __name__ == '__main__':
    main()
```

### Inventory project
Write a code following the example given above that will have the following actions
- "create" to create a new CSV file named "inventory.csv" that will contain inventory information with the following fields/headers:row_number,name,description,quantity,price 
- "insert" to insert a row/record into "inventory.csv"
- "update" to update a row/record in "inventory.csv"
- "delete" to delete or remove a row/record from "inventory.csv"
- "search" to find rows/records in "inventory.csv"
  
### Some example code to read and write into a file
The following example function writes into a file

```
import json

def write_csv(out_file, row_list):
    with open(out_file, "w") as FW: 
        for row in row_list:
            FW.write("\"%s\"\n" % ("\",\"".join(row)))
    return

def read_csv(out_file):
    row_list = []
    with open(out_file, "r") as FR: 
        for line in FR:
            row = line.split("\",\"")
            row_list.append(row)
    return row_list

def main():
    out_file = "example/myfile.csv"
    row_list = [
        ["first_name", "last_name", "height"],
        ["James", "Bond", "180"],
        ["John", "Doe", "170"]
    ]
    write_csv(out_file, row_list)

    row_list = read_csv(out_file)
    print (json.dumps(row_list, indent=4))

    return

if __name__ == '__main__':
    main()

```



