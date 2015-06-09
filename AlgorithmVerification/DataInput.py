'''
Created on 2015-5-19

@author: yujing
'''

def get_PRFVAL(list_Fact,list_Rec):
    tmp = [val for val in list_Fact if val in list_Rec]
    length_inter=len(tmp)
    length_fact=len(list_Fact)
    length_Rec=len(list_Rec)
    Pval = float('%0.3f'%length_inter)/float('%0.3f'%length_fact)
    Rval = float('%0.3f'%length_inter)/float('%0.3f'%length_Rec)
    Fval = 2*Pval*Rval/(Pval+Rval)
    return  Pval,Rval,Fval
def get_COVval(list_Rec,list_Pool):
    length_Rec=len(list_Rec)
    length_Pool=len(list_Pool)
    CVal = float('%0.3f'%length_Rec)/float('%0.3f'%length_Pool)
    return CVal;
#def get_Gene(list_Rec,list_Pool,list_dianji):
     
    
if __name__ == '__main__':
    list1 = {1,2,3,4,5}
    list2 = {2,3,4,7,9}
    list3 = {1,2,3,4,5,6,7,8,9,10}
    list4 = {10,10,10,9,9,8,7,6,5,1}
    print get_PRFVAL(list1,list2)
    print get_COVval(list2,list3)