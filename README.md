# SCOUT
## Semantic search engine for Clinical Oncology guideline Understanding and Treatment planning

 
## How to run the Project? 
1. Download the Repo and navigate to the respective folder and start the Command Line Interface.
2. Type the following command: 

```
pip install -r .\requirements.txt
```  

This will install all the requirements.  

3. Install pytesseract from https://github.com/tesseract-ocr/tesseract/releases   
   And poppler from https://poppler.freedesktop.org/  according to specification of your machines.   
   Copy paths of installled pytesseract and poppler and paste it in extract.py file.  

   (NOTE: this step is only required if you want to use scout engine for new pdf.)

4.navigate to search modules folder and then modify queries and pdf_name in file of query.py to use scout search engine: 

This will initiate scout engine and find out relevant pages

user can configure pdf name and search query from query.py itself.
