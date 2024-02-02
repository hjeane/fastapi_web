from pymongo import MongoClient

# 방법1 - URI
mongodb_URI = "mongodb+srv://root:1234@jeane.cgtytvj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongodb_URI)

# 방법2 - HOST, PORT
#client = MongoClient(host='localhost', port=27017)
db = client.ubion 
data = db.users
# print(client.list_database_names())

data.insert_one({
    'username':'park',
    'password':'5678'
})

# cursor = data.find({'username':'yang'})
# # for i in cursor:
# print(list(cursor))

cursor_1 = data.find_one({'email':'1@naver.com'})
if cursor_1 == None:
    print('ssssssss')
else:
    print(cursor_1)
