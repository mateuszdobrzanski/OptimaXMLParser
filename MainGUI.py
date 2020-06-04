from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import HendiParser, TomGastParser, RMGastroParser, FineDineParser, GrafenParser

# Prepare output after conversion
def show_conversion_info(status):
    if isinstance(status, int):
        message = "Przekonwertowano {} rekordów".format(status)
        messagebox.showinfo('Hendi', message)
    else:
        messagebox.showerror('Bład!', 'Niewłaściwy plik wejściowy')

# Create main window
window = Tk()
window.title("Optima XML Parser")
window.geometry('400x200')

selected = IntVar()

rad1 = Radiobutton(window,text='Hendi', value=1, variable=selected)
rad2 = Radiobutton(window,text='FineDine', value=2, variable=selected)
rad3 = Radiobutton(window,text='Grafen', value=3, variable=selected)
rad4 = Radiobutton(window,text='TomGast', value=4, variable=selected)
rad5 = Radiobutton(window,text='RMGastro', value=5, variable=selected)

# Convert XML to CSV
def clicked():
    selected_value = selected.get()

    # show an "Open" dialog box and return the path to the selected file
    filename = askopenfilename()
    file = str(filename)

    if selected_value == 1:
        status = HendiParser.hendi_parser(file.replace("/", "\\"))
        show_conversion_info(status)

    elif selected_value == 2:
        status = FineDineParser.fine_dine_parser(file.replace("/", "\\"))
        show_conversion_info(status)

    elif selected_value == 3:
        status = GrafenParser.grafen_parser(file.replace("/", "\\"))
        show_conversion_info(status)

    elif selected_value == 4:
        status = TomGastParser.tom_gast_parser(file.replace("/", "\\"))
        show_conversion_info(status)

    elif selected_value == 5:
        status = RMGastroParser.rm_gastro_parser(file.replace("/", "\\"))
        show_conversion_info(status)

    else:
        messagebox.showerror('Bład!', 'Nie wybrano typu pliku źródłowego.')


# Prepare layout
rad1.grid(column=1, row=1)
rad2.grid(column=1, row=2)
rad3.grid(column=1, row=3)
rad4.grid(column=1, row=4)
rad5.grid(column=1, row=5)

btn = Button(window, text="Parsuj", command=clicked)
btn.grid(column=1, row=7)

lbl = Label(window, text="Wybierz typ pliku źródłowego:")
lbl.grid(column=0, row=0)
lbl_blank = Label(window, text="")
lbl_blank.grid(column=0, row=6)

window.mainloop()
