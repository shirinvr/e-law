from flask import Flask, render_template, request, redirect,send_file,  flash, abort, url_for
from elaw import app,db,mail
from elaw import app,db,mail
from elaw import app
from elaw.models import *
from elaw.forms import *
from flask_login import login_user, current_user, logout_user, login_required
from random import randint
import os
from PIL import Image
from flask_mail import Message
from io import BytesIO


@app.route('/about')
def about():
    return render_template("about.html")



@app.route('/map')
def map():
    return render_template("map.html")




@app.route('/meet')
def meet():
    return render_template("meet.html")




@app.route('/calender')
def calender():
    return render_template("calender.html")

@app.route('/single')
def single():
    return render_template("single.html")


@app.route('/dele')
def dele():
    return render_template("del.html")



@app.route('/nodl')
def nodl():
    return render_template("nodl.html")
    
@app.route('/del_account/<int:id>',methods = ['GET','POST'])
def del_account(id):
    d=Login.query.filter_by(id=id).first()
    return render_template("del_account.html",d=d)


@app.route('/ldel_account/<int:id>',methods = ['GET','POST'])
def ldel_account(id):
    d=Login.query.filter_by(id=id).first()
    return render_template("ldel_account.html",d=d)


@app.route('/admin_index')
def admin_index():
    return render_template("admin_index.html")





@app.route('/typography')
def typography():
    return render_template("typography.html")


@app.route('/user_index/<id>')
def user_index(id):
    d=Login.query.filter_by(usertype="lawyer",approve="Approved").all()
    return render_template("user_index.html",d=d)





@app.route('/lawyer_index/<id>')
def lawyer_index(id):
    return render_template("lawyer_index.html")





@app.route('/')
def index():
    d=Login.query.filter_by(usertype="lawyer",approve="Approved").all()
    return render_template("index.html",d=d)

@app.route('/icons')
def icons():
    return render_template("icons.html")



@app.route('/layout')
def layout():
    return render_template("layout.html")



@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/contact', methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        my_data = Contact(name=name, email=email,subject=subject,message=message,usertype="public")
        db.session.add(my_data) 
        db.session.commit()
        return redirect('/')
    else :
        return render_template("contact.html")



@app.route('/add_law', methods = ['GET','POST'])
def add_law():
    if request.method == 'POST':
        law = request.form['law']
        details = request.form['details']
        my_data = Law(law=law, details=details)
        db.session.add(my_data) 
        db.session.commit()
        return redirect('/manage_laws')
    else :
        return render_template("add_law.html")

@app.route('/lawyer_add_case', methods = ['GET','POST'])
def lawyer_add_case():
    if request.method == 'POST':
        lid = request.form['lid']
        case = request.form['case']
        desc = request.form['desc']
       
        my_data = Case(lid=lid,case=case, desc=desc)
        db.session.add(my_data) 
        db.session.commit()
        return redirect('/manage_case')
    else :
        return render_template("lawyer_add_case.html")




@app.route('/send_noti/<id>', methods = ['GET','POST'])
def send_noti(id):
    d = BookLawyer.query.get_or_404(id)
    if request.method == 'POST':
        message = request.form['message']
        msg_sendmail(d.uemail,message)
        d="Notification Send Successfully!"
        return render_template("send_noti.html",d=d)

    else:
        return render_template("send_noti.html")



def msg_sendmail(uemail,message):
    
    msg = Message('Case Notification',
                  recipients=[uemail])
    msg.body = f'''{message} '''
    mail.send(msg)


@app.route('/add_court', methods = ['GET','POST'])
def add_court():
    if request.method == 'POST':
        court = request.form['court']
        jury = request.form['jury']
        address = request.form['address']
        location = request.form['location']
        time = request.form['time']

        my_data = Court(court=court, jury=jury,address=address,location=location,time=time)
        db.session.add(my_data) 
        db.session.commit()
        return redirect('/manage_courts')
    else :
        return render_template("add_court.html")

@app.route('/edit_court/<int:id>', methods = ['GET','POST'])
def edit_court(id):
    d = Court.query.get_or_404(id)
    if request.method == 'POST':
        d.court = request.form['court']
        d.jury = request.form['jury']
        d.address = request.form['address']
        d.location = request.form['location']
        d.time = request.form['time']
        db.session.commit()
        return redirect('/manage_courts')
    else :
        return render_template("edit_court.html",d=d)





