import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancesystem-api-default-rtdb.asia-southeast1.firebasedatabase.app/" # Replace this URL with your RT-DB Reference URL.
})

ref = db.reference('Students')
data = {
    "3457":
        {
            "name": "Dr. APJ Abdul Kalam",
            "major": "Physics",
            "Semester": 6,
            "total_attendance": 100,
            "standing": "g",
            "last_attended_time": "2023-01-05 12:07:34"
        },
    "7888":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "Semester":6,
            "total_attendance":90,
            "standing":"g",
            "last_attended_time":"2023-01-05 12:07:34"
        },
}

for key,value in data.items():
    ref.child(key).set(value)
