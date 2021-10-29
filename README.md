# SCOUT
## Semantic search engine for Clinical Oncology guideline Understanding and  Treatment planning

# Algorithm 1 (Ranking of pages based on TF-IDF measure) 
Ranking of pages based on TF-IDF measure :
  
  
We gave TF-IDF score to each page of pdf by divide how many times a keyword appears on a page by the frequency of keyword across pdf.

![image](https://user-images.githubusercontent.com/49832962/139417598-e520e5ee-7fa7-4a79-9dff-cc75ef0effa7.png)


# Algorithm - 2 (For Capital Letters)
The same algorithm is applied for capital keywords. As capital words have more priority because titles and important words are in the capital for the whole PDF.

![image](https://user-images.githubusercontent.com/49832962/139417800-22e66403-0a38-4ec2-b567-81eaaa00f3c5.png)


# Algorithm - 3 (Nearest keywords algorithm)
We made a dictionary that can store the index of keywords. Let dictionary be dict

GOAL:- goal is to find the page which possesses the nearest query keywords.  
For finding a score for a particular page the process is given below:  
  
- 5 pages are selected from previous frequency based algorithms   
- Score is given to each page for the query using the nearest keyword algorithm.     
- In the nearest keyword algorithm , score is assigned to selected pages based on the minimum interval of indices where all possible keywords of the query are present.
- If  a keyword is not present in the page then we simply exclude that keyword and score is normalized accordingly.

![image](https://user-images.githubusercontent.com/49832962/139418376-03d10a5e-5ac7-4463-bc7c-d17131cf1d71.png)

![image](https://user-images.githubusercontent.com/49832962/139419221-122e6462-fdad-4b97-9cd7-260216e8aad4.png)
Figure demonstrates how algorithm finds minimum interval between query keywords
![image](https://user-images.githubusercontent.com/49832962/139419307-942c8da2-6c27-4e3a-8c5f-1245a4b92d42.png)




