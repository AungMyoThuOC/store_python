import sqlite3
from db import db

class UserModel(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    
    def __init__(self, username, password): 
        #self.id = _id
        self.username = username
        self.password = password

        #connection = sqlite3.connect('mydatabase.db')
        #cursor = connection.cursor()

        #query = "Select * fROM user where username = ?"
        #result = cursor.execute(query (username))
        #row = result.fetchone()
        #print(row)
        #if row:
         #   user = cls(row[0], row[1], row[2])
        #else:
       #     user = None
    
        #connection.close()
       # return user

        #connection = sqlite3.connect('mydatabase.db')
        #cursor = connection.cursor()

        #query = "Select * fROM user where userid = ?"
        #result = cursor.execute(query (userid))
        #row = result.fetchone()
        #print(row)
        #if row:
        #    user = cls(row)
        #else:
        #    user = None
        
        #connection.close()
        #return user

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_userid(cls, _id):
        return cls.query.filter_by(id=_id).first()