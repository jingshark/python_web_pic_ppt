"""
Created on 2015-7-1

@author: yujing
"""

import csv,io

csvfile = file("d://testjson.csv", "rb")
reader = csv.reader(csvfile)
i=0
dict2=[]
path=[]
lay1=0
lay2=0
lay3=0
s1=0
s2=0
s3=0
for line in reader:
    if i==0:
       if line[0]=="to" and line[2] == "edu":
           dict2.append({"name":line[1],"layer":2})
           i=i+1
           lay2=lay2+1
           dict2.append({"name": line[4],"layer":3})
           path.append({"source":i,"target":i-1,"value":int(line[3])})
           i=i+1
           lay3=lay3+1
       elif line[0]=="ref":
           dict2.append({"name": line[1],"layer":2})
           lay2=lay2+1
           i=i+1
           dict2.append({"name": line[2],"layer":1})
           lay1=lay1+1
           path.append({"source":i,"target":i-1,"value":int(line[3])})
           i=i+1                          
    else :
       if line[0]=="to" and line[2] == "edu":
            jie2=0
            jie3=0
            for name1 in dict2:
                print name1
                if  name1["name"]!=line[1] and name1["layer"] == 2:
                    s2=s2+1
                elif name1["name"]==line[1] and name1["layer"] == 2:
                    jie2=s2+1
                if  name1["name"]!=line[4] and name1["layer"] == 3:
                    s3=s3+1
                elif name1["name"]==line[4] and name1["layer"] == 3:
                    jie3=s3+1
            print s2,s3
            if s2 == lay2:
                dict2.append({"name": line[1],"layer":2})    
                s2=0
                jie2=i
                i=i+1
                lay2=lay2+1
            if s3 == lay3:
                dict2.append({"name": line[4],"layer":3})
                jie3=i    
                s3=0
                i=i+1
                lay3=lay3+1
            else :
                s2=0
                s3=0
            path.append({"source":jie2,"target":jie3,"value":int(line[3])})
            #print path 
       elif line[0]=="ref":
            jie2=0
            jie1=0
            for name1 in dict2:
               # print name1
                if  name1["name"]!=line[1] and name1["layer"] == 2:
                    s2=s2+1
                elif name1["name"]==line[1] and name1["layer"] == 2:
                    jie2=s2+1
                if  name1["name"]!=line[2] and name1["layer"] == 1:
                    s1=s1+1
                elif name1["name"]==line[2] and name1["layer"] == 1:
                    jie3=s1+1
            #print s2,s1
            if s2 == lay2:
                dict2.append({"name": line[1],"layer":2})    
                s2=0
                jie2=i
                i=i+1
                lay2=lay2+1
            if s1 == lay1:
                dict2.append({"name": line[2],"layer":1})
                jie1=i    
                s1=0
                i=i+1
                lay1=lay1+1
            else :
                s2=0
                s1=0
            path.append({"source":jie1,"target":jie2,"value":int(line[3])})
            #print path
#    print dict2,path      
csvfile.close() 
json={"nodes":dict2,"links":path}
print json
