import datetime

from front.components.popup import Popup
from .Roles import *
import hashlib
from back.db import db
class User():
    num =3

    def __init__(self,login,role=None,id=None,date=None):
        self.login = login

        if role is None:
            self.role = Roles.loger
        else:
            self.role = role

        if date is None:
            self.date = datetime.datetime.now().strftime("%d/%m/%Y")
        else:
            self.date = date

        if id is not None:
            self.encode(id)
        else:
            self.id = None
        self.solved = False
        self.task = None
        self.count = 0


    def add_user(self):
        try:
           res = db.add_user(self.login,self.id,self.role,self.date)
           if res:
               self.dif = db.get_diff(self.login)
           return res
        except:
            Popup.error()
            return True

    def exists(self,id):
        try:
           if db.user_exists_l(self.login):
                self.date = db.get_date(self.login)
                self.encode(id)
                if self.id == db.get_vid_id(self.login):
                    res = db.get_task(self.login)
                    self.dif = db.get_diff(self.login)
                    self.task = res
                    return True
                return False
        except:
            Popup.error()


    def get_task(self):
        self.solved = False
        if self.task is None:
            res = db.get_task(self.login)
        else:
            res = db.get_task(self.login,self.task)
        self.task = res

    def update_dif(self,check):
        tdif = db.get_task_dif(self.task)
        if check:
            self.count += 0.3 + tdif * 0.05
        else:
            self.count -= 0.3 + tdif * 0.1
        if self.count <= -1:
            self.dif -= 0.5
            self.dif = max(min(db.get_maxtask()[0], self.dif), db.get_mintask()[0])
            self.count = 0.2
            db.update_task(self.login, round(self.dif))
        elif self.count >= 1:
            self.dif +=1
            self.dif = max(min(db.get_maxtask()[0], self.dif), db.get_mintask()[0])
            self.count = 0.2
            db.update_task(self.login, round(self.dif))


    def encode(self,id):
        sha_256 = hashlib.new('sha256')
        salt_check = id + self.date + "|-?|" + self.login + "?W#!!?|" + "".join(
            [str(ord(x) * User.num) + "?!" for x in self.login])
        sha_256.update(salt_check.encode())
        self.id = sha_256.hexdigest()

    def update(self):
        try:
            db.update_vid(self.login,self.id)
        except:
            Popup.error()

    def get_role(self):
        return self.role
    def set_role(self,role):
        if isinstance(role,Roles):
            self.role = role
        else:
            self.role = Roles(role)

    def get_login(self):
        return self.login

    def set_login(self, login):
        self.login = login

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

