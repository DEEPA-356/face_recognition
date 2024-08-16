Step 01: Make sure you have Python 3.11 and PyCharm Community or Professional IDE are installed in your system.
Step 02: Extract the contents of this zip file and open the "face_recognition_attendance_system-master" folder as a PyCharm Project by right click on it and selecting "Open as a PyCharm Project".
Step 03: On a browser, go to firebase.google.com and click on "Get Started" to create a Firebase account. Follow the on screen instructions to do so.
Step 04: On the Firebase Console, Create a New Firebase Project. Make sure to name the Firebase Project URL-Friendly.
Step 05: On the Project Overview page, go to the project settings and navigate to the "Service accounts" section.
Step 06: Under "Firebase Admin SDK", Choose "Python" as the "Admin SDK configuration snippet" and click on the "Generate new private key" button. A PRIVATE KEY will be downloaded in the JSON file format.
Step 07: Open the downloaded JSON file using a text editor and copy all of its content. In the project folder, Open the "ServiceAccountKey.json" file using a Text Editor or Code Editor and over-paste / (press Ctrl+A then, Ctrl+V) the copied content. save the file.
Step 08: In the Firebase Project Overview page, In the "Product categories" pane, Under the "Build" Section, select "Realtime Database" and click on "Create Database".
Step 09: Select the nearest Database location to reduce latency [Singapore (asia-southeast1) will be ideal for us] and select "Start in test mode" under the "Security rules" and click "Enable".
Step 10: Copy the reference url by clicking on the copy icon near the url link.
Step 11: In pyCharm, Open "AddDatatodatabase.py", "EncodeGenerator.py" and "main.py" files and replace the already existing reference URL in all three of the files with your own URL that we just copied.
Step 12: In the Firebase Project Overview page, In the "Product categories" pane, Under the "Build" Section, Select "Storage" and click on "Get Started".
Step 13: Select "Start in test mode" and click "Next" and then "Done".
Step 14: Copy the Storage Bucket folder path URL by clicking on the copy icon near the url link.
Step 15: In the pyCharm, Open "EncodeGenerator.py" and "main.py" files and replace the already existing Storage Bucket folder path URL in both of the files with your own URL that we just copied (make sure to remove the "gs://" part of the URL here).
Step 16: Under the project folder, In the "Images" folder place a picture of the person your want to be enrolled in the attendance (must be a PNG file with a resolution of 216x216, and named in integers).
Step 17: In PyCharm, Open "AddDatatodatabase.py" and add a entry as a JSON object for the new person enrolled in the attendance, where the key is named with the name of the PNG image(without the extension) and the value will be a object with the approriate details. (refer the provide example)
Step 18: In PyCharm, Run the "AddDatatodatabase.py" file first and make sure it finishes executing without throwing any errors.
Step 19: Then, Run the "EncodeGenerator.py" file and make sure it finishes executing with the output "Encoding Complete File Saved".
Step 20: Finally run the "main.py" file and allow access to camera and try using the attendance with a person enrolled.

Step 21*: Use the stop button the PyCharm IDE to stop and close the attendance system window and project (Otherwise it will keep reopening and continue to run).
