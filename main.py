import firebase_admin
from firebase_admin import credentials, db
from firebase_admin.exceptions import PermissionDeniedError
from urllib.error import URLError
from urllib.request import urlopen
import json
import time
import datetime

#this is an indicator variable whether program has an error.
has_error = False

#access to firebase and raising it by specific database URL 
key = credentials.Certificate("firebase-config.json")
firebase_admin.initialize_app(key, {
        'databaseURL' : 'https://muhendisonur.firebaseio.com/'
    })

#this function gets json data from an URL and returns it as dict data type
def json_deserialize_url(url):
    try:
        #getting json from URL
        json_file_url = url
        json_file_response = urlopen(json_file_url)

        #deserializing it to use in python environment
        json_deserialized = json.load(json_file_response)
    except Exception as e:
        print("[ERROR!] JSON Parsing(Deserialazing) Hatası!")    
    return json_deserialized

#infinity loop to run the program periodically
while True:
    try:
        json_data = json_deserialize_url("http://localhost/dashboard/sample_input.json")
    except URLError as e:
        print("[Error!] JSON bilgilerini erişmek için girdiğiniz URL geçersiz veya erişilemiyor!")
        has_error = True

    #updating the database with new data (firebase operation)
    try:
        db.reference('regions').set(json_data['regions'])
    except PermissionDeniedError as e:
        print("[ERROR!] Girdiğiniz veritabanı bilgileri(url, access key vb.) hatalı veya geçersiz!")
        has_error = True
    except NameError as e: #if an error occured on defining json_data variable, NameError will be occured on this section's try block
        print("[ERROR!] JSON bilgilerini erişmek için girdiğiniz URL geçersiz olduğu için gerekli değişken tanımlanamadı!")

    #if program has some error, it prints this section
    if(has_error):
        print(f"[DANGER] Program has been executed with some error at {datetime.datetime.now()}\n")
        has_error = False
    else: #otherwise it prints this section
        print(f"[OK] Program has been executed succesfully at {datetime.datetime.now()}\n")

    #1 minute delay
    time.sleep(60)
