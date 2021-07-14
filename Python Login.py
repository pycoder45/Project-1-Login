import pickle
import os 

#global data_file
#global data
if os.path.isfile("u_data.txt"): 
  pass
else : 
  make_f = open("u_data.txt","wb")
  sample = { "user_admin": {"name": "data","email": "bhai@gmail.com","username": "admin1","password": "qwerty"} }
  pickle.dump(sample,make_f)
  make_f.close()
 
data_file = open("u_data.txt","rb")
data = pickle.load(data_file)
database = data
data_file.close()

def update_data(): 
  nf = open("u_data.txt","wb")
  pickle.dump(database,nf)
  nf.close()

def signup():
  _name = input("Enter Your Name : ")
  _email = input("Enter Your Email : ")
  _username = input("Set Username : ")
  _password = input("Enter Your Password : ")
  
  database[_username] = {
    "name" : _name,
    "email" : _email,
    "username" : _username,
    "password" : _password
  }
  update_data()
  print("\n\t -| ACCOUNT CREATED SUCCESSFULLY |-\n")

def login():
  u_username = input("Enter Your Username: ")
  u_password = input("Password: ")
  
  getfile = open("u_data.txt","rb")
  getdata = pickle.load(getfile)
  
  if u_username in getdata:
    if (getdata[u_username]["username"] == u_username) and (getdata[u_username]["password"] == u_password): 
      print("\n\t-| Logged In Successfully ✓ |-")
    else: 
      print("\n\t -| Check Your Password :( |-")
  else : 
    print("\n\t -| Account Not Exist | Create A New One |-\n")

update_data()

print("\n\t\t | LOGIN |  OR  | SIGN-UP | \n")
print("\t [ Use 'L' for Login & 'S' for Sign-up ]")

ls_input = input("~ ")

if ls_input == "L": 
  login()
elif ls_input == "S": 
  signup()
else: 
  print("Enter The Command Correctly ")

# DATA BRIDGE

file1 = open("u_data.txt","rb")
readit = pickle.load(file1)
print(readit)

name_DB = []
email_DB = []
username_DB = []
password_DB = []

for key in readit: 
  name_DB.append(readit[key]["name"])
  email_DB.append(readit[key]["email"])
  username_DB.append(readit[key]["username"])
  password_DB.append(readit[key]["password"])


file1.close()


bsit = open("minihtml.html","w")
bsit.write('''<!doctypehtml><html lang=en><title>Table V02</title><meta charset=UTF-8><meta content="width=device-width,initial-scale=1"name=viewport><style media=all>@import url(https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap);*{margin:0;padding:0;box-sizing:border-box}body,html{height:100%;font-family:sans-serif}a{margin:0;transition:all .4s;-webkit-transition:all .4s;-o-transition:all .4s;-moz-transition:all .4s}a:focus{outline:0!important}a:hover{text-decoration:none}h1,h2,h3,h4,h5,h6{margin:0}p{margin:0}li,ul{margin:0;list-style-type:none}input{display:block;outline:0;border:none!important}textarea{display:block;outline:0}input:focus,textarea:focus{border-color:transparent!important}button{outline:0!important;border:none;background:0 0}button:hover{cursor:pointer}iframe{border:none!important}.limiter{width:100%;margin:0 auto}.container-table100{width:100%;min-height:100vh;background:#c4d3f6;display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;align-items:center;justify-content:center;flex-wrap:wrap;padding:33px 30px}.wrap-table100{width:960px;border-radius:10px;overflow:hidden}.table{width:100%;display:table;margin:0}@media screen and (max-width:768px){.table{display:block}}.row{display:table-row;background:#fff}.row.header{color:#fff;background:#6c7ae0}@media screen and (max-width:768px){.row{display:block}.row.header{padding:0;height:0}.row.header .cell{display:none}.row .cell:before{font-family:Poppins,sans-serif!important;font-weight:700!important;font-size:12px;color:grey;line-height:1.2;text-transform:uppercase;font-weight:unset!important;margin-bottom:13px;content:attr(data-title);min-width:98px;display:block}}.cell{display:table-cell}@media screen and (max-width:768px){.cell{display:block}}.row .cell{font-family:Poppins,sans-serif!important;font-weight:400!important;font-size:15px;color:#666;line-height:1.2;font-weight:unset!important;padding-top:20px;padding-bottom:20px;border-bottom:1px solid #f2f2f2}.row.header .cell{font-family:Poppins,sans-serif!important;font-weight:400!important;font-size:18px;color:#fff;line-height:1.2;font-weight:unset!important;padding-top:19px;padding-bottom:19px}.row .cell:nth-child(1){width:240px;padding-left:40px}.row .cell:nth-child(2){width:240px;padding-left:20px}.row .cell:nth-child(3){width:240px;padding-left:20px}.row .cell:nth-child(4){width:240px;padding-left:0}.row,.table{width:100%!important}.row:hover{background-color:#ececff;cursor:pointer}@media (max-width:768px){.row{border-bottom:1px solid #f2f2f2;padding-bottom:18px;padding-top:30px;padding-right:15px;margin:0}.row .cell{border:none;padding-left:30px;padding-top:16px;padding-bottom:16px}.row .cell:nth-child(1){padding-left:30px}.row .cell{font-family:Poppins,sans-serif!important;font-weight:400!important;font-size:18px;color:#555;line-height:1.2;font-weight:unset!important}.cell,.row,.table{width:100%!important}}</style><div class=limiter><div class=container-table100><div class=wrap-table100><div class=table id=adi45><div class="row header"><div class="cell hd">Full Name</div><div class="cell hd">Email Address</div><div class="cell hd">Username</div><div class="cell hd">Password</div></div><div class=row><div class=cell data-title="Full Name">Joseph Smith</div><div class=cell data-title=Age>27</div><div class=cell data-title="Job Title">Project Manager</div><div class=cell data-title=Location>Somerville, MA</div></div></div></div></div></div><script charset=utf-8>''')
#bsit.close()

#asit = open("minijs.js","w")
bsit.write(f"var name_DB = {name_DB};")
bsit.write(f"var email_DB = {email_DB};")
bsit.write(f"var username_DB = {username_DB};")
bsit.write(f"var password_DB = {password_DB};")
bsit.write('''for(var i=0;i<name_DB.length;i++)data123=`<div class="row"><div class="cell" data-title="Full Name">${name_DB[i]}</div><div class="cell" data-title="Age">${email_DB[i]}</div><div class="cell" data-title="Job Title">${username_DB[i]}</div><div class="cell" data-title="Location">${password_DB[i]}</div></div>`,document.getElementById("adi45").innerHTML+=data123;''')
bsit.write("</script>")
bsit.close()
