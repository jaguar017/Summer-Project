import face_recognition
import os
import cv2

Known_faces_dir ="known_faces"
Unknown_faces_dir="unknown_faces"
Tolerance=0.5
Model="hog"

video=cv2.VideoCapture(0)
print("loading known faces")

known_faces=[]
known_names=[]

for name in os.listdir(Known_faces_dir):
    for filename in os.listdir(f"{Known_faces_dir}/{name}"):
        image= face_recognition.load_image_file(f"{Known_faces_dir}/{name}/{filename}")
        encoding=face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)

print("Processing unknown faces")
for filename in os.listdir(Unknown_faces_dir):
    print(filename)
    image=face_recognition.load_image_file(f"{Unknown_faces_dir}/{filename}")
    img=cv2.resize(image,(640,480))
   # img1=cv2.resize(image,(512,512))
    locations=face_recognition.face_locations(img,model=Model)
    encodings=face_recognition.face_encodings(img,locations)
    img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

    for face_encoding,face_location in zip(encodings,locations):
        results = face_recognition.compare_faces(known_faces,face_encoding,Tolerance)
        match =None
        if True in results:
            match =known_names[results.index(True)]
            print(f"Match found: {match}")
            top_left=(face_location[3],face_location[0])
            bottom_right=(face_location[1],face_location[2]+22)
            cv2.rectangle(img,top_left,bottom_right,(0,0,255))
            cv2.putText(img,match,(face_location[3]+10,face_location[2]+15),cv2.FONT_HERSHEY_COMPLEX,0.5,(200,200,200))
    cv2.imshow(filename,img)
    
    if cv2.waitKey(1000)&0Xff ==ord("q"):
        break

cv2.destroyAllWindows()
