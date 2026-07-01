FILE = "employee.txt"


# ADD
def add_employee():

    e_id = input("Enter Employee ID: ")
    e_name = input("Enter Name: ")
    e_dep = input("Enter Department: ")
    salary = input("Enter Salary: ")

    with open(FILE, "a") as f:
        f.write(f"{e_id},{e_name},{e_dep},{salary}\n")

    print("Employee Added")


# VIEW
def view_employee():

    try:

        with open(FILE, "r") as f:

            data = f.readlines()

            if len(data) == 0:
                print("No Records")

            else:

                for row in data:
                    print(row.strip())

    except FileNotFoundError:
        print("File Not Found")


# UPDATE
def update_employee():

    emp_id = input("Enter Employee ID: ")

    new_data = []

    found = False

    with open(FILE, "r") as f:

        records = f.readlines()

    for row in records:

        data = row.strip().split(",")

        if data[0] == emp_id:

            name = input("Enter New Name: ")
            dep = input("Enter New Department: ")
            salary = input("Enter New Salary: ")

            new_data.append(
                f"{emp_id},{name},{dep},{salary}\n"
            )

            found = True

        else:
            new_data.append(row)

    with open(FILE, "w") as f:

        f.writelines(new_data)

    if found:
        print("Updated Successfully")

    else:
        print("Employee Not Found")


# DELETE
def delete_employee():

    emp_id = input("Enter Employee ID: ")

    new_data = []

    found = False

    with open(FILE, "r") as f:

        records = f.readlines()

    for row in records:

        data = row.strip().split(",")

        if data[0] != emp_id:
            new_data.append(row)

        else:
            found = True

    with open(FILE, "w") as f:

        f.writelines(new_data)

    if found:
        print("Deleted Successfully")

    else:
        print("Employee Not Found")


# MENU
while True:

    print("\n===== EMPLOYEE MANAGEMENT =====")
    print("1. Add")
    print("2. View")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    match choice:

        case 1:
            add_employee()

        case 2:
            view_employee()

        case 3:
            update_employee()

        case 4:
            delete_employee()

        case 5:
            print("Program Closed")
            break

        case _:
            print("Invalid Choice")
