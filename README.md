# **Inventory App (CSV, JSON, Complex JSON)**

**Repository**: [inventory-python-csv](https://github.com/yoftil7/inventory-python-csv)  
**Version**: 1.0  
**Developer**: Yoftahie Alem

## **Overview**
This is a learning project that explores three different implementations of an inventory management system using:
- CSV files
- JSON files
- Complex JSON files

The app was developed as part of learning Python file handling, CSV parsing, and working with JSON structures. Each version of the app performs basic inventory management using its respective data format.

## **Key Features**
- **CSV Version**: Basic inventory management (CRUD operations) stored in a CSV file.
- **JSON Version**: Inventory stored and manipulated in JSON format.
- **Complex JSON Version**: A more advanced inventory system using nested JSON structures.
  
Each version is separate and demonstrates how data can be stored, retrieved, and managed using different formats.

## **Tech Stack**
- **Language**: Python
- **Data Storage**: 
  - CSV files
  - JSON files
  - Complex JSON files
  
## **Project Structure**

- **`inventory_with_csv_file/`**: The folder containing the CSV version of the inventory app.
  - **`main.py`**: Core logic of the inventory app using CSV files.
  - **`utils.py`**: Helper functions for handling CSV operations.
  - **`y.csv`**: Sample CSV file used for inventory storage.
  
- **`inventory_with_JSON/`**: The folder containing the JSON version of the inventory app.
  - **`main.py`**: Core logic of the inventory app using JSON files.
  
- **`inventory_with_complex_json_file/`**: The folder containing the complex JSON version of the app.
  - **`main.py`**: Handles inventory data stored in complex nested JSON structures.

- **`project_3/`**: Old or experimental code related to earlier versions of the project.
  
- **`.DS_Store`**: macOS system file (ignore this).
- **`.optpar.py.swp`**: Temporary swap file (ignore this).

## **System Requirements**
- Python 3.x

## **Installation and Setup**

### **Clone the Repository**
```bash
git clone https://github.com/yoftil7/inventory-python-csv.git
cd inventory-python-csv
```

### **Run the CSV Version**
```bash
cd inventory_with_csv_file
python3 main.py
```

### **Run the JSON Version**
```bash
cd inventory_with_JSON
python3 main.py
```

### **Run the Complex JSON Version**
```bash
cd inventory_with_complex_json_file
python3 main.py
```

Each version of the app will prompt for inputs or commands to manage the inventory based on the respective file format.

## **Usage**
### CSV Version:
- Uses a CSV file (`y.csv`) to manage inventory.
- Perform basic CRUD operations directly from the terminal.

### JSON Version:
- Stores inventory data in JSON format.
- You can add, modify, and delete items using this structure.

### Complex JSON Version:
- Similar to the JSON version but allows handling more complex nested data structures, useful for hierarchical or detailed inventories.

## **Future Enhancements**
- Add a front-end interface for easier interaction with the inventory.
- Improve error handling and validation for each version.
- Merge the three versions into a unified, more flexible system.

## **License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.
