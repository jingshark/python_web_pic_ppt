'''
Created on 2015-7-1

@author: yujing
'''
import csv,io
csvfile = file("d://testjson.csv", "rb")
reader = csv.reader(csvfile)
i=0
node1=[]
node2=[]
node3=[]
for line in reader:
    if i==0:
        if line[0]=="ref":
            node1.append(line[2])
            node2.append(line[1])
            i=i+1
        elif line[0]=="to":
            node2.append(line[1])
            node3.append(line[4])
            i=i+1
    else :
        if line[0]=="ref":
            s=0
            s1=0
            for node in node1:
                #print node
                if node!=line[2]:
                    s=s+1
            for node in node2:
                if node!=line[1]:
                    s1=s1+1
            if s==len(node1):
                node1.append(line[2])
            if s1==len(node2):
                node2.append(line[1])    
            i=i+1
        elif line[0]=="to":
            s=0
            s1=0
            for node in node2:
                if node!=line[1]:
                    s=s+1
            for node in node3:
                if node!=line[4]:
                    s1=s1+1
            if s==len(node2):
                node2.append(line[1])
            if s1==len(node3):
                node3.append(line[4])    
            i=i+1
csvfile.close() 
nodeend=node1+node2+node3
print nodeend
dict=[]
for node in nodeend:
    dict.append({"name":node})
print dict
csvfile = file("d://testjson.csv", "rb")
reader = csv.reader(csvfile)
#ii=0
path=[]
for line in reader:
        if line[0]=="ref":
            i1=0
            i2=0
            tar=0
            sor=0
            for node in node1:
                i1=i1+1
                if node==line[2]:
                    sor=i1-1
            for node in node2:
                i2=i2+1
                if node==line[1]:
                    tar=i2+len(node1)-1
            path.append({"source":sor,"target":tar,"value":int(line[3])}) 
        if line[0]=="to":
            i1=0
            i2=0
            tar=0
            sor=0
            for node in node2:
                i1=i1+1
                if node==line[1]:
                    sor=i1+len(node1)-1
            for node in node3:
                i2=i2+1
                if node==line[4]:
                    tar=i2+len(node1)+len(node2)-1
            path.append({"source":sor,"target":tar,"value":int(line[3])})
csvfile.close()
json={"nodes":dict,"links":path} 
print json       