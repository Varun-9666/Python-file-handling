granted = False
def grant():
    global granted
    granted = True
def login(Email,Password):
    success = False
    file = open("userdetails.txt","r")
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==Email and b==Password):
             success = True
             break
    file.close()
    if(success):
        print("Login Successful")
        grant()
    else:
        print("wrong Email and Password")

def register():
  DB = open("userdetails.txt", "r")
  Email = input("Enter the email: ")

  lower, upper, special, digit = 0, 0, 0, 0
  Password = input("Enter the password: ")

  if len(Password)>=5 and len(Password)<=16:
    for i in Password:
      for word in Password.split():
        if (i.isupper()):
          upper +=1
        if (i.islower()):
          lower +=1
        if (i.isdigit()):
          digit +=1
        if (i == '@' or i == '$' or i == '_' or i =='#'):
          special +=1
  else:
    print("Password should be more than 5 char and less than 16 char")
  if (lower >= 1 and upper >= 1 and special >= 1 and digit >= 1):
    print("Good Password")
    DB = open("userdetails.txt", "a")
    DB.write(Email+", "+Password+"\n")
  else:
    print("Must have minimum one special character,one digit,one uppercase, one lowercase character")

def access(option):
    global name
    if(option=="login"):
        Email = input("Enter your Email: ")
        Password = input("Enter your password: ")
        login(Email,Password)
    else:
        print("Enter your Email and Password to register")
        register()

def begin():
    global option
    print("welcome")
    option = input("login or reg: ")
    if(option!="login" and option!="reg"):
        begin()
        
begin()
access(option)
if(granted):
  print("Welcome")
