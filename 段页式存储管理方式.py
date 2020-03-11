from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox

#段表[【段号，状态，页表大小（页的数量），页表始址】,【段号，状态，页表大小（页的数量），页表始址(对应着页表的页号)】...]
Segment=[]


#页表[【【页号，状态，块号】,【页号，状态，块号】...】,【【页号，状态，块号】,【页号，状态，块号】...】...]
Page=[]


#逻辑地址[段号，页号，页内地址]
LogicAddress=[]


#内存中的块[【块号，块内地址】,【块号，块内地址】...]
Memory=[]


#段表寄存器[段表大小（内存中段的数量），段表始址]
SegmentR=[]

window=Tk()
window.geometry('1000x600')
img=PhotoImage(file=r"背景图.png")
labelBg=Label(window,image=img)
labelBg.pack()
#输入框区@@@@@@@@@@@@@

#程序分段数量的输入

labelSegmentNum=Label(window,text="程序分段数：")
labelSegmentNum.place(x=20,y=500)
entrySegmentNum=Entry(window)
entrySegmentNum.place(x=100,y=500,width=50)

#段内分页数的输入

labelPageNum=Label(window,text="段内分页数：")
labelPageNum.place(x=170,y=500)
entryPageNum=Entry(window)
entryPageNum.place(x=250,y=500,width=50)

#内存分块数的输入
MemoryNum=StringVar()
labelMemoryNum=Label(window,text="内存分块数：")
labelMemoryNum.place(x=320,y=500)
entryMemoryNum=Entry(window)
entryMemoryNum.place(x=400,y=500,width=70)

#逻辑地址段号的输入

labelLogicSegmentNum=Label(window,text="逻辑地址段号：")
labelLogicSegmentNum.place(x=20,y=545)
entryLogicSegmentNum=Entry(window)
entryLogicSegmentNum.place(x=110,y=545,width=40)

#逻辑地址页号的输入

labelLogicPageNum=Label(window,text="逻辑地址页号：")
labelLogicPageNum.place(x=170,y=545)
entryLogicPageNum=Entry(window)
entryLogicPageNum.place(x=260,y=545,width=40)

#逻辑地址页内地址的输入

labelLogicPageinadd=Label(window,text="逻辑地址页内地址：")
labelLogicPageinadd.place(x=320,y=545)
entryLogicPageinadd=Entry(window)
entryLogicPageinadd.place(x=430,y=545,width=40)

#@@@@@@@@@@@@@@@@@@


#显示区&&&&&&&&&&&&&&&&&&&&
def treeSegmentClick(none):
      #负责显示鼠标点击段的页表内容(定义到前面,是因为有这个函数，页表才可以建立)
      delPageTable()
      a=treeSegment.selection()#得到一个元组
      b=treeSegment.item(a,"values")[0]
      b=int(b)
##      print(b)
      global Page
      listPage=Page[b]
      for i in listPage:
            treePage.insert('','end',values=i)
      

#建立段表
treeSegment=ttk.Treeview(window,columns=['0','1','2','3'],show='headings')
treeSegment.place(x=100,y=150,height=300)
treeSegment.column('0',width=40,anchor='center')
treeSegment.heading('0',text='段号')
treeSegment.column('1',width=40,anchor='center')
treeSegment.heading('1',text='状态')
treeSegment.column('2',width=80,anchor='center')
treeSegment.heading('2',text='页面大小')
treeSegment.column('3',width=80,anchor='center')
treeSegment.heading('3',text='页面始址')
treeSegment.bind('<ButtonRelease-1>',treeSegmentClick)



#建立段内页表
treePage=ttk.Treeview(window,columns=['0','1','2'],show='headings')
treePage.place(x=400,y=230,height=150)
treePage.column('0',width=40,anchor='center')
treePage.heading('0',text='页号')
treePage.column('1',width=40,anchor='center')
treePage.heading('1',text='状态')
treePage.column('2',width=40,anchor='center')
treePage.heading('2',text='块号')

#显示块号
treeMemory=ttk.Treeview(window,columns=['0','1'],show='headings')
treeMemory.place(x=800,y=150,height=250)
treeMemory.column('0',width=40,anchor='center')
treeMemory.heading('0',text='块号')
treeMemory.column('1',width=80,anchor='center')
treeMemory.heading('1',text='块内地址')

