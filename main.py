
# Inventory Matrix Reconciliation System

# Function to accept a positive integer
def get_positive_integer(message):

    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Enter a number greater than zero.")

        except ValueError:
            print("Please enter a valid whole number.")


# Function to accept non-negative stock quantity
def get_quantity(message):

    while True:
        try:
            value = int(input(message))

            if value >= 0:
                return value

            print("Stock quantity cannot be negative.")

        except ValueError:
            print("Please enter a valid whole number.")


# Function to calculate shortages and surpluses
def identify_stock(stock, target):

    shortages = []
    surpluses = []

    for i in range(len(stock)):

        shortage_row = []
        surplus_row = []

        for j in range(len(stock[i])):

            difference = stock[i][j] - target[i][j]

            if difference < 0:
                shortage_row.append(abs(difference))
                surplus_row.append(0)

            elif difference > 0:
                surplus_row.append(difference)
                shortage_row.append(0)

            else:
                shortage_row.append(0)
                surplus_row.append(0)

        shortages.append(shortage_row)
        surpluses.append(surplus_row)

    return shortages, surpluses


# Function to calculate required transfers
def calculate_transfers(stock, target, products, warehouses):

    # Create a working copy of the stock matrix
    updated_stock = []

    for row in stock:
        updated_stock.append(row.copy())

    transfers = []

    # Process each product separately
    for i in range(len(products)):

        # Identify warehouses with surplus
        donors = []

        # Identify warehouses with shortage
        receivers = []

        for j in range(len(warehouses)):

            difference = updated_stock[i][j] - target[i][j]

            if difference > 0:
                donors.append([j, difference])

            elif difference < 0:
                receivers.append([j, abs(difference)])

        # Transfer stock from surplus to shortage
        for receiver in receivers:

            receiver_index = receiver[0]

            for donor in donors:

                donor_index = donor[0]

                if receiver[1] == 0:
                    break

                if donor[1] == 0:
                    continue

                # Calculate transferable quantity
                quantity = min(donor[1], receiver[1])

                if quantity > 0:

                    # Update inventory
                    updated_stock[i][donor_index] -= quantity

                    updated_stock[i][receiver_index] += quantity

                    # Update remaining surplus and shortage
                    donor[1] -= quantity
                    receiver[1] -= quantity

                    # Store transfer details
                    transfers.append([
                        products[i],
                        warehouses[donor_index],
                        warehouses[receiver_index],
                        quantity
                    ])

    return updated_stock, transfers


# Function to display matrix
def display_matrix(title, matrix, products, warehouses):

    print("\n==========", title, "==========")

    print("Product".ljust(18), end="")

    for warehouse in warehouses:
        print(warehouse.rjust(12), end="")

    print()

    for i in range(len(products)):

        print(products[i].ljust(18), end="")

        for j in range(len(warehouses)):
            print(str(matrix[i][j]).rjust(12), end="")

        print()


# Function to display shortage and surplus
def display_stock_analysis(stock, target, products, warehouses):

    shortages, surpluses = identify_stock(stock, target)

    print("\n========== STOCK SHORTAGE REPORT ==========")

    found = False

    for i in range(len(products)):

        for j in range(len(warehouses)):

            if shortages[i][j] > 0:

                found = True

                print(
                    products[i],
                    "-",
                    warehouses[j],
                    "Shortage:",
                    shortages[i][j]
                )

    if not found:
        print("No stock shortages found.")

    print("\n========== STOCK SURPLUS REPORT ==========")

    found = False

    for i in range(len(products)):

        for j in range(len(warehouses)):

            if surpluses[i][j] > 0:

                found = True

                print(
                    products[i],
                    "-",
                    warehouses[j],
                    "Surplus:",
                    surpluses[i][j]
                )

    if not found:
        print("No stock surpluses found.")


# Main Program
print("==============================================")
print("       INVENTORY MATRIX RECONCILIATION")
print("==============================================")

# Get warehouse details
warehouse_count = get_positive_integer(
    "\nEnter number of warehouses: "
)

warehouses = []

for i in range(warehouse_count):

    name = input("Enter warehouse " + str(i + 1) + " name: ").strip()

    while name == "" or name in warehouses:

        if name == "":
            print("Warehouse name cannot be empty.")
        else:
            print("Warehouse name already exists.")

        name = input("Enter another warehouse name: ").strip()

    warehouses.append(name)


# Get product details
product_count = get_positive_integer(
    "\nEnter number of products: "
)

products = []

for i in range(product_count):

    name = input("Enter product " + str(i + 1) + " name: ").strip()

    while name == "" or name in products:

        if name == "":
            print("Product name cannot be empty.")
        else:
            print("Product name already exists.")

        name = input("Enter another product name: ").strip()

    products.append(name)


# Create stock matrix
stock = []

print("\n========== ENTER CURRENT STOCK ==========")

for i in range(product_count):

    row = []

    print("\nProduct:", products[i])

    for j in range(warehouse_count):

        quantity = get_quantity(
            "Enter " + warehouses[j] + " stock: "
        )

        row.append(quantity)

    stock.append(row)


# Create target stock matrix
target = []

print("\n========== ENTER TARGET STOCK ==========")

for i in range(product_count):

    row = []

    print("\nProduct:", products[i])

    for j in range(warehouse_count):

        quantity = get_quantity(
            "Enter " + warehouses[j] + " target stock: "
        )

        row.append(quantity)

    target.append(row)


# Display current stock
display_matrix(
    "CURRENT INVENTORY MATRIX",
    stock,
    products,
    warehouses
)


# Display target stock
display_matrix(
    "TARGET INVENTORY MATRIX",
    target,
    products,
    warehouses
)


# Identify shortages and surpluses
display_stock_analysis(
    stock,
    target,
    products,
    warehouses
)


# Calculate transfers
updated_stock, transfers = calculate_transfers(
    stock,
    target,
    products,
    warehouses
)


# Display transfer plan
print("\n========== STOCK TRANSFER PLAN ==========")

if len(transfers) == 0:

    print("No stock transfers required.")

else:

    for i in range(len(transfers)):

        transfer = transfers[i]

        print("\nTransfer", i + 1)

        print("Product:", transfer[0])
        print("From:", transfer[1])
        print("To:", transfer[2])
        print("Quantity:", transfer[3])


# Display updated inventory
display_matrix(
    "UPDATED INVENTORY MATRIX",
    updated_stock,
    products,
    warehouses
)


# Final reconciliation report
print("\n========== FINAL RECONCILIATION ==========")

all_targets_met = True

for i in range(product_count):

    for j in range(warehouse_count):

        if updated_stock[i][j] < target[i][j]:

            all_targets_met = False

            print(
                "Remaining shortage:",
                products[i],
                "-",
                warehouses[j],
                ":",
                target[i][j] - updated_stock[i][j]
            )

        elif updated_stock[i][j] > target[i][j]:

            all_targets_met = False

            print(
                "Remaining surplus:",
                products[i],
                "-",
                warehouses[j],
                ":",
                updated_stock[i][j] - target[i][j]
            )


if all_targets_met:

    print("\nSUCCESS: All warehouse stock targets achieved.")

else:

    print("\nNOTICE: Some stock targets could not be matched.")

print("\nInventory Reconciliation Completed!")
