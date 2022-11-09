import pandas, random
from tkinter import *
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
i=0
f=0
t=0
# ---------------------------- FLIPPING CARD SECTION ------------------------------- #

def show_answer():
    global i, t, f
    lang="English"
    txt = words[i][lang]
    flash_card.itemconfig(title, text=lang, fill="white")
    flash_card.itemconfig(word, text=txt, fill="white")
    flash_card.itemconfig(front_img, image=flash_card_img_back)
      
    



# ---------------------------- DATA SECTION ------------------------------- #
# list of dicts in {'Fr':value, 'Eng':value} format
data = pandas.read_csv('data/french_words.csv')
words = data.to_dict(orient="records")

# missed_words
words_to_learn = words
# shuffle the list each time
random.shuffle(words)

# generate new word 
def generate_word():
    global i, flip_timer
    lang = "French"
    window.after_cancel(flip_timer)
    try:
        txt = words[i][lang]
    except IndexError:
        messagebox.showinfo(title="Congrats", message="You've finished the word list")
    else:
        flash_card.itemconfig(title, text=lang, fill="black")
        flash_card.itemconfig(word, text=txt, fill="black")
        flash_card.itemconfig(front_img, image=flash_card_img)
        flip_timer = window.after(1500, func=show_answer)
    

def known_word():
    global i

    txt = words_to_learn[i]
    words_to_learn.remove(txt)
    df = pandas.DataFrame(words_to_learn)
    df.to_csv("words_to_learn.csv")
    generate_word()

# ---------------------------- UI SECTION ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=70, pady=80, bg=BACKGROUND_COLOR)
flip_timer = window.after(100, func=show_answer)


# flash_card img
flash_card_img = PhotoImage(file='images/card_front.png')
flash_card_img_back = PhotoImage(file='images/card_back.png')
# the flashcard canvas
flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = flash_card.create_image(400, 263, image=flash_card_img)
# canvas texts
title = flash_card.create_text(400, 150, text="", font=("Courier", 40, 'italic'))
word = flash_card.create_text(400, 260, text="", font=("Courier", 60, 'bold'))
flash_card.grid(row=1, column=1, columnspan=2)

# wrong and write buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, border=0, command=generate_word)
wrong_button.grid(row=2, column=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, border=0, command=known_word)
right_button.grid(row=2, column=2)

generate_word()

window.mainloop()

