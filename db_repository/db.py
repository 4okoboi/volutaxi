import pyrebase

firebaseConfig = {'apiKey': "AIzaSyCWSPbFxEGKCnQNjMY_8HhgbjmqDTluQ0o",
                  'authDomain': "hack-8645c.firebaseapp.com",
                  'databaseURL': "https://hack-8645c-default-rtdb.asia-southeast1.firebasedatabase.app",
                  'projectId': "hack-8645c",
                  'storageBucket': "hack-8645c.appspot.com",
                  'messagingSenderId': "463099006706",
                  'appId': "1:463099006706:web:36c5ad0612c2976adaca6b"}

firebase = pyrebase.initialize_app(firebaseConfig)

database = firebase.database()
db_auth = firebase.auth()

# user = db_auth.create_user_with_email_and_password("afdsasdf@gmail.com", "12345678")
# user_info = {"b_day": "11.02.1223", "name": "Артем", "number": "+7122391392", "patronymic": "Арсеньевич",
#              "secondName": "Улесов",
#              "userId": user['localId'], "username": "artulleeee"}
# result = database.child("Users").child(user['localId']).push(user_info)

# user = db_auth.create_user_with_email_and_password("qwerty23456@gmail.com", "12345678")
# print(user)
# result = database.child("Users").child("GKN590DjpMdbrttRM").push("{}")
# print(result)
