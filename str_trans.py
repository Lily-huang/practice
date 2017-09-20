# -*- coding:utf-8  -*-

def str_trans(origin_str):
    ori_array=origin_str.toArray()
    ret_array=[]
    up_flag=0
    index=0
    for ori in ori_array:
        if (up_flag==index) and index!=0:
            ret_array.append(ori.toUper())
            index++
            break
        if not ori.islower():
            up_flag=index+2
            ori = ori.tolower()
            ret_array.append(ori)
        else:
            ret_array.append(ori)
        index++

    ret_str=ret_array.toString()
    return ret_str[::-1]

def get_calculate_json(datas):
    date_array=map(lambda x: x[0]+'-'+x[1], datas)
    categories=set(list(date_array))
    pn_set=set(list(map(lambda x: x[2], datas)))
    data={}
    for pn in pn_set:
        pn_data=filter(lambda x: x[2]==pn, datas)
        data[pn]=map(lambda x:x[3],pn_data)
    json_str={}
    json_str['data']=data
    json_str['categories']=categories
    return json_str

def fact(n):
    if n==1 or n==0:
        return 1
    return n * fact(n-1)

'''
4、文件夹下包含txt文件和子文件夹，需要遍历该文件夹下所有txt文件，并统计文件中包含多少个hello world 字符串？若单个文件较大超过4GB，该怎么处理？若文件数量较大，该怎么处理？
(1)linux:wc -l|grep 'hello world'
   code:遍历计数
(2)超过4G必需考虑文件拆分和缓冲，不能直接读到内存中
   可以把文件大文件拆分成小文件，再进行遍历匹配计算，可以在bufferedReader中设置缓冲区参数
(3)文件数量较大，如果文件较小可以考虑合并文件再进行处理
   对文件的处理状态进行标志，作为锁状态，可使用多线程来处理，保证不重复处理相同的文件

5、Flask中，A模板需要从B，C两个模板继承，怎样实现？
(1)继承：B和C之间成为父子关系，A继承自其中的子类  #记错了，java才是

Flask不太熟，继承会用


6、truncate为什么比delete快？
没用过truncate
看了资料delete是一行一行处理释放资源的，truncate是从数据表的级别，所以效率高些


7、处理字符串 str = "  api-修复velocity延迟问题2_-4——21A34中文 345&+_：“”）（）￥~·、}】【‘；’】yiy		*****~·|、+——--……6"
   用"_"替换掉空白处

如果有不可识别的特殊字符，先换编码，再进行对应处理，之后转回来
'''
