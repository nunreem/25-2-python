import tkinter as  tk
import random
import time

#작성시작 **이만큼을니가써야돼유림아**
def animate_text(canvas,text_id):
    for i in range(10):
        update_text_size(canvas,text_id)

def update_text_size(canvas,text_id):
    current_size=100
    new_size =current_size + random.randint(-100,100)
    canvas.itemconfigure(text_id,font=("Helvetica",new_size))

def update_text_color(canvas,text_id):
    colors=["red","yellow","green","pink"]
    new_color=random.choice(colors)
    canvas.itemconfigure(text_id,fill=new_color)

#애플리케이션 초기 설정
root=tk.Tk()
root.title("Text Animation")

canvas = tk.Canvas(root, width=400, height = 200)
canvas.pack()

text_id=canvas.create_text(200,100,text="Hello", font=("Helvetica",12),fill="black")

animate_text(canvas, text_id)

root.mainloop()