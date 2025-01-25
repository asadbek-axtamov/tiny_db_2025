from tinydb import TinyDB
db = TinyDB('db.json')

db.insert(
    {
        'name': "Asadbek",
        'age': 20,
        'occupation': "Engeener"
    }
)

db.insert(
    {
        'name': "Husan",
        'age': 45,
        'occupation': "Doctor" 
    }
)