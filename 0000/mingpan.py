#coding=utf-8
#定义一个名片列表,用来储存学生信息
# card_infors=[]
# while True:
#     #2 获取用户的输入
#     num=int(raw_input('请输入操作序号'))
#     #3 根据用户的数据执行相应的功能
#     if num==1:
#         new_name =raw_input('请输入新的名字：')
#         new_qq =raw_input('请输入新的qq：')
#         new_weixin =raw_input('请输入新的微信：')
#         new_addr =raw_input('请输入新的地址')
#
#         #定义一个字典，用来存储一个新的名片
#         new_infor ={}
#         new_infor['name']=new_name
#         new_infor['qq']=new_qq
#         new_infor['weixin']=new_weixin
#         new_infor['addr']=new_addr
#         #将一个字典，添加到列表中
#
#         card_infors.append(new_infor)
#         # print card_infors    #for——test
#     elif num==2:
#
#         find_flag=0 #默认表示没有找到
#         del_mingpian=raw_input('请输入你要删除的名片姓名')
#         for temp in card_infors[:]:
#             if del_mingpian == temp['name']:
#                 card_infors.remove(temp)
# # 原始的list是card_infors，那么其实，card_infors[:]是对原始的card_infors的一个拷贝，
# # 是一个新的list，所以，我们遍历新的list，而删除原始的list中的元素，则既不会引起索引溢出           #
#                 print '删除名片成功'
#                 find_flag=1
#                 break
#
#         if find_flag==0:
#              print('查无此人,无法删除')
#
#     elif num==3:
#         find_flag=0 #默认表示没有找到
#         find_mingpian=raw_input('请输入你要修改的名片姓名')
#         for temp in card_infors[:]:
#             if find_mingpian==temp['name']:
#                 update_mingpian=raw_input('请输入修改后的名片姓名为：')
#                 temp.update({'name':update_mingpian})
#                 print '修改名片成功'
#                 find_flag=1
#                 break
#
#         if find_flag==0:
#              print('查无此人,无法修改')
#
#     elif num==4:
#         find_flag=0 #默认表示没有找到
#         find_name =raw_input('请输入你查找的姓名')
#         for temp in card_infors:
#             if find_name==temp['name']:
#                 print "%s\t%s\t%s\t%s" %(temp['name'],temp['qq'],temp['weixin'],temp['addr'])
#                 find_flag=1
#                 break
#
#         #判断是否找到了
#         if find_flag==0:
#             print('查无此人')
#
#     elif num==5:
#         print('姓名\tQQ\t微信\t地址')
#         for temp in card_infors:
#             print "%s\t%s\t%s\t%s" %(temp['name'],temp['qq'],temp['weixin'],temp['addr'])
#
#     elif num==6:
#         break
#     else:
#         print('输入有误，请重新输入')

#定义一个名片列表,用来储存学生信息
card_infors=[]

def minpian():
    '''打印功能菜单'''
    print('='*50)
    print('     名片管理系统V1.0 ')
    print('1.添加一个新的名片')
    print('2.删除一个名片')
    print('3.修改一个名片')
    print('4.查询一个名片')
    print('5.显示所有名片')
    print('6.保存信息')
    print('7.退出系统')
    print('='*50)

def add_new_card_infors():
    '''完成添加一个新的名片'''
    new_name =raw_input('请输入新的名字：')
    new_qq =raw_input('请输入新的qq：')
    new_weixin =raw_input('请输入新的微信：')
    new_addr =raw_input('请输入新的地址')

    #定义一个字典，用来存储一个新的名片
    new_infor ={}
    new_infor['name']=new_name
    new_infor['qq']=new_qq
    new_infor['weixin']=new_weixin
    new_infor['addr']=new_addr
    #将一个字典，添加到列表中
    global card_infors
    card_infors.append(new_infor)
    # print card_infors    #for——test
def del_card_infors():
    global card_infors
    find_flag=0 #默认表示没有找到
    del_mingpian=raw_input('请输入你要删除的名片姓名')
    for temp in card_infors[:]:
        if del_mingpian == temp['name']:
            card_infors.remove(temp)
# 原始的list是card_infors，那么其实，card_infors[:]是对原始的card_infors的一个拷贝，
# 是一个新的list，所以，我们遍历新的list，而删除原始的list中的元素，则既不会引起索引溢出           #
            print '删除名片成功'
            find_flag=1
            break

    if find_flag==0:
         print('查无此人,无法删除')
def update_card_infors():
    '''修改一个名片'''
    global card_infors
    find_flag=0 #默认表示没有找到
    find_mingpian=raw_input('请输入你要修改的名片姓名')
    for temp in card_infors[:]:
        if find_mingpian==temp['name']:
            update_mingpian=raw_input('请输入修改后的名片姓名为：')
            temp.update({'name':update_mingpian})
            print '修改名片成功'
            find_flag=1
            break

    if find_flag==0:
         print('查无此人,无法修改')
def find_card_infors():
    '''查询一个名片'''
    global card_infors
    find_flag=0 #默认表示没有找到
    find_name =raw_input('请输入你查找的姓名')
    for temp in card_infors:
        if find_name==temp['name']:
            print "%s\t%s\t%s\t%s" %(temp['name'],temp['qq'],temp['weixin'],temp['addr'])
            find_flag=1
            break

    #判断是否找到了
    if find_flag==0:
        print('查无此人')


def show_card_infors():
    '''显示所有名片'''
    global card_infors
    print('姓名\tQQ\t微信\t地址')
    for temp in card_infors:
        print "%s\t%s\t%s\t%s" %(temp['name'],temp['qq'],temp['weixin'],temp['addr'])
def save_file():
    f =open('mingpian.txt','w')
    f.write(str(card_infors))
    print('保存信息成功')
    f.close()

def load_infor():
    global card_infors
    f =open('mingpian.txt')
    card_infors=eval(f.read())
    f.close()
def main():
    '''完成对整个程序的控制'''
    #1.打印功能提示
    minpian()
    load_infor()
    while True:
        #2获取用户的输入
        num=int(raw_input('请输入操作序号'))

        #根据用户的输入执行程序
        if num==1:
            add_new_card_infors()
        elif num==2:
            del_card_infors()
        elif num==3:
            update_card_infors()
        elif num==4:
            find_card_infors()
        elif num ==5:
            show_card_infors()
        elif num ==6:
            save_file()
        elif num==7:
            break
        else:
            print('输入有误，请重新输入')



if __name__=='__main__':
    main()
