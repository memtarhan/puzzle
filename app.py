from Tkinter import *
import time

window = Tk()

timer_label = Label(window, justify='center')


def countdown(counter):
    timer_label["text"] = "Time Left: {}".format(counter)
    if counter > 0:
        # call countdown again after 1000ms (1s)
        window.after(1000, countdown, counter - 1)
    else:
        timer_label["text"] = "GAME OVER"


def create():
    window.geometry("600x600")
    window.title("Balloons")
    window.config(background='black')
    timer_label.config(font=("Symbol", 44, 'bold'), background='black', foreground='red')
    timer_label.pack()
    countdown(5)
    window.mainloop()


if __name__ == '__main__':
    create()
