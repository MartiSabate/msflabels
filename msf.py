import tkinter
from fpdf import FPDF
import os


# parent window
window = tkinter.Tk()
# set window title
window.title("Etiquetes de producció")
# set window size 
#window.geometry("500x500") 


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

# default tkinter values

rentar = tkinter.StringVar(value="RENTAR")
unica = tkinter.StringVar(value="UNICA")


# define and print text entry boxes

param1entry = tkinter.Entry(frame1)
param1entry.grid(row=0, column=1)
param2entry = tkinter.Entry(frame1)
param2entry.grid(row=1, column=1)
param3entry = tkinter.Entry(frame1, textvariable=unica)
param3entry.grid(row=2, column=1)
param4entry = tkinter.Entry(frame1)
param4entry.grid(row=3, column=1)
param5entry = tkinter.Entry(frame1)
param5entry.grid(row=3, column=3)
param6entry = tkinter.Entry(frame1)
param6entry.grid(row=4, column=1)
param7entry = tkinter.Entry(frame1)
param7entry.grid(row=5, column=1)
param8entry = tkinter.Entry(frame1, textvariable=rentar)
param8entry.grid(row=6, column=1)
param9entry = tkinter.Entry(frame1)
param9entry.grid(row=7, column=1)


# print button

#print_Data function definition

def print_data(params, iters):
    #exctact last quantity value
    lastQuantity = str(params[9])
    lastOutput = ""
    params.pop(-1)
    # define PDF
    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_font('helvetica', '', 20)
    pdf.set_auto_page_break(auto=True, margin = 15)
    # add a page
    pdf.add_page()
    # add info (100,70) < wide, high
    # Configuration
    left_x = 10 # left column
    right_x = 110  # right column
    y = 7
    #retrieve iterations based on input
    iterations = int(params[8]) #idk what is this
    params.pop(-1)
    #generate label output
    output = ""
    for values in params: #generate multi_cell value
        output += values + "\n"
    
    #generate last output string if different to 0
    if lastQuantity != "0":
        print("last quantity value = " + str(lastQuantity))
        params[3] = lastQuantity
        for values in params: #generate multi_cell value
            lastOutput += values + "\n"
    #print output on screen
    #for i in range(iterations):
    for i in range(iters):
        print("i value is: " + str(i))
        print("range iterations values is: " + str(range(iters)))
        if i+1 == iters and lastQuantity != "0":
            output = lastOutput
        #final output based on the iteration
        iteration_output = output + str(i+1) + "\n__________________"
        #cursor add value each iteration
        cursorAdd = 90
        if (i % 2) == 0:
            if i != 0:
                y += cursorAdd # adjust cursor y as corresponding per its iteration
                if i % 6 == 0:
                    y -= cursorAdd
                print(pdf.get_y())            
                # Left column
                pdf.set_xy(left_x, y)
                pdf.multi_cell(100, 7, iteration_output)
            else:
                print(pdf.get_y())            
                # Left column
                pdf.set_xy(left_x, y)
                pdf.multi_cell(100, 7, iteration_output)
        else:
            # Right column
            pdf.set_xy(right_x, y)
            pdf.multi_cell(100, 7, iteration_output)
            if pdf.get_y() == 257:  # A4 pages have a height of 297 mm, minus margins (~10mm top/bottom)
                pdf.add_page()
                y = 7  # Reset y to the top of the new page
        # print
        #pdf.multi_cell(100, 7, iteration_output)
        # Check if y is getting close to the bottom of the page
    

    # retrieve temporal os path
    tmp_path = os.path.expandvars(r"%TMP%\pdf_1.pdf")
    #save pdf
    pdf.output(tmp_path)
    # print pdf
    #os.startfile(tmp_path, "print")
    os.startfile(tmp_path)
    print("done")

#validate_data function definition
def validate_data():
        # set a maximum amount of characters per parameter
        charLimit = 30
        #print(type(param1entry.get()))
        #print("Length: " + str(len(param1entry.get())))
        print("Input validation test ongoing")
        if len(param1entry.get()) > charLimit:
            print("param1 failed")
            exit(1)
        if len(param2entry.get()) > charLimit:
            print("param2 failed")
            exit(1)
        if len(param3entry.get()) > charLimit:
            print("param3 failed")
            exit(1)
        if len(param4entry.get()) > charLimit:
            print("param4 failed")
            exit(1)
        if len(param5entry.get()) > charLimit:
            print("param5 failed")
            exit(1)
        if len(param6entry.get()) > charLimit:
            print("param6 failed")
            exit(1)
        if len(param7entry.get()) > charLimit:
            print("param7 failed")
            exit(1)
        if len(param8entry.get()) > charLimit:
            print("param8 failed")
            exit(1)
        if len(param9entry.get()) > charLimit:
            print("param9 failed")
            exit(1)
        # define output values
        param1 = param1entry.get() # preguntar que fer
        param2 = "Articulo: " + param2entry.get()
        param3 = "Talla: " + param3entry.get()
        param4 = "Cantidad: " + param5entry.get()
        #param4 = "Cantidad: " + str(int(int(param4entry.get())/int(param5entry.get())))
        
        param5 = "***: " + param6entry.get() # preguntar que fer
        param6 = "Color: " + param7entry.get()
        param7 = "***: " + param8entry.get() # preguntar que fer
        param8 = "***: " + param9entry.get() # preguntar que fer
        param9 = param5entry.get() # quantitat / grups de

        #calculate modulus+quantity value as int
        modulusQuantity = 0
        modulus = int(param4entry.get())%int(param5entry.get())
        if modulus != 0:
            if int(param4entry.get()) > int(param5entry.get()):
                modulusQuantity = "Cantidad: " + str(int(param4entry.get())%int(param5entry.get()))
            else:                    
                modulusQuantity = "Cantidad: " + str(int(param4entry.get())%int(param5entry.get())+int(param5entry.get()))
        #modulusQuantity = "Cantidad: " + str(int(param4entry.get())%int(param5entry.get())+int(int(param4entry.get())/int(param5entry.get())))
        print("Modulus + quantitat = " + str(modulusQuantity))
        params = [param1, param2, param3, param4, param5, param6, param7, param8, param9, modulusQuantity]
        print("Input validatin ok, printing")

        # calculate iterations
        iterations = int(int(param4entry.get())/int(param5entry.get()))
        if (int(param4entry.get())%int(param5entry.get())) != 0:
            print("sum 1 to iterations")
            iterations += 1
            print("iterations: " + str(iterations))

        #after validation successfull print data
        print_data(params, iterations)

# when the button is clicked, the function print_data will be executed
button = tkinter.Button(frame, text="Imprimir", command = validate_data)
button.grid(row=1, column=0)

# run/open the tk inter application window
window.mainloop()