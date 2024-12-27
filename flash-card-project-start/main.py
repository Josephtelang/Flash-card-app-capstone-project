from tkinter import *
import random
import pandas



BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flash Card App")
window.config(padx=40,pady=40,bg=BACKGROUND_COLOR)



canvas = Canvas(width=800,height=600,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

current_card ={}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError :
    data = pandas.read_csv("./data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# print(data_list)
# print(data.Japanese)
# if right_button is clicked:

def is_known_cards():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv",index=False)
    
def next_card():
    global flip_timer,current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(word_title,text="French",fill="black")
    canvas.itemconfig(word_text,text=current_card["French"] ,fill="black")
    canvas.itemconfig(card_background,image=card_front)
    flip_timer = window.after(3000,flip_card)
    
  
    

def flip_card():
    # print(random_index)
    canvas.itemconfig(word_title,text=f"English",fill="white")
    canvas.itemconfig(word_text,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back)

flip_timer = window.after(3000,flip_card)
    
card_background = canvas.create_image(400,263,image=card_front)
canvas.grid(row=0,column=0,columnspan=2)
word_title = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))

word_text = canvas.create_text(400,263,text=f"" ,font=("Arial",40,"bold"))


wrong_button = Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

right_button = Button(image=right_img,highlightthickness=0,command=is_known_cards)
right_button.grid(row=1,column=1)

next_card()

window.mainloop()

