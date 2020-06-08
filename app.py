from Tkinter import *
import os
from tkinter.filedialog import askdirectory

timer_counter = 10
total_aim = 45
score = 0
level = 1
height = 1000
width = 1000

window = Tk()

timer_label = Label(window, justify='center')
total_aim_label = Label(window, justify='center')
score_label = Label(window, justify='center')
level_label = Label(window, justify='center')


def create_countdown():
    timer_label.config(font=("Helvetica", 64), background='black', foreground='red')
    timer_label.place(x=width / 2, y=44, anchor="center")
    countdown(timer_counter)


def create_total_aim():
    total_aim_label.config(font=("Helvetica", 64), background='black', foreground='green')
    total_aim_label.place(x=width / 2, y=128, anchor="center")
    total_aim_label["text"] = "Total Aim: {}".format(total_aim)


def create_score():
    score_label.config(font=("Helvetica", 64), background='black', foreground='orange')
    score_label.place(x=width / 2, y=height - 128, anchor="center")
    score_label["text"] = "Your score: {}".format(score)


def create_level():
    level_label.config(font=("Helvetica", 64), background='black', foreground='white')
    level_label.place(x=width / 2, y=height - 44, anchor="center")
    level_label["text"] = "Your at Level: {}".format(level)


def change_dir():
    song_list = []

    scriptDir = os.getcwd()  # directory from where script was ran
    directory = askdirectory()
    os.chdir(directory)

    for file in os.listdir(directory):
        if file.endswith('.mp3'):
            realdir = os.path.realpath(file)
            song_list.append(file)

    os.chdir(scriptDir)


def create_balloon():
    render = Image.open('balloon.png')
    image = PhotoImage(file=render)
    button = Button(window, text="34", image=image, compound='center')
    button.place(x=width / 2, y=height - 256, anchor="center")


def countdown(counter):
    timer_label["text"] = "Time Left: {}".format(counter)
    if counter > 0:
        # call countdown again after 1000ms (1s)
        window.after(1000, countdown, counter - 1)
    else:
        timer_label.place(x=height / 2, y=width / 2, anchor="center")
        timer_label["text"] = "GAME OVER"
        # TODO: Implement Game Over logic


def create():
    window.geometry("{}x{}".format(height, width))
    window.title("Balloons")
    window.config(background='black')

    create_countdown()
    create_total_aim()
    create_score()
    create_level()

    create_balloon()

    window.mainloop()


if __name__ == '__main__':
    create()
