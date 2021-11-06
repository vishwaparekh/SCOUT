# SCOUT
## Semantic search engine for Clinical Oncology guideline Understanding and Treatment planning

 
## How to run the Project? 
1. Download the Repo and navigate to the respective folder and start the Command Line Interface.
2. Type the following command to install all the requirements: 

```
pip install -r .\requirements.txt
```  

 

3. Install pytesseract from https://github.com/tesseract-ocr/tesseract/releases   
   And poppler from https://poppler.freedesktop.org/  according to specification of your machines.   
   Copy paths of installled pytesseract and poppler and paste it in extract.py file.  

   (NOTE: this step is only required if you want to use scout engine for new pdf.)
 
4. To use scout search engine: 

```
search = Search("prostate_blocks")
search.call_query("show therapy for M1 crpc")
```  
   - This will initiate scout engine for 'prostate blocks guidelines' and find out relevant pages for query of 'show therapy for M1 crpc'
   - User can configure guidelines name and search query from query.py itself.
   
5. To use scout engine for new guidelines, keep a pdf file of guidelines in scout folder and write following code. 
```
from extract import Extract
#a=Extract("<guidelines_name>")
```  
