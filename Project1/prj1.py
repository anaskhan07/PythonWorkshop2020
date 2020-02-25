
# ..........................................First Project By KHAN ANAS ANIS...............................

# Importing all required files
from bs4 import BeautifulSoup           '''To get the urls of images in a Beautiful order'''
import  requests                        '''To get the urls of websites'''
from requests_html import HTMLSession   '''To get the HTMLSession'''
import cv2                              '''To get access of images and process it accordingly'''
import shutil                           '''To download the images'''
import time                             '''To get access of time functions'''
Session = HTMLSession()
urls=[]


cat_face_cascade = cv2.CascadeClassifier("cat.xml")
host_path = r"C:\Windows\System32\drivers\etc\hosts"
temp = r"hosts"
redirect = "127.0.0.1"
for i in range(2,3):
    urls.append(f"http://www.cutestpaw.com/page/{i}/")

for url in urls:
    source = Session.get(url).html.html
    soup = BeautifulSoup(source,'lxml')
    box = soup.find('div', {'id':'photos'})
    elements = box.find_all('a')
    images = []
    for element in elements:
        
        img = element.select('img')[0]['src']
        images.append(img)
    
    # f_cascade = cv2.CascadeClassifier("cat.xml")
    for j in range(0,len(images)):
        resp = requests.get(images[i],stream = True)
        local_file = open('local_image.jpg','wb')
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw,local_file)
        # print(path)
        image = cv2.imread("local_image.jpg",1)
        grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        face = cat_face_cascade.detectMultiScale(image,scaleFactor = 1.1,minNeighbors = 5)
        
        
        if face.all()==True:              '''if face is getting some value then it is true'''
            faces = False
        else:
            faces = True
            
        for x,y,w,h in face:
            image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        
        resized = cv2.resize(image,(int(image.shape[1]),int(image.shape[0])))
        cv2.imshow('imagex',resized)
        cv2.waitKey(1000)
        cv2.destroyAllWindows
            
        if faces==True:                        ''' if faces is true the cat is detected else the site is blocked'''
            print("The Site Will Be Blocked As It Has Not A Single Image Of Cat")
            with open(host_path,'r+') as file:
                content = file.read()
                for web in images:
                    if web in content:
                        pass
                    else:
                        file.write(redirect + " "+ web+ "\n")
        else:
            with open(host_path,'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any (web in line for web in images):
                        file.write(line)
                    file.truncate()
            print("The Site Has Got The Image Of A Cat")
        time.sleep(1)
            