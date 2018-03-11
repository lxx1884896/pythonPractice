#coding=utf-8
from tkinter import *
# root=Tk()
# girls=["西施","貂蝉","王昭君","杨贵妃"]
# v=[]
# for girl in girls:
#
#     v.append(IntVar())
#     b=Checkbutton(root,text=girl, variable=v[-1])
#     b.pack(anchor=W)
# mainloop()
root=Tk()
group=LabelFrame(root,text="最好的脚本语言是？",padx=40,pady=40)
group.pack(padx=100,pady=10)
langs=[("python",1),("perl",2),("ruby",3),("lua",4)]
v=IntVar()
v.set(1)
for a, c in langs:
    b=Radiobutton(group,text=a,variable=v,value=c)
    b.pack(anchor=W)
mainloop()



