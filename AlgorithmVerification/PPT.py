'''
Created on 2015-6-8

@author: yujing
'''

import win32com.client
import win32com.client.dynamic
import os


  
App = win32com.client.Dispatch("PowerPoint.Application")
App.Visible = 0
Presentation = App.Presentations.Open("d:\BugCurve.ppt")
mySlide = Presentation.Slides.Add(2,12)
shape = mySlide.Shapes.AddPicture("d:\This_is_Picture.png",LinkToFile=False,SaveWithDocument=True,Left=40,Top=100,Width=650,Height=400)



# import win32com
# from win32com.client import Dispatch, constants
# 
# ppt = win32com.client.Dispatch('PowerPoint.Application')
# pptSel = ppt.Presentations.Open('D:/BugCurve.ppt',ReadOnly=1, Untitled=0, WithWindow=0)
# win32com.client.gencache.EnsureDispatch('PowerPoint.Application')
# slide_count = pptSel.Slides.Count
# ppt.Quit()
# print(slide_count)


# ppt = win32com.client.Dispatch('PowerPoint.Application')
# ppt.Visible = 1
# pptSel = ppt.Presentations.Open("c:\\1.ppt")
# win32com.client.gencache.EnsureDispatch('PowerPoint.Application')
# 
# f = file("c:\\1.txt","w")
# slide_count = pptSel.Slides.Count
# for i in range(1,slide_count + 1):
#     shape_count = pptSel.Slides(i).Shapes.Count
#     print shape_count
#     for j in range(1,shape_count + 1):
#         if pptSel.Slides(i).Shapes(j).HasTextFrame:
#             s = pptSel.Slides(i).Shapes(j).TextFrame.TextRange.Text
#             f.write(s.encode('utf-8') + "\n")        
# f.close()
# ppt.Quit()