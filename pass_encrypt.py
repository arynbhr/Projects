from cryptography.fernet import Fernet
def create_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def key_load():
    with open("key.key","rb") as f:
        key=f.read()
        return key
def view():
    with open("Password.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user,pwd=data.split("|")
            print("\nAccount : ",user)
            print("Password : ",(fer.decrypt(pwd).decode()))
def add():
    acc_name=input("Enter account name : ")
    pwd=input("Enter password : ")
    
    with open("Password.txt","a") as f:
        f.write(acc_name+"|"+ fer.encrypt(pwd.encode()).decode()+"\n") 
create_key()        
key=key_load()
fer=Fernet(key)                       
while True:
    choice=input("Enter your choice (add,view) and q for quit : ")
    
    if choice=="add":
        add()
    elif choice=="view":
        view()
    elif choice=="q":
        break
    else:
        continue