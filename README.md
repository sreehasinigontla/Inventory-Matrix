# Inventory-Matrix
# 📦 Inventory Matrix Reconciliation System

## 📌 Project Overview

The **Inventory Matrix Reconciliation System** is a Python-based application designed to compare product quantities across multiple warehouses using nested lists (two-dimensional matrices).

The system identifies stock shortages and surpluses, calculates the required stock transfers between warehouses, and updates inventory quantities to meet specified stock targets.

It helps maintain balanced inventory levels and improves warehouse stock management.

## 🎯 Objectives

- Store product quantities across multiple warehouses.
- Represent inventory using nested lists.
- Compare current stock with target stock.
- Identify warehouse-wise stock shortages.
- Identify warehouse-wise stock surpluses.
- Calculate required stock transfers.
- Update inventory after transfers.
- Identify remaining shortages and surpluses.
- Generate a final inventory reconciliation report.

## 🏢 Warehouse Details

The system supports multiple warehouses, such as:

1. Warehouse A
2. Warehouse B
3. Warehouse C

Users can enter any number of warehouses and products.

## 📊 Sample Inventory Matrix

### Current Stock

| Product | Warehouse A | Warehouse B | Warehouse C |
|---|---:|---:|---:|
| Laptops | 50 | 20 | 10 |
| Mobiles | 30 | 60 | 20 |
| Keyboards | 80 | 15 | 25 |

### Target Stock

| Product | Warehouse A | Warehouse B | Warehouse C |
|---|---:|---:|---:|
| Laptops | 30 | 30 | 20 |
| Mobiles | 40 | 40 | 30 |
| Keyboards | 40 | 40 | 40 |

## 🚀 Features

1. Multiple warehouse registration.
2. Multiple product registration.
3. Current stock quantity entry.
4. Target stock quantity entry.
5. Nested list inventory representation.
6. Stock shortage identification.
7. Stock surplus identification.
8. Automatic stock transfer calculation.
9. Updated inventory matrix generation.
10. Remaining shortage and surplus detection.
11. Final reconciliation report.

## 🧮 Calculation Methods

### 1. Stock Difference

```text
Stock Difference = Current Stock - Target Stock
```

### 2. Stock Shortage

```text
If Current Stock < Target Stock:

Shortage = Target Stock - Current Stock
```

### 3. Stock Surplus

```text
If Current Stock > Target Stock:

Surplus = Current Stock - Target Stock
```

### 4. Stock Transfer

```text
Transfer Quantity =
Minimum of Available Surplus and Required Shortage
```

### 5. Updated Inventory

```text
Updated Stock =
Current Stock - Transferred Stock
              + Received Stock
```

## 🔄 Transfer Process

The system follows these steps:

1. Read current inventory quantities.
2. Read target stock quantities.
3. Compare current stock with target stock.
4. Identify warehouses with surplus stock.
5. Identify warehouses with shortage stock.
6. Transfer surplus stock to warehouses with shortages.
7. Update the inventory matrix.
8. Check whether all target quantities are achieved.

Stock transfers are calculated separately for each product.

## 💻 Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

## 🐍 Python Concepts Used

- Variables and Data Types
- Lists
- Nested Lists
- Two-Dimensional Matrices
- Dictionaries
- Conditional Statements
- For Loops
- While Loops
- Functions
- Arithmetic Operators
- Built-in Functions
- List Indexing

## 📁 Project Structure

```text
Inventory-Matrix-Reconciliation/
│
├── inventory_reconciliation.py
├── README.md
├── problem_statement.txt
├── objectives.txt
├── assumptions.txt
├── algorithm.txt
├── pseudocode.txt
├── flowchart.png
├── test_cases.txt
│
└── output_screenshots/
    ├── output1.png
    ├── output2.png
    └── output3.png
```

## ▶️ How to Run the Project

**Step 1:** Install Python 3 on your computer.

**Step 2:** Download or clone the GitHub repository.

**Step 3:** Open the project folder in Visual Studio Code.

**Step 4:** Open the terminal.

**Step 5:** Execute the following command:

```bash
python inventory_reconciliation.py
```

**Step 6:** Enter the number of warehouses.

**Step 7:** Enter warehouse names and product names.

**Step 8:** Enter the current stock quantities for each product.

**Step 9:** Enter the target stock quantities.

**Step 10:** View the shortage report, surplus report, transfer plan, and updated inventory matrix.

## 🧪 Test Cases

| Test Case | Input / Condition | Expected Result |
|---|---|---|
| TC01 | Current stock equals target stock | No transfer required |
| TC02 | Warehouse A has surplus and B has shortage | Transfer calculated |
| TC03 | Multiple warehouses have surplus | Stock distributed to shortage warehouses |
| TC04 | Total stock is equal to total target | All targets achieved |
| TC05 | Total stock is less than total target | Remaining shortage reported |
| TC06 | Total stock is greater than total target | Remaining surplus reported |
| TC07 | Zero current stock | Shortage identified |
| TC08 | Multiple products | Each product reconciled separately |

## 📊 Expected Output

The program displays:

- Current inventory matrix.
- Target inventory matrix.
- Product-wise stock shortages.
- Warehouse-wise stock surpluses.
- Required stock transfer details.
- Source warehouse.
- Destination warehouse.
- Transfer quantity.
- Updated inventory matrix.
- Remaining shortages and surpluses.
- Final reconciliation status.

## ⚠️ Assumptions

- All stock quantities are non-negative integers.
- Every product is tracked separately.
- Stock can be transferred between warehouses.
- Transfers do not incur transportation costs.
- Each warehouse has a predefined target quantity for every product.
- Transfers cannot exceed available surplus quantities.
- If total stock is insufficient, remaining shortages are reported.
- If total stock exceeds target requirements, remaining surpluses are reported.

## 📝 Conclusion

The Inventory Matrix Reconciliation System provides a simple and effective way to manage stock quantities across multiple warehouses using Python.

It uses nested lists to store inventory information, compares current stock with target stock, identifies shortages and surpluses, and calculates the required stock transfers.

This project demonstrates the practical application of Python nested lists, loops, conditional statements, functions, and matrix operations in real-world inventory management.

---

**Project Name:** Inventory Matrix Reconciliation System

**Subject:** Python Activity-Based Learning
name:sree hasini
section:5 
**Programming Language:** Python 3

**Project Type:** Case Study
