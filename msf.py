import tkinter
from fpdf import FPDF
import os



# parent window
window = tkinter.Tk()
# set window title
window.title("Etiquetes de producció")
# set window size 
window.geometry("500x500") 


# create frame inside the window (hiererchally)
frame = tkinter.Frame(window)
# resize frame as per its content
frame.pack()

# save print the frame
frame1 = tkinter.LabelFrame(frame, text="Manufacturas Sabaté")
frame1.grid(row=0, column=0, padx=20, pady=20)

#define and print labels

param1label = tkinter.Label(frame1, text="**")
param1label.grid(row=0, column=0)
param2label = tkinter.Label(frame1, text="Article")
param2label.grid(row=1, column=0)
param3label = tkinter.Label(frame1, text="Talla")
param3label.grid(row=2, column=0)
param4label = tkinter.Label(frame1, text="Quantitat")
param4label.grid(row=3, column=0)
param5label = tkinter.Label(frame1, text="Grups de")
param5label.grid(row=3, column=2)
param6label = tkinter.Label(frame1, text="**")
param6label.grid(row=4, column=0)
param7label = tkinter.Label(frame1, text="Color")
param7label.grid(row=5, column=0)
param8label = tkinter.Label(frame1, text="**")
param8label.grid(row=6, column=0)
param9label = tkinter.Label(frame1, text="**")
param9label.grid(row=7, column=0)


# define and print text entry boxes

param1entry = tkinter.Entry(frame1)
param1entry.grid(row=0, column=1)
param2entry = tkinter.Entry(frame1)
param2entry.grid(row=1, column=1)
param3entry = tkinter.Entry(frame1)
param3entry.grid(row=2, column=1)
param4entry = tkinter.Entry(frame1)
param4entry.grid(row=3, column=1)
param5entry = tkinter.Entry(frame1)
param5entry.grid(row=3, column=3)
param6entry = tkinter.Entry(frame1)
param6entry.grid(row=4, column=1)
param7entry = tkinter.Entry(frame1)
param7entry.grid(row=5, column=1)
param8entry = tkinter.Entry(frame1)
param8entry.grid(row=6, column=1)
param9entry = tkinter.Entry(frame1)
param9entry.grid(row=7, column=1)


# print button

#print_Data function definition

def print_data(params):
    # define PDF
    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_font('helvetica', '', 10)
    pdf.set_auto_page_break(auto=True, margin = 10)
    # add a page
    pdf.add_page()
    # add info (100,70) < wide, high
    # Configuration
    left_x = 10 # left column
    right_x = 110  # right column
    y = 7
    #retrieve iterations based on input
    iterations = int(params[8])
    params.pop(-1)
    #generate label output
    output = ""
    for values in params: #generate multi_cell value
        output += values + "\n"
    #print output on screen
    for i in range(iterations):
        #final output based on the iteration
        iteration_output = output + str(i+1) + "\n_____________________________________"
        if (i % 2) == 0:
            if i != 0:
                y += 70 # adjust cursor y as corresponding per its iteration
            # Left column
            pdf.set_xy(left_x, y)
        else:
            # Right column
            pdf.set_xy(right_x, y)
        # print
        pdf.multi_cell(100, 7, iteration_output, ln=True)
    
    #save pdf
    pdf.output('pdf_1.pdf')
    # print pdf
    os.startfile("/home/mozzard/Documents/labels/pdf_1.pdf", "print")
    print("done")

#validate_data function definition
def validate_data():
        #print(type(param1entry.get()))
        #print("Length: " + str(len(param1entry.get())))
        print("Input validation test ongoing")
        if len(param1entry.get()) > 10:
            print("param1 failed")
            exit(1)
        if len(param2entry.get()) > 10:
            print("param2 failed")
            exit(1)
        if len(param3entry.get()) > 10:
            print("param3 failed")
            exit(1)
        if len(param4entry.get()) > 10:
            print("param4 failed")
            exit(1)
        if len(param5entry.get()) > 10:
            print("param5 failed")
            exit(1)
        if len(param6entry.get()) > 10:
            print("param6 failed")
            exit(1)
        if len(param7entry.get()) > 10:
            print("param7 failed")
            exit(1)
        if len(param8entry.get()) > 10:
            print("param8 failed")
            exit(1)
        if len(param9entry.get()) > 10:
            print("param9 failed")
            exit(1)
        # define output values
        param1 = "GTE: " + param1entry.get() # preguntar que fer
        param2 = "Articulo: " + param2entry.get()
        param3 = "Talla: " + param3entry.get()
        param4 = "Cantidad: " + param5entry.get()
        param5 = "Color: " + param6entry.get() # preguntar que fer
        param6 = "??1: " + param7entry.get()
        param7 = "??2: " + param8entry.get()
        param8 = "??3: " + param9entry.get()
        param9 = int(param4entry.get())/int(param5entry.get())

        params = [param1, param2, param3, param4, param5, param6, param7, param8, param9]
        print("Input validatin ok, printing")
        #after validation successfull print data
        print_data(params)

# when the button is clicked, the function print_data will be executed
button = tkinter.Button(frame, text="Imprimir", command = validate_data)
button.grid(row=1, column=0)

# run/open the tk inter application window
window.mainloop()