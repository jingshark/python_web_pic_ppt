'''
Created on 2015-6-2

@author: yujing
'''

'''
Created on 2015-5-28

@author: yujing
'''
import json,urllib2,sys,re, urllib,os,httplib,chardet

def _get_src(req, req_timeout):
    try:
        resp = urllib2.urlopen(req, timeout = req_timeout)
        # html = resp.read()
   
        html = resp.read()
        detecter = chardet.detect(html)
        info_encode = detecter.get('encoding','utf-8')##通过第3方模块来自动提取网页的编码

        html = html.decode(info_encode,'ignore').encode("utf8")##先转换成unicode编码，然后转换系统编码输出
        return  html
    except  Exception,ex:
        print "Error: unable to fecth data" + str(ex)
        #traceback.print_exc()
        return ""

def get_src(url):
    req_timeout = 10
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    req.add_header('Accept', 'text/html;q=0.9,*/*;q=0.8')
    req.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3')
    #req.add_header('Accept-Encoding', 'gzip')
    #req.add_header('Connection', 'close')
    req.add_header('Referer',url)
    print req 
    for i in range(1,4):

        result = _get_src(req, req_timeout)
        if result != None and result.strip() != "":
            return result

def get_info():
    #output = open("D:/result.txt", "w")
    try:
        src = get_src("http://192.168.5.111:9105/resume/getDetailFromFile?enable=true")
        obj = json.loads(src)
        print obj[0]["info"]
     #   if len(obj) > 0:
      #      print obj[0]["desc_skill_item"]
      #          product=product1[0]["name"]
        #        for i in range(1, product1.__len__()-1):
        #            product="%s,%s"%(product,product1[i]["name"])
        #print skill
        return 0
    except:    
        return 0
if __name__ == '__main__':
    get_info()
    print "down"
        