@app.route('/edit_userpic/<int:id>', methods = ['GET','POST'])
def edit_userpic(id):
    d = Login.query.get_or_404(id)
    if request.method == 'POST':
        img=request.files['image']
        pic_file = save_picture(img)
        view = pic_file
        print(view) 
        d.image=view
        db.session.commit()
        return redirect('/user_view_profile/'+str(d.id))
    else :
        return render_template("edit_userpic.html",d=d)



@app.route('/edit_lawyerpic/<int:id>', methods = ['GET','POST'])
def edit_lawyerpic(id):
    d = Login.query.get_or_404(id)
    if request.method == 'POST':
        img=request.files['image']
        pic_file = save_picture(img)
        view = pic_file
        print(view) 
        d.image=view
        db.session.commit()
        return redirect('/user_view_profile/'+str(d.id))
    else :
        return render_template("edit_lawyerpic.html",d=d)


@app.route('/edit_userprofile/<int:id>', methods = ['GET','POST'])
def edit_userprofile(id):
    d = Login.query.get_or_404(id)
    if request.method == 'POST':
        d.name = request.form['name']
        d.contact = request.form['contact']
        d.username = request.form['username']
        d.address = request.form['address']
        d.place = request.form['place']
        d.password = request.form['password']
        # img=request.files['image']
        # pic_file = save_picture(img)
        # view = pic_file
        # print(view) 
        # d.image=view
        db.session.commit()
        return redirect('/user_view_profile/'+str(d.id))
    else :
        return render_template("edit_userprofile.html",d=d)




@app.route('/edit_lawyerprofile/<int:id>', methods = ['GET','POST'])
def edit_lawyerprofile(id):
    d = Login.query.get_or_404(id)
    m=Court.query.all()
    if request.method == 'POST':
        d.name = request.form['name']
        d.contact = request.form['contact']
        d.username = request.form['username']
        d.qualification = request.form['qualification']
        d.court = request.form['court']
        d.type = request.form['type']
        d.password = request.form['password']
        d.barcodeid = request.form['barcodeid']
        # img=request.files['image']
        # pic_file = save_picture(img)
        # view = pic_file
        # print(view) 
        # d.image=view
        db.session.commit()
        return redirect('/lawyer_view_profile/'+str(d.id))
    else :
        return render_template("edit_lawyerprofile.html",d=d,m=m)


@app.route('/edit_law/<int:id>', methods = ['GET','POST'])
def edit_law(id):
    d = Law.query.get_or_404(id)
    if request.method == 'POST':
        d.law = request.form['law']
        d.details = request.form['details']
        db.session.commit()
        return redirect('/manage_laws')
    else :
        return render_template("edit_law.html",d=d)




@app.route('/delete_account/<int:id>', methods = ['GET','POST'])
@login_required
def delete_account(id):
    delet = Login.query.get_or_404(id)

    try:
        db.session.delete(delet)
        db.session.commit()
        return redirect('/dele')
    except:
        return redirect('/nodl')



@app.route('/delete_law/<int:id>', methods = ['GET','POST'])
@login_required
def delete_law(id):
    delet = Law.query.get_or_404(id)

    try:
        db.session.delete(delet)
        db.session.commit()
        return redirect('/manage_laws')
    except:
        return 'There was a problem deleting that task'

@app.route('/delete_court/<int:id>', methods = ['GET','POST'])
@login_required
def delete_court(id):
    delet = Court.query.get_or_404(id)

    try:
        db.session.delete(delet)
        db.session.commit()
        return redirect('/manage_courts')
    except:
        return 'There was a problem deleting that task'



@app.route('/delete_case/<int:id>', methods = ['GET','POST'])
@login_required
def delete_case(id):
    delet = Case.query.get_or_404(id)

    try:
        db.session.delete(delet)
        db.session.commit()
        return redirect('/manage_case')
    except:
        return 'There was a problem deleting that task'



