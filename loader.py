import tkinter as tk
import random
import os
import sys

ATT = 0


def restart_program():
    py = sys.executable
    os.execl(py, py, *sys.argv)


def main():
    def engine(ATT, ST, EN):
        win = tk.Tk()
        win.config(bg="#00000F")
        win.title("Mini Game")
        win.geometry("310x155+800+400")
        win.resizable(False, False)

        def set(n=-5):
            global ATT
            if n > 1:
                ATT = n
            elif n == 1:
                ATT -= n
            elif n == 0:
                ATT = n
            elif n == -5:
                return ATT

        def comp(fie):
            try:
                data = int(fie.get())
                if data == num:
                    tk.Label(win, text="ПОЗДРАВЛЯЮ, ТЫ СМОГ!!!", padx=40, pady=20, font=('Arial', 13), fg="red",
                             bg="#00000F").grid(row=0, column=0)
                    tk.Button(win, text="Restars", command=lambda: restart_program(), padx=70, pady=20, bg="#00000F",
                              font=('Arial', 10), fg="red", bd=15).grid(row=1, column=0)
                else:
                    if data < ST:
                        tk.Label(win, text="Error, number oi out of bounds!!!", padx=70, font=('Arial', 7), fg="red",
                                 bg="#00000F").grid(row=5, column=0)
                    elif data > EN:
                        tk.Label(win, text="Error, number oi out of bounds!!!", padx=70, font=('Arial', 7), fg="red",
                                 bg="#00000F").grid(row=5, column=0)
                    elif data < num:
                        tk.Label(win, text="Попробуй взять число побольше)", padx=70, font=('Arial', 7), fg="red",
                                 bg="#00000F").grid(row=5, column=0)
                        set(1)
                    elif data > num:
                        tk.Label(win, text="Попробуй взять число поменьше)", padx=70, font=('Arial', 7), fg="red",
                                 bg="#00000F").grid(row=5, column=0)
                        set(1)
                    if set() == 0:
                        tk.Label(win, text="ПОПЫТОК БОЛЬШЕ НЕТ!!!", padx=70, font=('Arial', 10), fg="red",
                                 bg="#00000F").grid(row=5, column=0)
                        tk.Button(win, text="Restars", command=lambda: restart_program(), padx=70, pady=45,
                                  bg="#00000F", font=('Arial', 19), fg="red").grid(row=0, column=0)
                    tk.Label(win, text=f"Попыток: {set()}.", padx=70, font=('Arial', 10), fg="red", bg="#00000F").grid(
                        row=1, column=0)
            except:
                tk.Label(win, text="Введите корректное число.", padx=70, font=('Arial', 10), fg="red",
                         bg="#00000F").grid(row=5, column=0)
            fie.delete(0, tk.END)

        set(ATT)
        num = random.randint(ST, EN)
        tk.Label(win, text=f"Угадайте число от {ST} до {EN}.", padx=70, font=('Arial', 10), fg="red",
                 bg="#00000F").grid(row=0, column=0)
        tk.Label(win, text=f"Попыток: {ATT}.", padx=70, font=('Arial', 10), fg="red", bg="#00000F").grid(row=1,
                                                                                                         column=0)
        tk.Label(win, text="Поле ввода", padx=70, font=('Arial', 10), fg="red", bg="#00000F").grid(row=2, column=0)
        fie = tk.Entry(win, fg="black", bg="#990000")
        fie.grid(row=3, column=0, padx=80)
        tk.Button(win, text="ПРИНЯТЬ", command=lambda: comp(fie), padx=107, bg="#00000F", font=('Arial', 10), fg="red",
                  bd=10).grid(row=4, column=0)

        win.mainloop()

    win = tk.Tk()
    win.config(bg="#00000F")
    win.title("Mini Game")
    win.geometry("315x100+800+400")
    win.resizable(False, False)

    def run_1():
        win.destroy()
        engine(9, 1, 100)

    def run_2():
        win.destroy()
        engine(5, 1, 200)

    def run_3():
        win.destroy()
        engine(3, 1, 300)

    tk.Label(win, text="Выберете уровень сложности", padx=70, font=('Arial', 10), bg="#990000", fg="white").grid(row=0,
                                                                                                                 column=0)
    tk.Button(win, text="Легко", command=run_1, padx=107, bg="#AAAAAA").grid(row=1, column=0)
    tk.Button(win, text="Средне", command=run_2, padx=103, bg="#888888").grid(row=2, column=0)
    tk.Button(win, text="Сложно", command=run_3, padx=101, bg="#666666").grid(row=3, column=0)

    win.mainloop()


main()
