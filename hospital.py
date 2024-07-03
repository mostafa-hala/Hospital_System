Clinics=[{"id":"1234","name":"mo","gender":"male","age":"22"}]
x_rays=[{"id":"2000","name":"so","gender":"female","age":"20"}]
surgery=[{"id":"1234","name":"mo","gender":"male","age":"22"}]
    

def check (id):
    c=0
    id=str(id)
    if id.isdigit() and len(id)==4:
        c+=1
    else: print("invalid number enter 4  numbers only ")
    return c


def exit():
    op=int(input(""" thank you 
     if you want return to main menu enter 0 if not any other """))
    return op 


def menu():
    choice=input("""****** welcome to the hospital ******
    1- New Patient 
    2- view information
    3- update information
    4- discharge patient
    5- display all patients ..""")
    return choice 


def checker(id):
    z=0 
    n=0   
    for i in range (0,len(Clinics)):
        if Clinics[i]["id"]==id:
             z+=1 
             n=i
    for i in range (0,len(x_rays)):
        if x_rays[i]["id"]==id:
             z+=3
             n=i
    for i in range (0,len(surgery)):
        if surgery[i]["id"]==id:
             z+=5
             n=i
    return z ,n 

def add_patient (Clinics,surgery,x_rays,id,section,name,age,gendre):
    if section==1:
            val,index=checker(id)
            if val ==0 :
                Clinics.append({"id":id,"name":name,"gender":gendre,"age":age})
                print('information has been saved ')
                print(Clinics[-1])
            elif val==1 or val==4 or val==6 or val==9:
                print("this patient is already present ")
            elif val==3 :
                print(x_rays[index])
                c=int(input("""this patient is already present in x-rays list 
                press 1 if you want add him to clinics and else if no """))
                if c==1:
                    print("the patient will be added with the infor. already present ")
                    Clinics.append(x_rays[index])
                    print(Clinics[-1])
            elif val==5:
                print(surgery[index])
                c=int(input("""this patient is already present in x-rays list 
                press 1 if you want add him to clinics and else if no """))
                if c==1:
                    print("the patient will be added with the infor. already present ")
                    Clinics.append(surgery[index])
                    print(Clinics[-1])
    elif section==2:
            val,index=checker(id)
            if val ==0:
                x_rays.append({"id":id,"name":name,"gender":gendre,"age":age})
                print('information has been saved  ')
                print(x_rays[-1])
            elif val==1 or val==6:
                if val==1:
                    print(Clinics[index])
                elif val==6:
                    print(surgery[index])
                c=int(input("""this patient is already present in another list 
                press 1 if you want add him to x-rays and else if no """))
                if c==1:
                    print("the patient will be added with the infor. already present ")
                    if val==1:
                        x_rays.append(Clinics[index])
                    elif val==6:
                        x_rays.append(surgery[index])
                    print(x_rays[-1])
            elif val==4 or val==9 or val==8 or val==3:
                print("this patient is already present ")
                print(x_rays[index])
            elif val==5:
                print(surgery[index])
                c=int(input("""this patient is already present in surgery list 
                press 1 if you want add him to x-rays and else if no """))
                if c==1:
                    print("the patient will be added with the infor. already present ")
                    x_rays.append(surgery[index])
                    print(x_rays[-1])
    elif section==3:
            val,index=checker(id)
            if val ==0:
                surgery.append({"id":id,"name":name,"gender":gendre,"age":age})
                print(f'information has been saved and your id is {id} ')
                print(surgery[-1])
            elif val==1 or val==4 :
                if val==1:
                    print(Clinics[index])
                elif val==4:
                    print(x_rays[index])
                c=int(input("""this patient is already present in another list 
                press 1 if you want add him to surgery list and else if no """))
                if c==1:
                    print("the patient will be added with the infor. already present ")
                    if val==1:
                        surgery.append(Clinics[index])
                    elif val==4:
                        surgery.append(x_rays[index])
                    print(surgery[-1])
            elif val==3 :
                print(x_rays[index])
                c=int(input("""this patient is already present in x_rays list 
                press 1 if you want add him to surgery list and else if no """))
                if c==1:
                    print("the patient will be added with the infor. already present ")
                    surgery.append(x_rays[index])
                    print(surgery[-1])
            elif val==5 or val==9 or val==8:
                print("this patient is already present ")
                print(surgery[index])
    else: print("enter number from 1 t0 3")


def view (Clinics,surgery,x_rays,id,s):
    z=0
    s=int(s)
    if s==1:
        for i in range (0,len(Clinics)):
            if Clinics[i]["id"]==id:
                z+=1
                print(f''' -patient name ;{Clinics[i]["name"]}
                -age;{Clinics[i]["age"]}
                -gender;{Clinics[i]["gender"]}''')
    if s==2:
        for i in range (0,len(x_rays)):
            if x_rays[i]["id"]==id:
                z+=1
                print(f''' -patient name ;{x_rays[i]["name"]}
             -age;{x_rays[i]["age"]}
             -gender;{x_rays[i]["gender"]}''')
    if s==3:
        for i in range (0,len(surgery)):
            if surgery[i]["id"]==id:
                z+=1
                print(f''' -patient name ;{surgery[i]["name"]}
             -age;{surgery[i]["age"]}
             -gender;{surgery[i]["gender"]}''')
    if z==0  :print("their is no patient with this id ")
    elif not z==0 and not s==1 or s==2 or s==3:print("invalid enter number from 1 to 3")


