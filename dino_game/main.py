from tkinter import *
from PIL import ImageTk, Image
from time import sleep 
from playsound import *
def jump():
    global check_jump
    if check_jump == False:
        playsound("tick.wav",block=False)
        check_jump = True
        for  i in range(30):
            canvas.move(dragon_img,0,-5)
            move_cloud()
            move_tree()
            canvas.update()
            sleep(0.01)
        for i in range(30):
            canvas.move(dragon_img,0,5)
            move_cloud()
            move_tree()
            canvas.update()
            sleep(0.01)
        check_jump = False
        
    
def key_press(event):
    if event.keysym == "space":
        jump()

        

def move_cloud():
    global cloud_img
    canvas.move(cloud_img,-5,0)
    cloud_x = canvas.coords(cloud_img)[0]
    if cloud_x <= -20:
        canvas.delete(cloud_img)
        cloud_img = canvas.create_image(550,50,anchor=NW,image=imgs[1])
    canvas.update()

def move_tree(): 
    global tree_img,score
    canvas.move(tree_img,-5,0)
    tree_x = canvas.coords(tree_img)[0]
    if tree_x <= -20:
        canvas.delete(tree_img)
        tree_img = canvas.create_image(550,250,anchor=NW,image=imgs[2])
        score+=1
        canvas.itemconfig(text_score,text="SCORE: "+str(score))
    canvas.update()

def check_game_over():
    global game_over,score
    if canvas.coords(tree_img)[0] < 50 and canvas.coords(dragon_img)[1] > 220:  
            canvas.itemconfig(text_game_over,text="GAME OVER")
            game_over = True
            score = 0
            playsound("te.wav",block=False)
    game_window.after(100,check_game_over)



  
    

if __name__ == '__main__':
    score = 0 
    check_jump = False
    game_over = False
    imgs= [0,0,0]
    game_window = Tk()
    game_window.title("Dinosaur Game")
    canvas = Canvas(master = game_window, width = 600, height = 300, background = "white")
    canvas.pack()
    imgs[0] = ImageTk.PhotoImage(Image.open("photos/dragon.jpg"))
    imgs[1] = ImageTk.PhotoImage(Image.open("photos/cloud.jpg"))
    imgs[2] = ImageTk.PhotoImage(Image.open("photos/tree.jpg"))

    dragon_img = canvas.create_image(0,250,anchor=NW,image=imgs[0])
    canvas.bind_all("<KeyPress>",key_press)
    cloud_img = canvas.create_image(550,50,anchor=NW,image=imgs[1])
    tree_img = canvas.create_image(550,250,anchor=NW,image=imgs[2])
    line = canvas.create_line(0,290,600,290)
    text_score = canvas.create_text(50,20,fill="red",font=("Times",10))
    text_game_over = canvas.create_text(300,150,fill="red",font=("Times",30))
    canvas.itemconfig(text_score,text="SCORE: "+str(score))
    canvas.update()

    check_game_over()
    while not game_over:
        move_cloud()
        move_tree()
        sleep(0.01)
        

    game_window.mainloop()