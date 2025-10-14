import mysql.connector as sql
import datetime as dt

con = sql.connect(host='localhost', user='root', passwd='root', database='COMPANY')
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS log_id(
    username VARCHAR(25) PRIMARY KEY,
    password VARCHAR(25) NOT NULL,
    gmail VARCHAR(25) NOT NULL
)
""")

print("================================================================= Welcome to Employee Management System ===============================================================")

def boot():
    print(dt.datetime.now())
    print("1. REGISTER\n")
    print("2. LOGIN\n")
    print("3. EXIT\n")
    b = int(input("Enter your choice: "))
    return b

def reg():
    name = input("Enter your Username: ")
    password = int(input("Enter digit password: "))
    gmail = input("Enter your Gmail: ")
    val = (name, password, gmail)
    v_SQLInsert = "INSERT INTO log_id (username,password,gmail) VALUES {}".format(val)
    cur.execute(v_SQLInsert)
    con.commit()
    print("USER created successfully!")

def log():
    name = input("Enter the Username: ")
    password = int(input("Enter the Password: "))
    v_Sql_sel = "SELECT * FROM log_id WHERE password='{}' AND username='{}'".format(password, name)
    cur.execute(v_Sql_sel)
    if cur.fetchall() == []:
        print("Invalid username or password")
    else:
        print("Login successful!")
        menu()

def menu():
    print("\n------------------- EMPLOYEE MANAGEMENT SYSTEM -------------------")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. View Employee Details")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Logout\n")

    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        addemp()
    elif ch == 2:
        viewall()
    elif ch == 3:
        viewempdet()
    elif ch == 4:
        upd()
    elif ch == 5:
        dels()
    elif ch == 6:
        logout()
    else:
        print("Invalid option")

def logout():
    print("Logging out...")

def dels():
    ide = int(input("Enter employee id to delete: "))
    de = "DELETE FROM employee WHERE id={}".format(ide)
    cur.execute(de)
    con.commit()
    print("Employee deleted successfully.")

def viewall():
    cur.execute("SELECT name FROM employee")
    x = cur.fetchall()
    for i in x:
        print(i)

def addemp():
    name = input("Enter name: ")
    dept = input("Enter department: ")
    perf = int(input("Rate performance out of 10: "))
    salary = float(input("Enter salary: "))
    ph = int(input("Enter phone number: "))
    det = (name, dept, perf, salary, ph)
    cur.execute("INSERT INTO employee(name,department,performance,salary,phno) VALUES {}".format(det))
    con.commit()
    print("Employee added successfully!")

def viewempdet():
    cur.execute("SELECT * FROM employee")
    x = cur.fetchall()
    for i in x:
        print(i)

def upd():
    print("\nEnter the detail you want to update:")
    print("1. Salary")
    print("2. Department")
    print("3. Performance")
    ch = int(input("Enter choice: "))
    ide = int(input("Enter employee ID: "))

    if ch == 1:
        sal = float(input("Enter new salary: "))
        upd1 = "UPDATE employee SET salary={} WHERE id={}".format(sal, ide)
        cur.execute(upd1)
    elif ch == 2:
        dept = input("Enter new department: ")
        upd2 = "UPDATE employee SET department='{}' WHERE id={}".format(dept, ide)
        cur.execute(upd2)
    elif ch == 3:
        perf = int(input("Enter new performance: "))
        upd3 = "UPDATE employee SET performance={} WHERE id={}".format(perf, ide)
        cur.execute(upd3)
    else:
        print("Invalid option")
        return

    con.commit()
    print("Details updated successfully.")

# Main loop
while True:
    b = boot()
    if b == 1:
        reg()
    elif b == 2:
        log()
    elif b == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid option")
