'''
Created on 2015-5-29

@author: yujing
'''

import re,urllib

def getHtml(url):
    page = urllib.urlopen(url)    
    html=page.read()
    return html

def getImage(html):
    srcg=r'src="(.*?\.jpg)" class='
    imgre = re.compile(srcg)
    imagelist = re.findall(imgre,html)
    i=1
    for imgurl in imagelist:
        urllib.urlretrieve(imgurl, "%s.jpg",i)
        i=i+1
#if __name__ == '__main__':
html=getHtml("http://image.baidu.com/")
getImage(html)        