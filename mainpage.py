import time
import definefile
print ("\t\t\t",time.ctime())

import mysql.connector as sql
con=sql.connect(host="localhost",user="root",password="root",database="COMPANY")
mycusor=con.cursor()
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