def discharge(Clinics,surgery,x_rays,id):
    z=0
    for i in range (0,len(Clinics)):
        if Clinics[i]["id"]==id:
             del Clinics[i]
             z+=1
             break
    for i in range (0,len(x_rays)):
            if x_rays[i]["id"]==id:
             del x_rays[i]
             z+=1
             break
    for i in range (0,len(surgery)):
            if surgery[i]["id"]==id:
             del surgery[i]
             z+=1
             break
    if z==0:print("there is no patient with this id ")
    else: print("patient is discharged successfully")


#def update (Clinics,surgery,x_rays,id,age,name, gender ):
#    z=0
#    new={"id":id,"name":name,"gender":gender,"age":age}
#    for i in range (0,len(Clinics)):
#        if Clinics[i]["id"]==id:
#            Clinics[i].update(new) 
#            z+=1
#            break
#    for i in range (0,len(x_rays)):
#            if x_rays[i]["id"]==id:
#             x_rays[i].update(new)
#             z+=1
#             break
#    for i in range (0,len(surgery)):
#            if surgery[i]["id"]==id:
#             surgery[i].update(new)
#             z+=1
#             break
#    if not z==0:
#        print("the  infor is updated successfully ")
#        print(new)
#    else: print("this id can not be found ")
def update1 (Clinics,surgery,x_rays,id ):
    for i in Clinics or x_rays or surgery:
        if i["id"]==id:
            new={"id":id,"name":i["name"],"age":i["age"],"gender":i["gender"]}  
    z=0
    inp=input("choose 1.2.3 ")
    if inp=="1":
        name=input("enter the new name ")
        new.update({"name":name})
    if inp=="2":
        age=input("enter the new age ")
        new.update({"age":age})
    if inp=="3":
        gender=int(input("""choose your gendre
            1- male  2- female  """))
        if gender==1:
                gender="male"
        else:
                gender="female"
        new.update({"gender":gender})

    for i in range (0,len(Clinics)):
        if Clinics[i]["id"]==id:
            Clinics[i].update(new) 
            z+=1
            break
    for i in range (0,len(x_rays)):
            if x_rays[i]["id"]==id:
             x_rays[i].update(new)
             z+=1
             break
    for i in range (0,len(surgery)):
            if surgery[i]["id"]==id:
             surgery[i].update(new)
             z+=1
             break
    if not z==0:
        print("the  infor is updated successfully ")
        print(new)
    else: print("this id can not be found ")


def display(Clinics,surgery,x_rays):
    print("""the clinic patients
_____________________________""")
    for i in Clinics:
        print("{}\t\t\t{}\t\t\t{}".format(i["name"],i["age"],i["gender"]))
    print("            ****************             ")
    print("""the x ray patient
_____________________________""")
    for i in x_rays:
        print("{}\t\t\t{}\t\t\t{}".format(i["name"],i["age"],i["gender"]))
    print("            ****************             ")
    print("""the surgury patients
______________________________""")
    for i in surgery:
        print("{}\t\t\t{}\t\t\t{}".format(i["name"],i["age"],i["gender"]))

while True :
    m=menu()
    if not m.isdigit() and not m in range (0,6):
        print("Enter number from  0 to 5")
    else:
        m=int(m)
        if m==0:
            quit=exit()
            if quit==0:
                continue
            else: break
        elif m==1 :
            section=int(input("""choose the section 
            1-clinics
            2- x-rays
            3-surgery  """))
            id=input("enetr the id ")
            c=check(id)
            if c==0 :
                quit=exit()
                if quit==0:
                    continue
                else: break
            else:
                name=input("enter the patient name ")
                age=input("enter the patient age ")
                gendre=int(input("""choose your gendre
                1- male  2- female  """))
                if gendre==1:
                    gendre="male"
                else:
                    gendre="female"
                add_patient(Clinics,surgery,x_rays,id,section,name,age,gendre)
                q=exit()
                if q==0:
                    continue
                else:break
        elif m==2:
            s=input("""choose the section 
            1-clinics
            2- x-rays
            3-surgery  """)
            id=input("enter your id ")
            c=check(id)
            if c==0 :
                quit=exit()
                if quit==0:
                    continue
                else: break
            else:
                view(Clinics,surgery,x_rays,id,s)
                q=exit()
                if q==0:
                    continue
                else:break
        elif m==3 :
            id=input("enter your id ")
            c=check(id)
            if c==0 :
                quit=exit()
                if quit==0:
                    continue
                else: break
            else:
                update1(Clinics,surgery,x_rays,id)
                q=exit()
                if q==0:
                    continue
                else:break
        elif m==4:
            id=input("enter your id ")
            c=check(id)
            if c==0 :
                quit=exit()
                if quit==0:
                    continue
                else: break
            else:
                discharge(Clinics,surgery,x_rays,id)
                q=exit()
                if q==0:
                    continue
                else:break
        elif m==5:
                display(Clinics,surgery,x_rays)
                q=exit()
                if q==0:
                    continue
                else:break



            





        


