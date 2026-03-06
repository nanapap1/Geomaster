import sqlite3
import random


class GeoDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
    def user_exists(self, user_id):
        result = self.cursor.execute("SELECT `ID` FROM `USERS` WHERE `VID` = ?", (user_id,))
        return bool(len(result.fetchall()))
    def user_exists_l(self, user_login):
        result = self.cursor.execute("SELECT `ID` FROM `USERS` WHERE `LOGIN` = ?", (user_login,))
        return bool(len(result.fetchall()))
    def get_len(self):
        result = self.cursor.execute("SELECT `ID` FROM `ID_INFO`")
        z = result.fetchall()
        return len(z)
    def get_user_id(self, user_id):
        result = self.cursor.execute("SELECT `ID` FROM `USERS` WHERE `VID` = ?", (user_id,))
        return result.fetchone()[0]
    def get_vid_id(self, login):
        result = self.cursor.execute("SELECT `VID` FROM `USERS` WHERE `LOGIN` = ?", (login,))
        return result.fetchone()[0]
    def get_date(self, login):
        result = self.cursor.execute("SELECT `DATE` FROM `USERS` WHERE `LOGIN` = ?", (login,))
        return result.fetchone()[0]
    def get_diff(self,login):
        result = self.cursor.execute("SELECT `DIF` FROM `USERS` WHERE `LOGIN` = ?", (login,))
        return result.fetchone()[0]
    def get_task_dif(self,id):
        result = self.cursor.execute("SELECT `DIF` FROM `TDIF` WHERE `ID` = ?", (id,))
        return result.fetchone()[0]
    def get_task(self, login,task=None):
        result = self.cursor.execute("SELECT `DIF` FROM `USERS` WHERE `LOGIN` = ?", (login,))
        result = result.fetchone()[0]
        res = self.get_difff()
        filtered_list = list(filter(lambda t: result-2<= t[1] <= result+2 and t[0]!=task, res))
        return random.choice(filtered_list)[0]
    def update_task(self, login,dif):
        self.cursor.execute("UPDATE `USERS` SET `DIF` = ? WHERE `LOGIN` = ?", (dif, login,))
        return self.conn.commit()
    def add_user(self, login,vid,role,date):
        if not(self.user_exists_l(login)):
            self.cursor.execute("INSERT INTO `USERS` (`LOGIN`,`VID`,`ROLE`,`DATE`) VALUES (?,?,?,?)", (login,vid,role.name,date))
            self.conn.commit()
            return True
        return False
    def write_task(self,body,resid,endid):
        self.cursor.execute("INSERT INTO `TASK` (`BODY`,`RESID`,`ENDID`) VALUES (?,?,?)", (body,resid,endid))
        return self.conn.commit()
    def update_vid(self,login,id):
        self.cursor.execute("UPDATE `USERS` SET `VID` = ? WHERE `LOGIN` = ?", (id,login,))
        return self.conn.commit()
    def write_res(self,func,quantity,more=None):
        if more is not None:
            self.cursor.execute("INSERT INTO `RESOURSE` (`FUNC`,`QUANTITY`,`MORE`) VALUES (?,?,?)", (func,quantity,more))
        else:
            self.cursor.execute("INSERT INTO `RESOURSE` (`FUNC`,`QUANTITY`) VALUES (?,?)", (func,quantity))
        return self.conn.commit()
    def write_end(self,func,quantity):
        self.cursor.execute("INSERT INTO `END` (`FUNCTION`,`QUANTITY`) VALUES (?,?)", (func,quantity))
        return self.conn.commit()
    def info_task(self,id):
        result = self.cursor.execute("SELECT `BODY`,`RESID`,`ENDID` FROM `TASK` WHERE `ID` = ?",(id,))
        res = result.fetchall()
        if res == [] or res == None:
            return False
        body,resid,endid = res[0]
        return body,resid,endid

    def add_dif(self,id,dif):
        result = self.cursor.execute("SELECT `DIF` FROM `TDIF` WHERE `ID` = ?",(id,))
        res = result.fetchall()
        if len(res)==0:
            self.cursor.execute("INSERT INTO `TDIF` (`ID`,`DIF`) VALUES (?,?)",(id,dif))
            return self.conn.commit()
        return

    def get_difff(self):
        result = self.cursor.execute("SELECT `ID`,`DIF` FROM `TDIF`")
        res = result.fetchall()
        return res

    def get_maxtask(self):
        result = self.cursor.execute("SELECT MAX(`DIF`) FROM `TDIF`")
        return result.fetchall()[0]
    def get_mintask(self):
        result = self.cursor.execute("SELECT MIN(`DIF`) FROM `TDIF`")
        return result.fetchall()[0]

    def get_res(self,id):
        result = self.cursor.execute("SELECT `FUNC`,`QUANTITY`,`MORE` FROM `RESOURSE` WHERE `ID` = ?", (id,))
        res = result.fetchall()
        if res == [] or res == None:
            return False
        func, quan, more = res[0]
        return func, quan, more
    def get_end(self,id):
        result = self.cursor.execute("SELECT `FUNCTION`,`QUANTITY` FROM `END` WHERE `ID` = ?", (id,))
        res = result.fetchall()
        if res == [] or res == None:
            return False
        func, quan = res[0]
        return func, quan
    def close(self):
       self.conn.close()