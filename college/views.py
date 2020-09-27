from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login,logout,authenticate
import datetime

# Create your views here.
def home(request):
    user = ""
    sign = ""
    stu = ""
    try:
        user = User.objects.get(username=request.user.username)
        sign = Signup.objects.get(user=user)
        stu = Student.objects.get(sign=sign)
    except:
        pass
    d={'stu':stu}
    return render(request,'carousel.html',d)
def nav(request):
    user = ""
    sign = ""
    stu = ""
    try:
        user = User.objects.get(username=request.user.username)
        sign = Signup.objects.get(user=user)
        stu = Student.objects.get(sign=sign)
    except:
        pass
    d={'stu':stu}
    return render(request,'navigation.html',d)

def Admin_home(request):
    accept = 0
    pending = 0
    reject = 0
    application = 0
    student = 0
    course1 = 0
    course = Course.objects.all()
    user = Signup.objects.all()
    app = Student.objects.all()
    status1 = Status.objects.get(status="pending")
    status2 = Status.objects.get(status="Accept")
    status3 = Status.objects.get(status="Reject")
    pend = Student.objects.filter(status=status1).all()
    acc = Student.objects.filter(status=status2).all()
    rej = Student.objects.filter(status=status3).all()
    for i in course:
        course1+=1
    for j in user:
        student+=1
    for k in app:
        application+=1
    for l in pend:
        pending+=1
    for m in acc:
        accept+=1
    for n in rej:
        reject+=1
    d = {'accept':accept,'pending':pending,'reject':reject,'application':application,'student':student,'course1':course1}
    return render(request,'adminhome.html',d)

def User_home(request):
    error = ""
    user = User.objects.get(username=request.user.username)
    sign = Signup.objects.get(user=user)
    data =Student.objects.filter(sign=sign).first()
    upload=False
    try:
        data1 = Upload_Document.objects.get(student=data)
        if data1:
            upload=True
    except:
        pass
    if data:
        error = "ad"
    else:
        error = "ad not"
    d = {'error':error,'upload':upload,'stu':data}
    return render(request,'userhome.html',d)

def home(request):
    notice = Notice.objects.all()
    d = {'notice': notice}
    return render(request,'carousel.html',d)

def About(request):
    return render(request,'about.html')


def Contact(request):
    return render(request,'contact.html')

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "yes"
            else:
                error = "not"
        except:
            error="not"
    d = {'error': error}
    return render(request,'login.html',d)

def Admin_Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "yes"
            else:
                error = "not"
        except:
            error="not"
    d = {'error': error}
    return render(request,'loginadmin.html',d)