@app.route('/login', methods=["GET","POST"])
def login():
     if request.method=="POST":
         username=request.form['username']
         password=request.form['password']
         admin = Login.query.filter_by(username=username, password=password,usertype= 'admin').first()
         lawyer=Login.query.filter_by(username=username,password=password, usertype= 'lawyer',approve='Approved').first()
         user=Login.query.filter_by(username=username,password=password, usertype= 'user').first()
         if admin:
             login_user(admin)
             next_page = request.args.get('next')
             return redirect(next_page) if next_page else redirect('/admin_index') 
             
         elif lawyer:
             login_user(lawyer)
             next_page = request.args.get('next')
             return redirect(next_page) if next_page else redirect('/lawyer_index/'+str(lawyer.id))
         
         elif user:
             login_user(user)
             next_page = request.args.get('next')
             return redirect(next_page) if next_page else redirect('/user_index/'+str(user.id))  

         else:
             d="Invalid Username or Password!"
             return render_template("login.html",d=d)

     return render_template("login.html")








@app.route('/user_register',methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        password = request.form['password']
        address = request.form['address']
        place = request.form['place']
        img=request.files['image']
        pic_file = save_picture(img)
        view = pic_file
        print(view)  

        my_data =Login(name=name,username=email,contact=contact,image=view,password=password,address=address,place=place,usertype="user")
        db.session.add(my_data) 
        db.session.commit()
        flash("Registered successfully! Please Login..")
        return redirect('/login')
        
    else :
        return render_template("user_register.html")




@app.route('/lawyer_register',methods=['GET', 'POST'])
def lawyer_register():
    d=Court.query.all()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        password = request.form['password']
        barcodeid = request.form['barcodeid']
        img=request.files['image']
        pic_file = save_picture(img)
        view = pic_file
        print(view)  

        qualification = request.form['qualification']
        type = request.form['type']
        court = request.form['court']
        my_data = Login(name=name,username=email,contact=contact,password=password,image=view,usertype="lawyer",approve="Approve",reject="Reject",barcodeid=barcodeid,qualification=qualification,type=type,court=court)
        try:

            db.session.add(my_data) 
            db.session.commit()
            sendmail(email)
        except:
            j="Sorry, Your Registeration Failed.Please Register with Valid Details."
            return render_template("lawyer_register.html",j=j)
            
      
        m="Your Registeration will be confirmed soon.."
        return render_template("lawyer_register.html",d=d,m=m)
        
    else :
        m="Your Registeration will be confirmed soon.."
        return render_template("lawyer_register.html",d=d)

def save_picture(form_picture):
    random_hex = random_with_N_digits(14)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = str(random_hex) + f_ext
    picture_path = os.path.join(app.root_path, 'static/pics', picture_fn)
    
    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn



def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def sendmail(email):
    
    msg = Message('Registeration Successfull',
                  recipients=[email])
    msg.body = f''' Congratulations , Your  Registeration  is completed successfully... Wait for Confirmation.. '''
    mail.send(msg)



@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect('/')



@app.route('/approve/<int:id>')
def approve(id):
    c= Login.query.get_or_404(id)
    c.approve = "Approved"
    c.reject="Reject"
    db.session.commit()
    a_sendmail(c.username)
    return redirect('/admin_view_lawyers')

@app.route('/lawyer_approve/<int:id>')
def lawyer_approve(id):
    c= BookLawyer.query.get_or_404(id)
    c.status = "Approved"
    c.approve="Approved"
    c.reject="Reject"
    c.pstatus="Make Payment"
    db.session.commit()
    law_sendmail(c.uemail)
    return redirect('/lawyer_view_bookings/'+str(current_user.id))


@app.route('/lawyer_reject/<int:id>')
def lawyer_reject(id):
    c= BookLawyer.query.get_or_404(id)
    c.status = "Rejected"
    c.approve="Approve"
    c.reject="Rejected"
    db.session.commit()
    rlaw_sendmail(c.uemail)
    return redirect('/lawyer_view_bookings/'+str(current_user.id))




def law_sendmail(uemail):
    
    msg = Message('Approved Successfully',
                  recipients=[uemail])
    msg.body = f''' Congratulations , Your  Lawyer Booking  is approved successfully... Login to make payment for further procedures '''
    mail.send(msg)


def rlaw_sendmail(uemail):
    
    msg = Message('Booking Rejected',
                  recipients=[uemail])
    msg.body = f''' Sorry , Your  Lawyer Booking  is rejected . '''
    mail.send(msg)


@app.route('/payment/<int:id>',methods=["GET","POST"])
def payment(id):
    c= BookLawyer.query.get_or_404(id)
    if request.method == 'POST':
        c.cardno =  request.form['cardno']
        c.month =  request.form['month']
        c.year =  request.form['year']
        c.cvv =  request.form['cvv']
        c.amount =  request.form['amount']
        c.pstatus="Paid"
        db.session.commit()
        p_sendmail(c.uemail)
        lp_sendmail(c.lemail)
        return redirect('/user_view_payments/'+str(current_user.id))
    else:
        return render_template('payment.html',c=c)



@app.route('/reject/<int:id>')
def reject(id):
    c= Login.query.get_or_404(id)
    c.reject = 'Rejected'
    c.approve="Approve"
    db.session.commit()
    r_sendmail(c.username)
    return redirect('/admin_view_lawyers')



def a_sendmail(username):
    
    msg = Message('Approved Successfully',
                  recipients=[username])
    msg.body = f''' Congratulations , Your  Registeration is approved successfully... Now You can login using username and password '''
    mail.send(msg)

def r_sendmail(username):
  
    msg = Message('Registeration Rejected',
                  recipients=[username])
    msg.body = f''' Sorry , Your  Registeration is rejected. '''
    mail.send(msg)


def p_sendmail(uemail):
  
    msg = Message('Payment Successful',
                  recipients=[uemail])
    msg.body = f''' Your Payment is Successful '''
    mail.send(msg)



def lp_sendmail(lemail):
  
    msg = Message('Payment Received',
                  recipients=[lemail])
    msg.body = f''' Login to view more details '''
    mail.send(msg)


@login_required
@app.route('/admin_view_lawyers',methods=["GET","POST"])
def admin_view_lawyers():
    obj = Login.query.filter_by(usertype="lawyer").all()
    return render_template("admin_view_lawyers.html",obj=obj)

@login_required
@app.route('/manage_laws',methods=["GET","POST"])
def manage_laws():
    obj = Law.query.all()
    return render_template("manage_laws.html",obj=obj)


@login_required
@app.route('/user_view_laws',methods=["GET","POST"])
def user_view_laws():
    obj = Law.query.all()
    return render_template("user_view_laws.html",obj=obj)


@login_required
@app.route('/user_view_courts',methods=["GET","POST"])
def user_view_courts():
    obj = Court.query.all()
    return render_template("user_view_courts.html",obj=obj)



@login_required
@app.route('/lawyer_view_laws',methods=["GET","POST"])
def lawyer_view_laws():
    obj = Law.query.all()
    return render_template("lawyer_view_laws.html",obj=obj)


@login_required
@app.route('/lawyer_view_courts',methods=["GET","POST"])
def lawyer_view_courts():
    obj = Court.query.all()
    return render_template("lawyer_view_courts.html",obj=obj)


@login_required
@app.route('/manage_case',methods=["GET","POST"])
def manage_case():
    obj = Case.query.all()
    return render_template("manage_case.html",obj=obj)



@login_required
@app.route('/manage_courts',methods=["GET","POST"])
def manage_courts():
    obj = Court.query.all()
    return render_template("manage_courts.html",obj=obj)

@login_required
@app.route('/user_view_lawyers',methods=["GET","POST"])
def user_view_lawyers():
    search=request.args.get('search')
    if search:
        obj=Login.query.filter(Login.name.contains(search)|Login.court.contains(search)|Login.type.contains(search)|Login.barcodeid.contains(search)|Login.qualification.contains(search) & Login.usertype.contains("lawyer") & Login.approve.contains("Approved"))
    else:
        obj=Login.query.filter_by(usertype="lawyer",approve="Approved").all()
    
    return render_template("user_view_lawyers.html",obj=obj)



@login_required
@app.route('/user_view_history/<id>',methods=["GET","POST"])
def user_view_history(id):
    obj = Case.query.filter_by(lid=id).all()
    return render_template("user_view_history.html",obj=obj)


@login_required
@app.route('/admin_view_users',methods=["GET","POST"])
def admin_view_users():
    obj = Login.query.filter_by(usertype="user").all()
    return render_template("admin_view_users.html",obj=obj)






@login_required
@app.route('/admin_view_feedbacks',methods=["GET","POST"])
def admin_view_feedbacks():
    obj = Contact.query.all()
    return render_template("admin_view_feedbacks.html",obj=obj)




@login_required
@app.route('/user_view_bookings/<int:id>',methods=["GET","POST"])
def user_view_bookings(id):
    obj = BookLawyer.query.filter_by(uid=id).all()
    return render_template("user_view_bookings.html",obj=obj)




@login_required
@app.route('/lawyer_view_bookings/<int:id>',methods=["GET","POST"])
def lawyer_view_bookings(id):
    obj = BookLawyer.query.filter_by(lid=id).all()
    return render_template("lawyer_view_bookings.html",obj=obj)

@login_required
@app.route('/lawyer_view_payments/<int:id>',methods=["GET","POST"])
def lawyer_view_payments(id):
    obj = BookLawyer.query.filter_by(lid=id,pstatus="Paid").all()
    return render_template("lawyer_view_payments.html",obj=obj)




@login_required
@app.route('/admin_view_bookings',methods=["GET","POST"])
def admin_view_bookings():
    obj = BookLawyer.query.filter_by(pstatus="Paid").all()
    return render_template("admin_view_bookings.html",obj=obj)




@login_required
@app.route('/user_view_payments/<int:id>',methods=["GET","POST"])
def user_view_payments(id):
    obj = BookLawyer.query.filter_by(uid=id,pstatus="Paid").all()
    return render_template("user_view_payments.html",obj=obj)






@app.route('/lawyer_view_profile/<int:id>',methods=["GET","POST"])
@login_required
def lawyer_view_profile(id):
    d = Login.query.get_or_404(id)
    return render_template("lawyer_view_profile.html",d=d)




@app.route('/user_view_lawyer_profile/<int:id>',methods=["GET","POST"])
@login_required
def user_view_lawyer_profile(id):
    d = Login.query.get_or_404(id)
    return render_template("user_view_lawyer_profile.html",d=d)




@app.route('/user_view_profile/<int:id>',methods=["GET","POST"])
@login_required
def user_view_profile(id):
    d = Login.query.get_or_404(id)
    return render_template("user_view_profile.html",d=d)




@login_required
@app.route('/user_contact/<id>', methods = ['GET','POST'])
def user_contact(id):
    d=Login.query.filter_by(id=id).first()
 
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        my_data = Contact(name=name, email=email,subject=subject,message=message,usertype="user")
        db.session.add(my_data) 
        db.session.commit()
   
        return redirect('/user_index/'+str(current_user.id))
    else :
        return render_template("user_contact.html",d=d)




@login_required
@app.route('/lawyer_contact/<id>', methods = ['GET','POST'])
def lawyer_contact(id):
    d=Login.query.filter_by(id=id).first()
 
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        my_data = Contact(name=name, email=email,contact=contact,subject=subject,message=message,usertype="lawyer")
        db.session.add(my_data) 
        db.session.commit()
   
        return redirect('/lawyer_index/'+str(current_user.id))
    else :
        return render_template("lawyer_contact.html",d=d)




@app.route('/book_lawyer/<int:uid>/<int:lid>',methods=['GET', 'POST'])
def book_lawyer(uid,lid):
    u=Login.query.filter_by(id=uid).first()
    l=Login.query.filter_by(id=lid).first()
    if request.method == 'POST':
        uid = request.form['uid']
        lid = request.form['lid']
        uname = request.form['uname']
        lname = request.form['lname']
        uemail = request.form['uemail']
        lemail = request.form['lemail']
        ucontact = request.form['ucontact']
        lcontact = request.form['lcontact']
        address = request.form['address']
        place = request.form['place']
        case = request.form['case']
        buk_date=request.form['buk_date']
        file = request.files['file']
        status="Approve"
        my_data = BookLawyer(uid=uid,lid=lid,uname=uname,buk_date=buk_date,filename=file.filename, data=file.read(),lname=lname,uemail=uemail,lemail=lemail,ucontact=ucontact,lcontact=lcontact,address=address,place=place,case=case,pstatus="Waiting For Confirmation",status=status,approve="Approve",reject="Reject")
        db.session.add(my_data) 
        db.session.commit()
        buk_sendmail(u.username)
        return redirect('/user_view_bookings/'+str(current_user.id))
        
    else :
        return render_template("book_lawyer.html",u=u,l=l)


@app.route('/download/<id>')
def download(id):
    upload = BookLawyer.query.filter_by(id=id).first()
    return send_file(BytesIO(upload.data), attachment_filename=upload.filename, as_attachment=True) 


def buk_sendmail(username):
  
    msg = Message('Booking Successful',
                  recipients=[username])
    msg.body = f''' Your Lawyer Booking is successful... Please wait for the Confirmation '''
    mail.send(msg)