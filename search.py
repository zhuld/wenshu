import csv  #csv库
import os
import sys

count = 0   #结果计数
#csv文件的栏目，
fields = ['原始链接','案号','案件名称','法院','所属地区','案件类型','案件类型编码','来源','审理程序','裁判日期','公开日期','当事人','案由','法律依据','全文']

csv.field_size_limit(500*1024*1024) #大文件，扩展csv行数限制

if len(sys.argv) != 3 :  #参数数量不对，输入关键词和项目名称
    name = input("请输入关键词：")
    print('有效栏目有：', fields)
    field = input("请输入栏目名称：")
else :
    name = sys.argv[1] #关键词
    field = sys.argv[2] #具体栏目
    
if field in fields : #栏目存在才继续
    
    #准备结果输出文件，csv格式，文件名 result_关键词_项目.cvs
    with open('result_'+name+'_'+field+'.csv','w', newline='', encoding = 'utf-8-sig') as result_file:
        csv_writer = csv.DictWriter(result_file ,fieldnames = fields)
        csv_writer.writeheader() #写入项目标题
        paths = os.walk(r'./') 
        #主循环
        for path , dir_lst, file_lst in paths: #当前文件夹所有文件遍历
            for file_name in file_lst:
                if file_name.endswith('csv')& (not ('result' in file_name)): #排除非cvs格式，以及结果输出文件
                    #打开csv文件
                    with open(os.path.join(path,file_name), mode = 'r', encoding = 'utf-8-sig' ) as csv_file:
                        csv_reader = csv.DictReader(csv_file)
                        for row in csv_reader: #遍历文件所有行
                            if name in row[field] : #判断条件，项目中是否包括关键词
                                count +=1           #计数加一
                                print(count , row['案件名称'])  #打印结果到终端
                                csv_writer.writerow(row)        #保存结果到结果文件

        if count>0 : print('总共',count, '行结果保存在：','result_'+name+'_'+field+'.csv')
        else:  print('未找到符合要求的结果')

else:
    print(field, '是无效栏目' )
    print('有效栏目有：', fields)