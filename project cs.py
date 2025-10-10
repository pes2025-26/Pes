def boot():
    print(dt.datetime.now())
    print("1. REGISTER")
    print()
    print("2.LOGIN")
    print()
    print("3.EXIT")
    print()
    b=input("Enter your choice")
    return b



def reg():
    name=input("Enter your Username :")
    print()
    password=int(input("Enter digit password"))
    print()
    gmail=input("Enter your Gmail")
    print()
    val=(name,password,gmail)
    v_SQLInsert="INSERT INTO log_id (username,password,gmail) {}".format(val)
    cur.execute(v_SQLInsert)
    con.commit()
    print()
    print("USER created")
    import mainpage


def log():
    name=input("enter the Username :")
    print()
    password=int(input("enter the Password :"))
    v_Sql_sel="select + from log_id where password = '"+str(password)+"' and user_id = '"+name+"'"
    cur.execute(v_Sql_sel)
    if cur.fetchall() is none:
        print()
        print("invalid user and password")
    else:
        print()
        import mainpage




def menu():
    print("                                                                       EMPLOYEE MANAGMENT SYSTEM                                                                        ")
    print("1.Add Employee")
    print("2.View Employees")
    print("3.Employees Details")
    print("4.View Employee")
    print("5.Update Employee Details")
    print("6.Remove Employee")
    print("7.Logout")

    ch=int(input("Enter The Choice:"))
    if ch==1:
        addemp()
    elif ch==2:
        viewall()
    elif ch==3:
        viewempdel()
    elif ch==4:
        viewemp1()
    elif ch==5:
        upd()
    elif ch==6:
        dels()
    elif ch==7:
        logout()
        exit()
    else:
        print("Invalid option")




def logout():
    print("Loging out")


def dels():
    ide=int(input("Enter employee id to delete"))
    de=("DELETE FROM employee WHERE id={}").format(ide)
    cur.execute(de)
    con.commit()



def viewall():
    view="SELECT name FROM employee"
    cur.execute(view)
    x=cur.fetchall()
    for i in x:
        print(i)


def addemp():
    name=input("enter name")
    dept=input("enter department")
    perf=int(input("Rate performance out of 10"))
    salary=float(input("Enter salary"))
    ph=int(input("Enter phone number"))
    det=(name,dept,perf,salary,ph)
    cur.execute("INSERT INTO employee(name,department,performance,salary,phno) values {};").format(det)
    print("Employee added successfully")

    view=("SELECT name FROM employee")

def viewemp1():
    ide=int(input("Enter employee id"))
    eo=("SELECT * FROM employee WHERE id={}").forma(eo)

def viewempdet():
    view="SELECT * FROM employee"
    cur.execute(view)
    x=cur.fetchall()
    for i in x:
        print(i)

def upd():
    print("Enter the detail you want to update")
    print("*")
    print()
    print('1.salary')
    print('2.Department')
    print('3.Performance')
    ch=int(input("Enter choice"))
    if ch==1:
        sal=float(input("Enter new sal"))
        upd1=("update employee set salary={}").format(sal)
        cur.excute(upd2)
        con.commit
        print("salary changed successfully")
    elif ch==2:
        dept==input("Enter new department")
        upd2=("update employee set department={};").format(dept) 
        cur.excute(upd2)
        con.commit
        print("department changed successfully")
    elif ch==3:
        perf=int(input("Enter new performance"))
        upd4=("update employee set performance={};").format(perf)
        cur.excute(upd2)
        con.commit
        print("Performance upadated successfully")
    else:
        print("option does not exist")



import mysql.connector as sql
con=sql.connect(host='localhost',user='root',passwd="root",database='COMPANY')
cur = con.cursor()
cur.execute("create table log_id(username varchar(25) primary key, password varchar(25) not null,gmail varchar(25) not null)")
print("================================================================= Welcome to Employee Management System ===============================================================")
import datetime as dt
while True:
    boot()
    if b==1:
        reg()
        while True:
            menu()
    elif b==2:
        log()
        while True:
            menu()
    elif b==3:
        break
        
    else:
        print("Invalid option")

    
