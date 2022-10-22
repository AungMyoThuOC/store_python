from models.user import UserModel


#userid_mapping = {user.id : user for user in users}

def authenticate (username, password):
    user = UserModel.find_by_username(username)
    # user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_userid(user_id)