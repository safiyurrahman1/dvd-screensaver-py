import tkinter
from random import uniform
import time

root = tkinter.Tk()
root.geometry("800x600")
root.configure(bg="black")
root.title("DVD thing")

class Logo():
    def __init__(self, x, y, imagePath) -> None:
        self.__image = tkinter.PhotoImage(file=imagePath)
        self.__imageLabel = tkinter.Label(root, image=self.__image, bg="black")
        
        self.x = x
        self.y = y
        self.__dx = 1
        self.__dy = 1

    def update(self):
        width = self.__imageLabel.winfo_reqwidth()

        if self.x >= root.winfo_width() - width:
            self.__dx = -uniform(0.5, 1)
        if self.x <= 0:
            self.__dx = uniform(0.5, 1)
        if self.y >= root.winfo_height() - (width / 2):
            self.__dy = -uniform(0.5, 1)
        if self.y <= 0:
            self.__dy = uniform(0.5, 1)

        self.x += self.__dx
        self.y += self.__dy

    def draw(self):
        bgTextLabel = tkinter.Label(root, text="@safiyurrahman1", bg="black", fg="grey", font=("Century Gothic", 20, "bold"))
        bgTextLabel.place(relx=0.5, rely=0.5, anchor="center")

        self.__imageLabel.lift(bgTextLabel)
        
        self.__imageLabel.place(x=self.x, y=self.y)
        self.update()
        self.__imageLabel.after(2, self.draw)

logo = Logo(400, 300, "./logo.png")
logo.draw()
tkinter.mainloop()