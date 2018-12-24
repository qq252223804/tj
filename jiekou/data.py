#coding=utf-8

import xlrd

def ReadExcel(sheetx,rowx,colx):
    a=xlrd.open_workbook('C:\\Users\\Administrator\\Desktop\\打包\\tj\\jiekou\\dataExcel.xlsx')
    b=a.sheet_by_index(sheetx)
    c=b.cell_value(rowx,colx)
    return c

def datacel():
    filepath='C:\\Users\\Administrator\\Desktop\\打包\\tj\\jiekou\\data.xlsx'  #文件的路径
    file=xlrd.open_workbook(filepath)#使用xlrd的open_workbook打开文件
    me=file.sheets()[0]
    nrows=me.nrows #获取行数
    # print(nrows)
    listkey=[]
    listconeent=[]
    listurl=[]
    listfangshi=[]
    listqiwang=[]      #定义对应的用例条件的list
    for i in range(1,nrows):#循环所有行数的值
        listkey.append(me.cell(i,2).value)
        listconeent.append(me.cell(i,3).value)
        listurl.append(me.cell(i,4).value)
        listfangshi.append((me.cell(i,5).value))
        listqiwang.append((me.cell(i,5).value))


    print (listkey)
    print (listconeent)
    # print listqiwang
# datacel()

