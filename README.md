# SCOUT
## Semantic search engine for Clinical Oncology guideline Understanding and  Treatment planning

## Abstract

#### 1. Introduction
Cancer is one of the largest public health burdens across the world. One out of every four
deaths in the United States is due to cancer. Furthermore, there are nearly 140 patients per
oncologist. The process of clinical decision-making is the essence of everyday clinical
practice. Oncology guidelines, such as NCCN guidelines, form a key component of clinical
decision making. However, most of the clinical guidelines are available in the PDF or text format
and span over hundreds of pages. In the current scenario, oncologists rely on keyword-based
search to query a particular treatment guideline, which has many disadvantages. One, the
oncologist can only type in one keyword or an exact phrase which is not always possible.
Second, the keyword query may produce many irrelevant results, rendering it impractical. As a
result, finding the correct treatment plan using just the keyword search is time-consuming and
unreliable. When multiple options need to be considered, balancing between accuracy and
speed in decision making is challenging. To that end, we developed SCOUT, a semantic search
algorithm for oncology clinical guidelines, that would provide an integrated search platform
across multiple clinical guidelines. The SCOUT was implemented and evaluated on the NCCN
guidelines using five different cancer types: breast cancer, prostate cancer, lung cancer, brain
cancer, and gastric cancer.

#### Step 1: Simple TF-IDF
The TF-IDF (D i ) score characterizes the likelihood of the search query being present on a page,
i. The TF-IDF score is computed by aggregating the frequency score of every keyword in the
search query as follows:

#### Step 2: Heuristic TF-IDF
The second step involves computing a TF-IDF score using a domain-specific dictionary by
weighing domain-specific keywords significantly higher than regular English keywords

#### Step 3: Compute Keyword Distances
In this step, the pages are ranked based on the relative distance between different keywords in
the search query. The keyword distance score for each page is computed as the minimum
number of sequential words that encompasses all the keywords present in the search query. If a
page does not contain all the keywords, the score is normalized using the Nearest keywords algorithm.

#### Step 4: The final step involves identifying and sorting the top-k matches
wherein, the top-k pages are selected using the scores from Step 1 and Step 2. The resultant top-k pages are then
sorted based on the keyword distance score, K.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## TECHNICAL DETAILS:-
#### Algorithm - 1 (Ranking of pages based on TF-IDF measure) 
Ranking of pages based on TF-IDF measure :
  
  
We gave TF-IDF score to each page of pdf by divide how many times a keyword appears on a page by the frequency of keyword across pdf.

![139417598-e520e5ee-7fa7-4a79-9dff-cc75ef0effa7](https://user-images.githubusercontent.com/49832962/139422212-2541c79b-2913-4305-b169-400fabf3e29f.png)



#### Algorithm - 2 (For Highlighted words)
The same algorithm is applied for capital keywords. As capital words have more priority because titles and important words are in the capital for the whole PDF.

![image](https://user-images.githubusercontent.com/49832962/139417800-22e66403-0a38-4ec2-b567-81eaaa00f3c5.png)


#### Algorithm - 3 (Nearest keywords algorithm)
We made a dictionary that can store the index of keywords. Let dictionary be dict

GOAL:- To find the page which possesses the nearest query keywords.  
For finding a score for a particular page the process is given below:  
  
- top 5 pages are selected from previous frequency based algorithms   
- Score is given to each page for the query using the nearest keyword algorithm.     
- In the nearest keyword algorithm , score is assigned to selected pages based on the minimum interval of indices where all possible keywords of the query are present.
- If  a keyword is not present in the page then we simply exclude that keyword and score is normalized accordingly.

![image](https://user-images.githubusercontent.com/49832962/139418376-03d10a5e-5ac7-4463-bc7c-d17131cf1d71.png)

![image](https://user-images.githubusercontent.com/49832962/139419221-122e6462-fdad-4b97-9cd7-260216e8aad4.png)  
Figure demonstrates how algorithm finds minimum interval between query keywords  
![image](https://user-images.githubusercontent.com/49832962/139419439-2456c6fc-dbe5-4754-ae88-a60862bd6077.png)




