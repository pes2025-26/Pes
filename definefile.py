def logout():
    print("Loging out")
    exit

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
        upd1=("update employee set salary={}";).format(sal)
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