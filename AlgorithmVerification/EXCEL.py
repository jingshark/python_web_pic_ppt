'''
Created on 2015-6-8

@author: yujing
'''
from win32com.client import Dispatch
app = Dispatch ("Excel.Application")
wb = app.Workbooks.Add ()

wb.SaveAs('E:\myfile.xlsx')
