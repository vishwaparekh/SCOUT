import pdf2image
import os
from pathlib import Path
import pytesseract,PIL
import pickle


class Extract:
     def __init__ (self , filename):
        pages = pdf2image.convert_from_path("data/"+filename)
        Path("data/"+filename).mkdir(parents=True, exist_ok=True)
        pytesseract.pytesseract.tesseract_cmd = 'tesseract_path'
        
    
        y=0
        for page in pages:
            y+=1
            name=str(y)+".jpg"
            fullpath = "data/"+filename+"/"+name
            page.save(fullpath, 'JPEG')
            

        result=[]
        y=0
        for page in pages:
            y+=1
            name=str(y)+".jpg"
            fullpath = "data/"+filename+"/"+name
            result.append(pytesseract.image_to_string(PIL.Image.open(fullpath)))
        

        b=[]
        def non_ascii_remover(text):
            text=text.replace("\n"," ").replace("."," ")
            return ''.join([i if (ord(i)>47 and ord(i)<123) or i=='-' else ' ' for i in text])
        for i in result:
            b.append(non_ascii_remover(i))
            
            
        
        with open("data/"+filename+".npy", "wb") as fp:   
            pickle.dump(b, fp)
