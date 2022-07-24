import firebase_admin
from firebase_admin import credentials,db,firestore

# Fetch the service account key JSON file contents
cred = credentials.Certificate(r'D:\VSCODE\MyPython\connection_test\env\nutproject0405-firebase-adminsdk-104pf-ece45cd371.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://nutproject0405.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
# ref = db.reference('/')
# ref.push({
#     'x':10,
#     'y':100
# })
# data = {"name":"bill","address":["Maxico","USAn"]}
# ref.child('data2').set(data)
# ref.child('data1').update({"name":"james"})
# print(ref.get())
# print(ref.get())
# for i in ref.child('data1').get():
#     print(i)

ft = firestore.client()

# =========auto gen id======
# ft.collction('demo').add({"name":"tom","age":10})

# ===== append data===========
# ft.collection('demo').document("data2").set({"name":"tom","age":12}, merge = True)
# ft.collection('demo').document("data3").set({"name":"jack","age":13})

# result = ft.collection('demo').document("data1").get()
# if result.exists:
#     print(result.to_dict())

# docs = ft.collection('demo').get()
# for doc in docs:
#     print(doc.to_dict())

# =========== query =====================
# docs = ft.collection('demo').where("age",">",10).get()
# docs = ft.collection('demo').where("age","array_contains",10).get()
docs = ft.collection('demo').where("age","in",[10,11,12]).get()
for doc in docs:
    print(doc.to_dict())