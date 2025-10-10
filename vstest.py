import mysql.connector as sql
con=sql.connect(host='localhost',user='root',passwd="root",database='COMPANY')
cur = con.cursor()
cur.execute("create table log_id(username varchar(25) primary key, password varchar(25) not null,gmail varchar(25) not null)")
print("================================================================= Welcome to Employee Management System ===============================================================")
import datetime as dt
def boot():
    print(dt.datetime.now())
    print("1. REGISTER")
    print()
    print("2.LOGIN")
    print()
    print("3.EXIT")
    print()
    b=input("Enter REGISTER or LOGIN")
    return b

a=boot()

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

def exit():
    exit
    
if a.lower()=="register":
    reg()
else:
    while True:
        a=boot()
        if a.lower()=="register":
            reg()
            break

if a.lower()=="login":
    log()
else:
    while True:
        a=boot()
        if a.lower()=="login":
            log()
            break
if a.lower()=="exit":
    exit()
else:
    while True:
        a=boot()
        if a.lower()=="exit":
            exit()
            break