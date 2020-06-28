import face_recognition
import os
import cv2
from firebase import firebase
Known_faces_dir ="known_faces"
Tolerance=0.8
Model="hog"

video=cv2.VideoCapture(0)
print("loading known faces")

known_faces=[]
known_names=[]
i=0

for name in os.listdir(Known_faces_dir):
    for filename in os.listdir(f"{Known_faces_dir}/{name}"):
        image= face_recognition.load_image_file(f"{Known_faces_dir}/{name}/{filename}")
        encoding=face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)

print("Processing unknown faces")
while True:
    ret,image=video.read()
    locations=face_recognition.face_locations(image,model=Model)
    encodings=face_recognition.face_encodings(image,locations)

    for face_encoding,face_location in zip(encodings,locations):
        results = face_recognition.compare_faces(known_faces,face_encoding,Tolerance)
        match =None
        print(results)
        if True in results:
            match =known_names[results.index(True)]
            print(f"Match found: {match}")
            top_left=(face_location[3],face_location[0])
            bottom_right=(face_location[1],face_location[2]+22)
            cv2.rectangle(image,top_left,bottom_right,(0,0,255))
            cv2.putText(image,match,(face_location[3]+10,face_location[2]+15),cv2.FONT_HERSHEY_COMPLEX,0.5,(200,200,200))
            cv2.imshow(filename,image)
            if(match ==None):
                cv2.imwrite("unknown"+str(i)+".jpg", image)
                print("unknown")
                cv2.imshow(filename,image)
                i=i+1
            
            
    if cv2.waitKey(1)&0Xff ==ord("q"):
        break
cv2.destroyAllWindows()
                                     
