from Tkinter import *
from ui import RoundedButton
import random

timer_counter = 3
total_aim = 45
scores = []
level = 1
height = 1000
width = 1000

window = Tk()

timer_label = Label(window, justify='center')
total_aim_label = Label(window, justify='center')
score_label = Label(window, justify='center')
level_label = Label(window, justify='center')
best_score_label = Label(window, justify='center')

balloons = []


def get_score():
    m_score = 0
    for score in scores:
        m_score += score

    return m_score


def on_click(event, title):
    event.widget.destroy()
    scores.append(int(title))
    score = get_score()
    if score >= total_aim:
        create()
    else:
        score_label["text"] = "Your score: {}".format(get_score())


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
    score_label["text"] = "Your score: {}".format(0)


def create_level():
    level_label.config(font=("Helvetica", 64), background='black', foreground='white')
    level_label.place(x=width / 2, y=height - 44, anchor="center")
    level_label["text"] = "Your at Level: {}".format(level)

def create_best_score():
    level_label.config(font=("Helvetica", 64), background='black', foreground='white')
    level_label.place(x=width / 2, y=height - 300, anchor="center")
    level_label["text"] = "Best score: {}".format(540)

def create_balloons():
    aim_mean = total_aim / 5
    for index in range(0, 5):
        aim_random = random.randint(0, 5)

        x = random.randint(0, width / 2)
        y = random.randint(0, height / 2)

        create_balloon(x, y, "{}".format(aim_random * aim_mean))


def create_balloon(x, y, title):
    balloon = RoundedButton(window, 96, 96, 0, 'red', title)
    balloon.place(x=x, y=y, anchor="center")
    balloon.bind("<Double-1>", lambda event, title=title: on_click(event, title))
    balloons.append(balloon)


def countdown(counter):
    timer_label["text"] = "Time Left: {}".format(counter)
    if counter > 0:
        # call countdown again after 1000ms (1s)
        window.after(1000, countdown, counter - 1)
    else:
        timer_label.place(x=height / 2, y=width / 2, anchor="center")
        timer_label["text"] = "GAME OVER"
        create_best_score()
        total_aim_label.destroy()
        for balloon in balloons:
            balloon.destroy()
        # TODO: Implement Game Over logic


def create():
    window.geometry("{}x{}".format(height, width))
    window.title("Balloons")
    window.config(background='black')

    create_countdown()
    create_total_aim()
    create_score()
    create_level()

    balloons = []
    create_balloons()

    window.mainloop()


if __name__ == '__main__':
    create()
