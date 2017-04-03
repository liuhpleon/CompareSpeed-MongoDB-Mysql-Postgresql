'''
Created on Mar 17, 2017

@author: haopeng
'''
import json

file_read = open("/home/haopeng/Data/pre_index_description.json","r+")
file_write = open("/home/haopeng/Data/inverted_index_description.json","w")
'''
file_read = open("/home/haopeng/UCR-Courses/CS236/Project/Data/1.5m_for_index.json","r+")
file_write = open("/home/haopeng/UCR-Courses/CS236/Project/Data/index_1500k.json","w")
'''
dict = {}
line = file_read.readline()
i = 0;
while(line!=None):
    try:
        info = eval(line)
    except:
        print "errors"
        break
    asin = info["asin"]
    title = info["description"]
    title = title.replace("/n"," ")
    title = title.split()
    for word in title:
        if dict.has_key(word):
            if asin not in dict.get(word): 
                dict.get(word).append(asin)
        else:
            dict[word] = [asin] 
    line = file_read.readline()   
    i = i +1
    if i%10000==0:
        print i
    
    
    
for k in dict.keys():
    word = k.__str__()
    asins = dict.get(k).__str__()
    info = {"word":word,"asin":asins}
    info = json.dumps(info)
    file_write.write(info+"\n")
    
       
        