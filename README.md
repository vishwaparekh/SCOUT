# SCOUT
##Semantic search engine for Clinical Oncology guideline Understanding and  Treatment planning

# Algorithm 1 (Ranking of pages based on TF-IDF measure) 
The query is split into keywords


We gave TF-IDF score to each page of pdf by multiplying how many times a keyword appears on a page by the inverse of the frequency of keyword across pdf.


Let’s say the query (Q) is “brain cancer” it will be split into keywords  “brain’’ and “cancer” and the TF-IDF score will be calculated for every keyword on every page. 

Let no of pages in pdf be m.

TF-IDF score for particular page= ⅀ (frequency of keyword in particular page)*(frequency of keyword in pdf)-1

Let the number of keywords in the query be n. Therefore(, keywords are K1,K2……, Kn.
c

Ti is the TF-IDF score of ith page for the query Q.

So T will be an array of size m such that T = {T1,T2 ,T3,.....,Tm}

# Algorithm - 2 (For Capital Letters)
The same algorithm is applied for capital keywords. As capital words have more priority because titles and important words are in the capital for the whole PDF.

![image](https://user-images.githubusercontent.com/49832962/139416815-29715920-71f2-4999-a18d-75366fc4aa90.png)

# Algorithm - 3 (Nearest keywords algorithm)
We made a dictionary that can store the index of keywords. Let dictionary be dict

We will make a dictionary of 5 selected pages only

Pseudocode:

'''
nearest_keywords(k,i)
{
	if(find_just_bigger_element(i))
	{
		return minimum_of(nearest_keywords((k+1,i),nearest_keywords(k+1,i-1)) 
	}
	return minimum_of(nearest_keywords((k+1,last_element_of(k+1) ))
}
'''


![1](https://user-images.githubusercontent.com/49832962/139058569-35154f7d-5968-4eb9-9e12-6ebad3880ed5.png)