#段表寄存器
treeSegmentR=ttk.Treeview(window,columns=['0','1'],show='headings')
treeSegmentR.place(x=30,y=30,height=60)
treeSegmentR.column('0',width=80,anchor='center')
treeSegmentR.heading('0',text='段表始址')
treeSegmentR.column('1',width=80,anchor='center')
treeSegmentR.heading('1',text='段表长度')

#逻辑地址
treeLogicAdd=ttk.Treeview(window,columns=['0','1','2'],show='headings')
treeLogicAdd.place(x=800,y=30,height=60)
treeLogicAdd.column('0',width=40,anchor='center')
treeLogicAdd.heading('0',text='段号')
treeLogicAdd.column('1',width=40,anchor='center')
treeLogicAdd.heading('1',text='页号')
treeLogicAdd.column('2',width=80,anchor='center')
treeLogicAdd.heading('2',text='页内地址')

######最后物理地址######
labelFinally=Label(window,text="如果每页为1K,则最后物理地址为：")
labelFinally.place(x=600,y=450)
def Finally(num):
      labelFinally1=Label(window,text=num)
      labelFinally1.place(x=800,y=450)
####################
#&&&&&&&&&&&&&&&&&&&&&&&&


#创建段表和页表的过程￥￥￥￥￥￥￥￥￥￥


#建立段表
def BuildSegmentTable(SegmentNum1,PageNum1):
      global Segment
      pi=0
      for Segmenti in range(SegmentNum1):
            Segment.append([])
            Segment[Segmenti].append(Segmenti)
            Segment[Segmenti].append(1)
            Segment[Segmenti].append(PageNum1)
            Segment[Segmenti].append(pi)
            pi=pi+PageNum1
##            print(pi)
      for Segmentj  in Segment:
            treeSegment.insert('','end',values=Segmentj)
##      print('S:',Segment)

            
def delSegmentTable():
      #删除段表控件里的所有信息
      num=treeSegment.get_children()
      for i in num:
            treeSegment.delete(i)
            
#建立段内页表
def BuildPageTable(SegmentNum1,PageNum1):
      global Page
      for Segi in range(SegmentNum1):
            Page.append([])       
            for Pagei in range(PageNum1):
                  Page[Segi].append([])
                  Page[Segi][Pagei].append(Pagei)
                  Page[Segi][Pagei].append(1)
                  Page[Segi][Pagei].append('None')
##      print('P:',Page)
      for i in Page[0]:
            treePage.insert('','end',values=i)


      
def delPageTable():
      #删除页表控件里的所有信息
      num=treePage.get_children()
      for i in num:
            treePage.delete(i)


#￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥

#创建块表并显示在控件里*********
def BuildMemoryTable(MemoryNum1):
      global Memory
      for Memoryi in range (MemoryNum1):
            Memory.append([])
            Memory[Memoryi].append(Memoryi)
            Memory[Memoryi].append('None')
      for Memoryk in Memory:
            treeMemory.insert('','end',values=Memoryk)
##      print('M:',Memory)

            
def delMemoryTable():
      #删除块表Treeview里的所有信息
      num=treeMemory.get_children()
      for i in num:
            treeMemory.delete(i)
       
#*******************************

####################################################            
def buildSegmentR():
      #填入段表寄存器数据,并显示在Treeview控件里
      global SegmentR
      Segnum=0
      for i in range(len(Segment)):
            if Segment[i][1]==0:
                  Segnum+=1
      SegmentR=[0,Segnum]
      treeSegmentR.insert('','end',values=SegmentR)
      
def delSegmentR():
      #清空段表寄存器Treeview
      num=treeSegmentR.get_children()
      for i in num:
            treeSegmentR.delete(i)


def LogicAdd():
      #逻辑地址填入数据,并显示在treeview里
      global LogicAddress
      SegmentNum=int(entryLogicSegmentNum.get())
      PageNum=int(entryLogicPageNum.get())
      Pageinadd=int(entryLogicPageinadd.get())
      LogicAddress=[SegmentNum,PageNum,Pageinadd]
      treeLogicAdd.insert('','end',values= LogicAddress)
      entryLogicSegmentNum.delete(0,END)#清空输入框内容
      entryLogicPageNum.delete(0,END)#清空输入框内容
      entryLogicPageinadd.delete(0,END)#清空输入框内容
      
