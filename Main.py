from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os
import time

print('Starting')
time.sleep(1)

whatFileName = 'to_ocr'

pageNum = 1

num = 0
whichList = (0,1,2,3,4,5,6,7,8,9)

for which in whichList:
    print("Loading "+whatFileName+str(which+1)+'.pdf... ');
    try:
        pages = convert_from_path(whatFileName+str(which+1)+'.pdf', 200)
    except  Exception as e:

        print("File "+whatFileName+str(which+1)+'.pdf not found, ending interpretation');
        print("Or, in any case, there was an error when trying to load it.")
        print("Error message: ",e)
        time.sleep(4)
        exit()
    print("Interpreting image as text...");

    i = 0
    for page in pages:
        if (len(str(i)) == 1):
            page.save('images'+str(which)+'/Page '+str(which)+'0'+str(i)+'.jpg', 'JPEG')
        elif (len(str(i)) == 2):
            page.save('images'+str(which)+'/Page '+str(which)+str(i)+'.jpg', 'JPEG')
        else:
            page.save('images'+str(which)+'/Page '+str(i)+'.jpg', 'JPEG')
        i+=1;

    pages = None;

    f = []
    t = []
    input_dir = 'images'+str(which)+'/'

    output = "";

    for root, dirs, filenames in os.walk(input_dir):
        for filename in filenames:
            print("Doing",filename,"as page number",str(pageNum))
            try:
                output += "Page "+str(pageNum)+"\n"
                #print("Interpreting as page num: ",str(pageNum))
                f.append(filename)
                img = Image.open(input_dir+ filename)
                text = pytesseract.image_to_string(img, lang = 'eng')
                img.close()
                t.append(text)
                output += text+"\n"
                output += '-='*30+"\n"
                pageNum += 1;
            except:
                #print("Unexpected file in image list; probably end of list")
                continue

    file = open("output"+str(which+1)+".txt","w")
    file.write(output)
    file.close();
    output = "";
    time.sleep(2)