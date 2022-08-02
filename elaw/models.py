from enum import unique
from elaw import db,app,login_manager
from flask_login import UserMixin
from flask_table import Table, Col, LinkCol
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(id):
    return Login.query.get(int(id))



class Login(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80), nullable=False)
    usertype = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(200))
    contact = db.Column(db.String(200))
    approve = db.Column(db.String(200))
    reject = db.Column(db.String(200))
    status = db.Column(db.String(200))
    address = db.Column(db.String(200))
    place = db.Column(db.String(200))
    type = db.Column(db.String(200))
    court = db.Column(db.String(200))
    barcodeid = db.Column(db.String(200))
    qualification = db.Column(db.String(200))
    image = db.Column(db.String(20), nullable=False, default='default.jpg')







class Contact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    email= db.Column(db.VARCHAR)
    subject = db.Column(db.String(200))
    message= db.Column(db.String(200))
    usertype = db.Column(db.String(80), nullable=False)



class Law(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    law = db.Column(db.String(200))
    details= db.Column(db.VARCHAR)



class Court(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    court = db.Column(db.String(200))
    jury = db.Column(db.String(200))
    address= db.Column(db.String(200))
    location=db.Column(db.String(200))
    time=db.Column(db.String(200))



class Case(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    lid = db.Column(db.String(200))
    case = db.Column(db.String(200))
    desc = db.Column(db.String(200))
 






class BookLawyer(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(80))
    lid = db.Column(db.String(80), nullable=False)
    uname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(200))
    ucontact = db.Column(db.String(200))
    lcontact = db.Column(db.String(200))
    uemail = db.Column(db.String(200))
    lemail = db.Column(db.String(200))
    address = db.Column(db.String(200))
    place = db.Column(db.String(200))
    pstatus=db.Column(db.String(200))
    status=db.Column(db.String(200))
    approve = db.Column(db.String(200))
    reject = db.Column(db.String(200))
    case = db.Column(db.String(200))
    cardno = db.Column(db.String(200))
    cvv = db.Column(db.String(200))
    month = db.Column(db.String(200))
    year = db.Column(db.String(200))
    amount = db.Column(db.String(200))
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    buk_date = db.Column(db.String(200))
    noti_msg=db.Column(db.String(200))
    st=db.Column(db.String(200))

