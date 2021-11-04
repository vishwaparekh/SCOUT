import json
import numpy as np
import pickle
from collections import Counter
import PIL

class Search:
    
    def __init__ (self , filename):
        self.filename = filename
        self.fp=open(self.filename, "rb") 
        self.word_array = pickle.load(self.fp)
        self.query_length=0
        #count frequency of words in page 
        lst=[]
        for i in self.word_array:
            lst.append(Counter(i.lower().split()))
        self.page_lst=lst
        
        #count frequency of words in document
        ss=""
        for i in self.word_array:
            ss=ss+i
        self.unique_dic=Counter(ss.lower().split())
        
        #extract capital word from the word array
        self.cap_lst=[]
        for i in self.word_array:
            cap_str=""
            for j in i.split() :
                if  j.isupper() :
                    cap_str=cap_str+" "+j
            self.cap_lst.append(cap_str)
            
        #count frequency of capital words in page
        lst=[]
        for i in self.cap_lst:
            lst.append(Counter(i.lower().split()))

        self.cap_page_lst=lst
        
        #count frequency of capital words in document
        ss=""
        for i in self.cap_lst:
            ss=ss+i
        self.cap_unique_dic=Counter(ss.lower().split())
        
        
    
    def call_query(self,query):
        self.query_length=len(query.split())
        ans1=self.algo1(query)
        ans2=self.algo2(query)
        ans=ans1+ans2
        
        res1=[i+1 for i in ans1.argsort()[-5:][::-1]]
        res2=[i+1 for i in ans2.argsort()[-5:][::-1]]
        res=[i+1 for i in ans.argsort()[-5:][::-1]]
        
        final=self.algo3(query,res)
        final=np.array(final)
        final_arg=[i+1 for i in final.argsort()[-5:][::-1]]
        
        res3=[]
        for i in final_arg:
            res3.append(res[i-1])
        
        if self.query_length == 1:
            res3 = res    
            
        print("algo1&2_result       "+str(res))
        print("algo1_freq_result    "+str(res1))
        print("algo2_capital_result "+str(res2))
        print("final_result         "+str(res3))
        
        im = PIL.Image.open("data/"+self.filename[:-4]+"/"+str(res3[0])+".jpg")  
        im.show() 
  

        
    def algo1 (self,query):
        answer_vector=np.zeros(len(self.word_array),dtype=float)
        for i in range(len(self.page_lst)):
            summ=0
            for word  in query.lower().split():
                if word in self.page_lst[i].keys():
                    summ=summ+self.page_lst[i][word]/self.unique_dic[word]+1
            answer_vector[i]=summ
        return  answer_vector
    
    
    def algo2(self,query):
        answer_vector=np.zeros(len(self.cap_lst),dtype=float)
        for i in range(len(self.cap_page_lst)):
            summ=0
            for word  in query.lower().split():
                if word in self.cap_page_lst[i].keys():
                    summ=summ+self.cap_page_lst[i][word]/self.cap_unique_dic[word]+1
            answer_vector[i]=summ
        return  answer_vector
    
    def algo3(self,query,res):
        minimum=1000000000 
        query=query.lower().split()
        arr=[]
        result=[]
        for i in res:
            dic=dict()
            
            for j in query:
                if j in self.word_array[i-1].lower().split():
                    res_list = [x for x, value in enumerate(self.word_array[i-1].lower().split()) if value == j] 
                    dic[j]=res_list
            arr.append(dic)
        for i in arr:
            key_arr=list(i.keys())
            if len(key_arr)>1:
                mini=1000000000
                for j in range(len(i[key_arr[0]])):
                            mini=min(mini,self.dic_tra(key_arr,i,0,j,i[key_arr[0]][j]-1,i[key_arr[0]][j]-1))
                result.append(len(i.keys())**3/mini)
            else:
                result.append(0)
        return result    
    
    def dic_tra(self,key_arr,page_dic,k,m,mini,maxi):
        
        if m<0:
            return 1000000000
        if k+1 >= len(key_arr):
            return maxi-mini
        else :
            f=0
            for i in range(len(page_dic[key_arr[k+1]])):
                if page_dic[key_arr[k+1]][i] > page_dic[key_arr[k]][m]:
                            return min(self.dic_tra(key_arr,page_dic,k+1,i,min(mini,page_dic[key_arr[k+1]][i]),max(maxi,page_dic[key_arr[k+1]][i])),self.dic_tra(key_arr,page_dic,k+1,i-1,min(mini,page_dic[key_arr[k+1]][i]),max(maxi,page_dic[key_arr[k+1]][i])))                                                                                
            return self.dic_tra(key_arr,page_dic,k+1,len(page_dic[key_arr[k+1]])-1,min(mini,page_dic[key_arr[k+1]][i]),max(maxi,page_dic[key_arr[k+1]][i]))                                                                                  