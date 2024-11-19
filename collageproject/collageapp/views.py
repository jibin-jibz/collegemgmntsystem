from django.shortcuts import render,redirect            
from django.http import HttpResponse
from collageapp.models import User,Departmnet,Student,Teacher
from django.contrib.auth import authenticate,login,logout
# Increase the recursion limit to 1500



# Create your views here.

# department adding

def dep_adding(request):
    if request.method=='POST':
        D=request.POST['dep_add']
        x=Departmnet.objects.create(Deparname=D)
        x.save()
        return HttpResponse("<script>window.alert('okk');window.location.href = '/collage/dep_regi';</script>")
        # response = HttpResponse(""" <script> alert('okk'); window.location.href = '/path/to/dep_adding/'; </script> """) 
        # return response()
        
    else:
        return render(request,'dep_regi.html')


#  creating admin page]

def mainhome(request):
    return render(request,'mainhome.html')

def adminpage(request):
    return render(request,'adminpage.html')

# HOME PAGE [ student  aD teacherregistration page]

def studentpage(request):
    return render(request,'studentpage.html')

def teacherpage(request):
    return render(request,'teacherpage.html')
# stud reg form

def studentreg(request):
    if request.method=='POST':
        r=request.POST['dep']
        s=request.POST['fname']
        t=request.POST['lname']
        u=request.POST['email']
        d=request.POST['uname']
        e=request.POST['password']
        n=request.POST['age']
        a=request.POST['address']
        x=User.objects.create_user(username=d,password=e,email=u,first_name=s,last_name=t,USERTYPE='STUDENT',is_active=False)
        x.save()
        y=Student.objects.create(Depar_id_id=r,sid=x,Age=n,Address=a)
        y.save()
        return HttpResponse("student registerd")
    else:
        x=Departmnet.objects.all()
        return render(request,'student_reg.html',{'x1':x})
    
# stude view page

def studview(request):
    x=Student.objects.all()
    return render(request,'studtable.html',{'x1':x})

# stud approved

def approve(request,aid):
    st=Student.objects.get(id=aid)
    st.sid.is_active=True
    st.sid.save()
    return HttpResponse("<script>alert('success');window.location.href='/studtable';</script>")

def approved_stud(request):
    x=User.objects.filter(is_active=1,USERTYPE='STUDENT')
    return render(request,'aproved_stud.html',{'x1':x})


    

# techer reg 

def techerreg(request):
    if request.method=='POST':
        t=request.POST['dep']
        e=request.POST['fname']
        a=request.POST['lname']
        c=request.POST['email']
        h=request.POST['uname']
        e=request.POST['password']
        r=request.POST['age']
        s=request.POST['address']
        r=request.POST['age']
        q=request.POST['qual']
        x=User.objects.create_user(username=h,password=e,email=c,first_name=e,last_name=a,USERTYPE='TEACHER')
        x.save()
        y=Teacher.objects.create(Depar_id_id=t,tid=x,Age=r,Address=s,Qualification=q)
        y.save()
        return HttpResponse("<script>alert('success');window.location.href='techerreg';</script>")
    else:
        x=Departmnet.objects.all()

        return render(request,'techer_reg.html',{'x1':x})
    
# login page for admin , student , teacher
def logins(request):
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['password']
        user=authenticate(request,username=u,password=p)
        if user is not None and user.is_superuser==1:
            return redirect(adminpage)
        elif user is not None and user.USERTYPE=='TEACHER':
            login(request,user)
            request.session['teach_id']=user.id
            return redirect(teacherpage)
        elif user is not None and user.USERTYPE=='STUDENT':
            login(request,user)
            request.session['stud_id']=user.id
            return redirect(studentpage)
        else:
            return HttpResponse("<h1>NOT VALID</h1>")
         
    else:


        return render(request,'login.html')

        
# update student

def updates(request):
    su=request.session.get('stud_id')
    stude=Student.objects.get(sid_id=su)
    user=User.objects.get(id=su)
    return render(request,'updte_stud.html',{'view':stude,'data':user})

def update_stu(request,uid):
    if request.method=='POST':
        stud=Student.objects.get(id=uid)
        sid=stud.sid_id
        user=User.objects.get(id=sid)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        user.username=request.POST['uname']
        user.save()
        stud.Age=request.POST['age']
        stud.Address=request.POST['address']
        stud.save()
        return HttpResponse("success")

def updat(request):   
    tu=request.session.get('teach_id')
    teud=Teacher.objects.get(tid_id=tu)
    user=User.objects.get(id=tu)
    return render(request,'updte_teach.html',{'view':teud,'data':user})

def update_teach(request,tid):
    if request.method=='POST':
        tude=Teacher.objects.get(id=tid)
        tid=tude.tid_id
        user=User.objects.get(id=tid)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        user.username=request.POST['uname']
        user.save()
        tude.Age=request.POST['age']
        tude.Address=request.POST['address']
        tude.save()
        return HttpResponse('YOU DON')
# delete student details
def deletel(request,dsid):
    x=User.objects.get(id=dsid)
    x.delete()
    return redirect(studview)

def delete2(request,dtis):
    y=User.objects.get(id=dtis)
    y.delete()
    return redirect()


def teachview(request):
    x=Teacher.objects.all()
    return render(request,'teach_table.html',{'x1':x})

def studview(request):
    x=Student.objects.all()
    return render(request,'stud_dtls.html',{'x1':x})


# claass teacher view for student

# def teachersviewbyst(request):
#     id=request.session['tid']
#     teacher=User.objects.get(id=id)
#     Depar_id=teacher.depar_id
#     students = User.objects.filter( Depar_id= Depar_id,is_staff=0)
#     return render(request,"viewdpbyst.html",{'sid':students})
  



    
def logouts(request):
    logout(request)
    return redirect(logins)


