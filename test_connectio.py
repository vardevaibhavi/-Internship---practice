import mysql.connector

# Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="EMPL"
)

cursor = conn.cursor()

if conn.is_connected():
    print("MySQL Connected Successfully")


# INSERT
def insert_data():

    e_id = int(input("Enter employee id: "))
    e_name = input("Enter employee name: ")
    e_dep = input("Enter department name: ")
    salary = int(input("Enter salary: "))

    sql = """
    INSERT INTO EMP
    (e_id, e_name, e_dep, salary)
    VALUES (%s, %s, %s, %s)
    """

    val = (e_id, e_name, e_dep, salary)

    cursor.execute(sql, val)
    conn.commit()

    print("Inserted Successfully")


# VIEW
def show_data():

    cursor.execute("SELECT * FROM EMP")

    data = cursor.fetchall()

    if len(data) == 0:
        print("No Records Found")

    else:
        for row in data:
            print(row)


# UPDATE
def update_data():

    e_id = int(input("Enter employee id: "))
    new_dep = input("Enter new department: ")

    sql = "UPDATE EMP SET e_dep=%s WHERE e_id=%s"

    val = (new_dep, e_id)

    cursor.execute(sql, val)

    conn.commit()

    print("Data Updated Successfully")


# DELETE
def delete_data():

    e_id = int(input("Enter employee id to delete: "))

    sql = "DELETE FROM EMP WHERE e_id=%s"

    val = (e_id,)

    cursor.execute(sql, val)

    conn.commit()

    print("Data Deleted Successfully")


# MENU (Switch Case)

while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    match choice:

        case 1:
            insert_data()

        case 2:
            show_data()

        case 3:
            update_data()

        case 4:
            delete_data()

        case 5:
            print("Program Closed")
            break

        case _:
            print("Invalid Choice")


cursor.close()
conn.close()
