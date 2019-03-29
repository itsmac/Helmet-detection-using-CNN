import requests
import base64
import json
import urllib
import config
import db
def licence_plate_recognition():
    IMAGE_PATH = r'E:\ProjectCollege\Images\Framess\framecapv.jpg'
    SECRET_KEY = config.SECRET_KEY

    with open(IMAGE_PATH, 'rb') as image_file:
        img_base64 = base64.b64encode(image_file.read())

    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=in&secret_key=%s' % (SECRET_KEY)
    r = requests.post(url, data = img_base64)
    json_response = r.json()
    plate_detail = json_response['results'][-1]['plate']
    result = db.database_values(plate_detail)
    print("License Plate number is " + plate_detail )
    if result is "Success":
        print("Successfully stored in the database")
    else:
        print("Not Stored in the database")
    print("Want to display the entire database Y/n?")
    ans = input()
    if ans in ['y','Y']:
        db.display()
    else:
        return ""
