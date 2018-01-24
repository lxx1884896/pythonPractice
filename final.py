#coding=utf-8
list=[]

f=open('E:\\text.txt')

for each_line in f :
   tmp= each_line.split()
   print(tmp)
   list.extend(tmp)
   # l=len(tmp)
   # for i in range(l):
   #     list.append([tmp[i])
l=len(list)
ff=open('E:\\readyText.txt', "w")
for i in range (l):
    ff.writelines(list[i]+'\n')




print  len(list)