def SignUp(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        c = request.POST['contact']
        p = request.POST['pwd']
        user = User.objects.create_user(username=u, password=p,first_name = f,last_name=l,email=e)
        Signup.objects.create(user=user,mobile=c)
        return redirect('login')
    d = {'error': error}
    return render(request,'signup.html',d)


def Logout(request):
    logout(request)
    return redirect('home')

def Userdetail(request):
    user = Student.objects.all()
    d ={'user':user}
    return render(request,'userdetail.html',d)

def Course_detail(request):
    data = Course.objects.all()
    d ={'data':data}
    return render(request,'coursedetail.html',d)

def Notice_detail(request):
    data = Notice.objects.all()
    d ={'data':data}
    return render(request,'noticedetail.html',d)

def Add_Course(request):
    error=False
    if request.method=="POST":
        c = request.POST['course']
        Course.objects.create(c_name=c)
        error=True
    d = {'error':error}
    return render(request,'add_course.html',d)


def Add_Notice(request):
    error=False
    if request.method=="POST":
        t = request.POST['title']
        d = request.POST['desc']
        Notice.objects.create(title=t,desc=d,Date1=datetime.date.today())
        error=True
    d = {'error':error}
    return render(request,'addnotice.html',d)

def View_Notice(request,pid):
    notice = Notice.objects.get(id=pid)
    d ={'notice':notice}
    return render(request,'view_notice.html',d)


def Admission_form(request):
    error=False
    user1 = ""
    sign1 = ""
    stu1 = ""
    try:
        user1 = User.objects.get(username=request.user.username)
        sign1 = Signup.objects.get(user=user1)
        stu1 = Student.objects.get(sign=sign1)
    except:
        pass
    course = Course.objects.all()
    if request.method=="POST":
        c = request.POST['course']
        i = request.FILES['img']
        f = request.POST['fname']
        m = request.POST['mname']
        b = request.POST['birth']
        n = request.POST['nation']
        g = request.POST['gen']
        ca = request.POST['cat']
        a = request.POST['add1']
        a1 = request.POST['add2']
        b10 = request.POST['10b']
        y10 = request.POST['10y']
        p10 = request.POST['10p']
        s10 = request.POST['10s']
        b12 = request.POST['12b']
        y12 = request.POST['12y']
        p12 = request.POST['12p']
        s12 = request.POST['12s']
        bg = request.POST['Gb']
        yg = request.POST['Gy']
        pg = request.POST['Gp']
        sg = request.POST['Gs']
        bpg = request.POST['pgb']
        ypg = request.POST['pgy']
        ppg = request.POST['pgp']
        spg = request.POST['pgs']
        ch = request.POST['check']
        if ch:
            user = User.objects.get(username=request.user.username)
            sign = Signup.objects.get(user=user)
            course1 = Course.objects.get(c_name=c)
            cat = Category.objects.get(cat=ca)
            stat = Status.objects.get(status="pending")
            student = Student.objects.create(status=stat,sign=sign, course=course1, cat=cat, gen=g, add1=a, add2=a1, f_name=f,
                                             m_name=m, nationality=n, birth=b, image=i)
            if b10:
                q1 = Qualification.objects.get(q_name="10th")
                Qualification_detail.objects.create(qualification=q1, student=student, year=y10, stream=s10,
                                                    percent=p10, board=b10)
            else:
                pass
            if b12:
                q2 = Qualification.objects.get(q_name="12th")
                Qualification_detail.objects.create(qualification=q2, student=student, year=y12, stream=s12,
                                                    percent=p12, board=b12)
            else:
                pass
            if bg:
                q3 = Qualification.objects.get(q_name="Graduation")
                Qualification_detail.objects.create(qualification=q3, student=student, year=yg, stream=sg, percent=pg,
                                                    board=bg)
            else:
                pass
            if bpg:
                q4 = Qualification.objects.get(q_name="Post Graduation")
                Qualification_detail.objects.create(qualification=q4, student=student, year=ypg, stream=spg,
                                                    percent=ppg, board=bpg)
            else:
                pass
            error=True
        else:
            pass

    d = {'course':course,'stu':stu1,'error':error}
    return render(request,'admission_form.html',d)

def View_detail(request,pid):
    error=""
    stat1=Status.objects.all()
    user=""
    sign=""
    stu=""
    quali=""
    if request.user.is_staff:
        stu=Student.objects.get(id=pid)
        quali = Qualification_detail.objects.filter(student=stu).all()
    if not request.user.is_staff:
        user = User.objects.get(id=pid)
        sign = Signup.objects.get(user=user)
        stu = Student.objects.get(sign=sign)
        quali = Qualification_detail.objects.filter(student=stu).all()
    quali10 = ""
    quali12 = ""
    qualig = ""
    qualipg = ""
    for i in quali:
        if i.qualification.q_name=="10th":
            q1 = Qualification.objects.get(q_name=i.qualification.q_name)
            quali10 = Qualification_detail.objects.get(student=stu,qualification=q1)
        if i.qualification.q_name=="12th":
            q2 = Qualification.objects.get(q_name=i.qualification.q_name)
            quali12 = Qualification_detail.objects.get(student=stu,qualification=q2)
        if i.qualification.q_name=="Graduation":
            q3 = Qualification.objects.get(q_name=i.qualification.q_name)
            qualig = Qualification_detail.objects.get(student=stu,qualification=q3)
        if i.qualification.q_name=="Post Graduation":
            q4 = Qualification.objects.get(q_name=i.qualification.q_name)
            qualipg = Qualification_detail.objects.get(student=stu,qualification=q4)
        if request.method=="POST":
            s = request.POST['stat']
            r = request.POST['rem']
            stat = Status.objects.get(status=s)
            stu.rem = r
            stu.status = stat
            stu.rem_date = datetime.date.today()
            stu.save()
            error="update"
    d={'user':user,'sign':sign,'error':error,'stat1':stat1,'stu':stu,'quali10':quali10,'quali12':quali12,'qualig':qualig,'qualipg':qualipg}
    return render(request,'view_detail.html',d)

def Upload_doc(request):
    error=False
    user1 = ""
    sign1 = ""
    udata =""
    stu1 = ""
    document="not"
    try:
        user1 = User.objects.get(username=request.user.username)
        sign1 = Signup.objects.get(user=user1)
        stu1 = Student.objects.get(sign=sign1)
        udata = Upload_Document.objects.get(student=stu1)
        if udata:
            document="yes"
    except:
        pass
    if request.method=="POST":
        tc = ""
        m10 = ""
        m12 = ""
        gc = ""
        pg = ""
        try:
            tc=request.FILES['tc']
        except:
            pass
        try:
            m10=request.FILES['m10']
        except:
            pass
        try:
            m12=request.FILES['m12']
        except:
            pass
        try:
            gc=request.FILES['gc']
        except:
            pass
        try:
            pg=request.FILES['pg']
        except:
            pass
        user = User.objects.get(username=request.user.username)
        sign = Signup.objects.get(user=user)
        stu = Student.objects.get(sign=sign)
        Upload_Document.objects.create(student=stu,tc=tc,mark10=m10,mark12=m12,g_certificate=gc,pg_certificate=pg)
        error=True
    d={'error':error,'stu':stu1,'document':document,'udata':udata}
    return render(request,'upload_document.html',d)


def Change_Password(request):
    error = False
    user1 = ""
    sign1 = ""
    stu1 = ""
    udata = ""
    document = "not"
    try:
        user1 = User.objects.get(username=request.user.username)
        sign1 = Signup.objects.get(user=user1)
        stu1 = Student.objects.get(sign=sign1)
        udata = Upload_Document.objects.get(student=stu1)
        if udata:
            document = "yes"
    except:
        pass
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n and c==o:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error="yes"
        else:
            error="not"
    d = {'stu': stu1,'error':error,'udata':udata,'document':document}
    return render(request,'change_password.html',d)

def View_Applicant(request,status):
    user = Student.objects.all()
    upload = Upload_Document.objects.all()
    upload1=[]
    for i in upload:
        upload1.append(i.student.sign.user.username)
    d = {'user':user,'status':status,'upload':upload1}
    return render(request,'view_application.html',d)

def view_doc(request,pid):
    user = Student.objects.get(id=pid)
    udata = Upload_Document.objects.get(student=user)
    d={'stu':user,'udata':udata}
    return render(request,'view_doc.html',d)


def delete_user(request,pid):
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('userdetail')


def delete_course(request,pid):
    course = Course.objects.get(id=pid)
    course.delete()
    return redirect('coursedetail')


def delete_notice(request,pid):
    notice = Notice.objects.get(id=pid)
    notice.delete()
    return redirect('view_notice')