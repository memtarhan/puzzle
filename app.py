from Tkinter import *

height = 1000
width = 1000

window = Tk()

timer_label = Label(window, justify='center')


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
    timer_label.config(font=("Helvetica", 64, 'bold'), background='black', foreground='red')
    timer_label.place(x=width / 2, y=44, anchor="center")
    countdown(5)
    window.mainloop()


if __name__ == '__main__':
    create()