def delLogicAdd():
      #清空逻辑地址treeview里的信息
      num=treeLogicAdd.get_children()
      for i in num:
            treeLogicAdd.delete(i)

####################################################      

            
def BuildTable():
      #将输入数值录入并实现可视化
      SegmentNum1=int(entrySegmentNum.get())
      PageNum1=int(entryPageNum.get())
      MemoryNum1=int(entryMemoryNum.get())
      BuildSegmentTable(SegmentNum1,PageNum1)
      BuildPageTable(SegmentNum1,PageNum1)
      BuildMemoryTable(MemoryNum1)
      entrySegmentNum.delete(0,END)#清空输入框内容
      entryPageNum.delete(0,END)#清空输入框内容
      entryMemoryNum.delete(0,END)#清空输入框内容
##++++++将页调入块表中+++++++++++
def InputMemory():
      global Segment
      global Page
      global Memory
      Flag=True
      MemoryIsUsed=[]
      MemoryIsUsed=Memory.copy()#将块表的划分传给一个使用块表
      random.shuffle(MemoryIsUsed)#打乱块号的顺序
      for S in Segment:
            js=0
            for P in Page:
                        for i in  range(len(Page[0])):
                              if len(MemoryIsUsed):
                                    P[i][1]=0
                                    P[i][2]=MemoryIsUsed[0][0]#页得到打乱后的块表的第一个
                                    MemoryIsUsed.pop(0)#删除块表第一个
                              else:
                                    Flag=False
                                    break
                        if Flag:
                              Segment[js][1]=0
                              js=js+1      
                        else:
                              break
##      print(Segment)
      delPageTable()
      for i in Page[0]:
            treePage.insert('','end',values=i)
      delSegmentTable()
      for j in Segment:
            treeSegment.insert('','end',values=j)


def InputLogic():
      buildSegmentR()
      LogicAdd()

def FindMemory():
      global LogicAddress
      global SegmentR
      global Page
      global Memory
      if LogicAddress[0]<=SegmentR[1]:
            段号=LogicAddress[0]+SegmentR[0]
            页号=LogicAddress[1]
            if 页号>len(Page[0]):
                  messagebox.showerror(title="缺页",message="缺页中断")
                  DelAll()
                  return
            块号=Page[段号][页号][2]
            Memory[块号][1]=LogicAddress[2]#块内地址=页内地址
            num=块号*1024+LogicAddress[2]
            Finally(num)
            delMemoryTable()
            for Memoryk in Memory:
                  treeMemory.insert('','end',values=Memoryk)
            
      else:
            print('越界')
            messagebox.showerror(title="越界",message="所求逻辑地址未调入内存中")

def DelAll():
      global LogicAddress
      global SegmentR
      global Segment
      global Page
      global Memory
      LogicAddress.clear()
      SegmentR.clear()
      Segment.clear()
      Page.clear()
      Memory.clear()
      delSegmentTable()
      delPageTable()
      delMemoryTable()
      delSegmentR()
      delLogicAdd()
      
##+++++++++++++++++++++++


#@@@@@@@@按钮区@@@@@@@@
#生成段表页表块表按钮
buttonInput0=Button(window,text="生成段表页表块表",command=BuildTable)
buttonInput0.place(x=500,y=495)
#将页放入块中
buttonInput1=Button(window,text="将段页表装入块表",command=InputMemory)
buttonInput1.place(x=650,y=495)
#将逻辑地址放入并找到物理地址
buttonInput2=Button(window,text="放入逻辑地址",command=InputLogic)
buttonInput2.place(x=500,y=540)
#找物理地址
buttonInput2=Button(window,text="找物理地址",command=FindMemory)
buttonInput2.place(x=650,y=540)

#清空所有存储值
buttondel=Button(window,text="清空",command=DelAll)
buttondel.place(x=800,y=495,width=60,height=60)

#@@@@@@@@@@@@@@@@@@@


window.mainloop()



