#프레임(Frame) 위젯은 다른 위젯을 담을수있는 컨테이너 역할을 한다.

from tkinter import*

root=Tk()
root.geometry("300x200")

frame=Frame(root,width=200,height=100)
frame.pack()

button1=Button(frame,text="버튼 1")
button1.pack(side="left")

button2=Button(frame,text="버튼 2")
button2.pack(side="left")

root.mainloop()