from tkinter import *

#F = 9/5C + 32

def celsius_button():
    try:
        fahr_number = entryBoxFahr.get()
        fahr = float(fahr_number)
        celsius_answer = (fahr-32)*(5/9)

        entryBoxCel.delete(0, END)
        # entryBoxAnswer.delete(0, END)
        entryBoxCel.insert(0, format(celsius_answer, ",.2f") + " °C")

        fahr_button["state"] = DISABLED

    except:
        print("ValueError: User must enter values.")

def fahrenheight_button():
    try:
        celsius_number = entryBoxCel.get()
        cel = float(celsius_number)
        fahr_answer = (9/5)*cel + 32

        entryBoxFahr.delete(0, END)
        # entryBoxAnswer.delete(0, END)
        entryBoxFahr.insert(0, format(fahr_answer, ",.2f") + " °F")

        cel_button["state"] = DISABLED

    except:
        print("ValueError: User must enter values.")


def clear_button():
    #Clear all entry boxes
    entryBoxCel.delete(0, END)
    entryBoxFahr.delete(0, END)
    # entryBoxAnswer.delete(0, END)

    #Set state for other buttons
    cel_button["state"] = NORMAL
    fahr_button["state"] = NORMAL

root = Tk()
root.title("Temperature Converter")

#Title
titleLabel = Label(root, text="Temperature Converter")
titleLabel.grid(row=0, column=0, columnspan=3)

#Labels
celLabel = Label(text="Celsius(°C): ")
celLabel.grid(row=1, column=0)

fahrLabel = Label(text="Fahrenheit(°F): ")
fahrLabel.grid(row=2, column=0)

# answerLabel = Label(text="")
# answerLabel.grid(row=3, column=0)

#Entry boxes
entryBoxCel = Entry(root, width=30)
entryBoxCel.grid(row=1, column=1)

entryBoxFahr = Entry(root, width=30)
entryBoxFahr.grid(row=2, column=1)

# entryBoxAnswer = Entry(root, width=30)
# entryBoxAnswer.grid(row=3, column=1)

#Buttons
cel_button = Button(root, text="Celsius\n°F -> °C", padx=20, pady=20, command=celsius_button)
cel_button.grid(row=4, column=1, columnspan=1)

fahr_button = Button(root, text="Fahrenheit\n°C -> °F", padx=10, pady=20, command=fahrenheight_button)
fahr_button.grid(row=4, column=0, columnspan=1)

clear_button = Button(root, text="Clear\n", padx=20, pady=20, command=clear_button)
clear_button.grid(row=4, column=2, columnspan=1)

root.mainloop()
