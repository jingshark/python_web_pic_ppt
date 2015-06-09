'''
Created on 2015-5-28

@author: yujing
'''
import json,urllib2,sys,re, urllib,os,httplib,chardet

def _get_src(req, req_timeout):
    try:
        resp = urllib2.urlopen(req, timeout = req_timeout)
        # html = resp.read()
       # #type_encode = sys.getfilesystemencoding()##系统默认编码
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

def get_skill(uid):

    try:
        src = get_src("http://rc.dm.csdn.net/compute/skillsForRecommend?id="+uid+"&type=blog")
        obj = json.loads(src)
        #print obj
        if len(obj) > 0:
            skill=obj[obj.__len__()-1]["name"]              
        else:
            skill = "-"
        #print skill
        return (skill.encode("gbk") )
    except:
        #print "error ", id
        skill = "-"      
        return (skill.encode("gbk"))
if __name__ == '__main__':
    
    output = open("D:/2014-highbolgresult.txt", "w")
    
    for line in open("D:/highbolg-2014.txt", "r").readlines():
        
        name = line.strip()
        skill =  get_skill(name)

        #print name, " -> ", skill
        output.write("%s\t%s\n" % (name, skill))
        
    
    output.close()
    print "down"
        