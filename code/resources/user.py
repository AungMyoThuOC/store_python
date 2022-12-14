import sqlite3
from models.user import UserModel
from flask_restful import Resource, Api, reqparse

class UserRegister(Resource):
   parser = reqparse.RequestParser()
   parser.add_argument(
    'username',
    type = str,
    required = True,
    help = "This field cannot be blank." 
   )

   parser.add_argument(
    'password',
    type = str,
    required = True,
    help = "This field cannot be blank."
   )
   
   #def delete(self):
   #     date = UserRegister.parser.parse_args()

   #     user = UserModel.find_by_username(date['username'])
   #     if user:
   #         user.remove_from_db()
   #         return {"message" : "User Deleted successfully."}, 201
            
   #     return {"message" : "User doesn't exist."}

   def post(self):
        data = UserRegister.parser.parse_args()


        if(UserModel.find_by_username(data['username'])):
            return {"message" : "A user with this username already exists."}, 400
        
        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message" : "User created successfully."}, 201


    #connection = sqlite3.connect('mydatabase.db')
    #cursor = connection.cursor()

    #query = "INSERT INTO users VALUES (NULL, ?, ?)"
    #cursor.execute(query, (data['username'], data['password']))

    #connection.commit()
    #connection.close()

    #return {"message" : "User created successfully"}, 201