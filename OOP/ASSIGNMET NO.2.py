from tkinter import *
name = input("Please Enter your name: ")
dream_job = input("What is your dream job? ")
window = Tk()
window.title("Future Career")
window.geometry("500x300")
label = Label(window, text=" " + "\n" + " " + "\n" + " " + "\n" + name + "\n" + "<< " + dream_job + " >>", font=("Arial", 20, "bold"))
label.pack()
window.mainloop()
