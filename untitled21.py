from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Working on canvas using functions")
root.geometry("600x600")


color_label=Label(root,text="Enter a Color :")
color_label.place(relx=0.6,rely=0.9,anchor=CENTER)


input_box= Entry(root)
input_box.insert(0,"black")
input_box.place(relx=0.8,rely=0.9,anchor=CENTER)



canvas=Canvas(root,width = 590,height = 510,bg="white",highlightbackground="lightgray")


img = ImageTk.PhotoImage(Image.open("start_point1.png"))
my_image = canvas.create_image(50,50,image=img)

direction=""
oldx=50
oldy=50
newx=50
newy=50

def draw(direction,oldx,oldy,newx,newy):
    fill_color = input_box.get()
    if(direction=="right"):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
    if(direction=="left"):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
    if(direction=="up"):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
    if(direction=="down"):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)           
canvas.pack()
root.blind("<Right>",right_dir)
root.blind("<Left>",left_dir)
root.blind("<Up>",up_dir)
root.blind("<Down>",down_dir)
root.mainloop()