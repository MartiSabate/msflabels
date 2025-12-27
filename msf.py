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

# default tkinter values declaration

## configure test mode

TEST_RUN = False
#TEST_RUN = False

#rentar = tkinter.StringVar(value="RENTAR")
unica = tkinter.StringVar(value="UNICA")

if TEST_RUN:

    print("Running in TEST MODE")
    ## test values declaration
    test_value1 = tkinter.StringVar(value="NEPAL")
    test_value2 = tkinter.StringVar(value="5454/6")
    test_value3 = unica
    test_value4_odd = tkinter.IntVar(value=1213)
    test_value4_even = tkinter.IntVar(value=12)
    test_value5_odd = tkinter.IntVar(value=31)
    test_value5_even = tkinter.IntVar(value=12)
    test_value6 = tkinter.StringVar(value="PARAM1")
    test_value7 = tkinter.StringVar(value="331-NEGRE")
    test_value8 = tkinter.StringVar(value="RENTAT")
    test_value9 = tkinter.StringVar(value="PLANXAT")

    param1entry = tkinter.Entry(frame1, textvariable=test_value1)
    param1entry.grid(row=0, column=1)
    param2entry = tkinter.Entry(frame1, textvariable=test_value2)
    param2entry.grid(row=1, column=1)
    param3entry = tkinter.Entry(frame1, textvariable=test_value3)
    param3entry.grid(row=2, column=1)
    param4entry = tkinter.Entry(frame1, textvariable=test_value4_even)
    param4entry.grid(row=3, column=1)
    param5entry = tkinter.Entry(frame1, textvariable=test_value5_even)
    param5entry.grid(row=3, column=3)
    param6entry = tkinter.Entry(frame1, textvariable=test_value6)
    param6entry.grid(row=4, column=1)
    param7entry = tkinter.Entry(frame1, textvariable=test_value7)
    param7entry.grid(row=5, column=1)
    param8entry = tkinter.Entry(frame1, textvariable=test_value8)
    param8entry.grid(row=6, column=1)
    param9entry = tkinter.Entry(frame1, textvariable=test_value9)
    param9entry.grid(row=7, column=1)

else:
    
    print("Running in PROD mode")
    # define and print text entry boxes for prod

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
    param8entry = tkinter.Entry(frame1)
    param8entry.grid(row=6, column=1)
    param9entry = tkinter.Entry(frame1)
    param9entry.grid(row=7, column=1)



# declare position lists globally
# left column -> x = 10, right column -> x = 110
# first position -> y = 7, second position -> y = 97, third position y = 187
pos_left_first = [10, 7]    # left first
pos_left_second = [10, 97]   # left second
pos_left_third = [10, 187]  # left third
pos_right_first = [110, 7]   # right first
pos_right_second = [110, 97]  # right second
pos_right_third = [110, 187] # right third

# function to print the O
def print_o(pdf, font_size):
    pdf.set_font('courier', 'B', font_size)
    pdf.multi_cell(100, 7, "\t\t\t\t\t\t\t\t\tO\n")

# function to print a blank line
def print_blank_line(pdf):
    pdf.multi_cell(100, 7, "")

# function to determine the position

def determine_position(iteration):
    match positions := iteration % 6:
        case 0:
            return pos_left_first
        case 1:
            return pos_right_first
        case 2:
            return pos_left_second
        case 3:
            return pos_right_second
        case 4:
            return pos_left_third
        case 5:
            return pos_right_third
        case _:
            return pos_left_first

#print_lines function definition

def print_lines(pdf, font_size, params, position, iteration):  
    x, y = position
    left_padding = 10 # configure left padding in order to center the text

    pdf.set_xy(x, y)  # set start position once

    for idx, j in enumerate(params):
        if idx == 3 or idx == 5 or idx == 6 or idx == 7: # add padding to the position
            pdf.set_x(x+left_padding)
        else:
            pdf.set_x(x)  # multi_cell resets X to margin; force column X each line
        pdf.set_font('courier', '', font_size)
        # 0 = NEPAL
        # 1 = ARTICLE
        # 2 = TALLA
        # 3 = CNT
        # 4 = PARAM1
        # 5 = COLOR
        # 6 = RENTAT
        # 7 = PLANXAT
        match idx: # switch case alternative
            case 1:
                pdf.set_font('courier', '', font_size)
                label = "Art "
                w = pdf.get_string_width(label) + 2  # +2 is padding (tweak 1–4)
                pdf.cell(w, 7, label, ln=0) # print on pdf without jump line

                pdf.set_font('courier', 'B', font_size)
                pdf.cell(0, 7, str(j), ln=1) #print on the same line
                continue
            
            case 2: #print the content and a blank line
                pdf.multi_cell(100, 7, j)  # no "\n" needed
                pdf.set_x(x)
                print_blank_line(pdf)
                continue
            case 5 | 6 | 7:
                if idx == 5:
                    pdf.set_font('courier', 'B', font_size)
                pdf.set_x(x + left_padding)  # add left padding

            case _:
                # Equivalent to the else branch
                pdf.set_font('courier', '', font_size)

        pdf.multi_cell(100, 7, j)  # no "\n" needed
        if idx == 3: #print O after the indicated position idx
            pdf.set_x(x)
            print_o(pdf, font_size)

    # separator goes AFTER the loop at the current Y
    pdf.set_font('courier', '', font_size)
    pdf.set_x(x)
    pdf.multi_cell(100, 7, f"{iteration+1}\n__________________")

#print_Data function definition

def print_data(params, iters):
    # generate PDF object
    pdf = FPDF('P', 'mm', 'A4')
    font_size = 15
    #exctract last quantity value
    lastQuantity = str(params[9])
    params.pop(-1) #remove last quantity from params list for now
    # define PDF atributes (reconfigured during the execution)
    pdf.set_font('courier', '', font_size) # configure font and size
    pdf.set_auto_page_break(auto=True, margin = 15) # configure auto page break
    pdf.add_page() # add a page
    params.pop(-1) #remove last quantity from params list
    iters -= 1 #adjust iterations
    for i in range(iters):
        print("i value is: " + str(i))
        #determine position
        pos = determine_position(i)
        print("position selected is: " + str(pos))
        print_lines(pdf, font_size, params, pos, i)
        #after 6 labels, add a new page
        if (i+1)%6 == 0 and i != 0:
            print("new page added")
            pdf.add_page()
    #after all iterations, print last output if required
    if lastQuantity != "0":
        params[3] = lastQuantity #restore last quantity value
        print("printing last output")
        #determine position
        pos = determine_position(iters)
        print("position selected is: " + str(pos))
        print_lines(pdf, font_size, params, pos, iters)
    
    tmp_path = os.path.expandvars(r"%TMP%\pdf_1.pdf") # retrieve temporal os path
    
    pdf.output(tmp_path) #save pdf to temporal path over the last one if exists
    os.startfile(tmp_path) # print pdf
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
        param2 = param2entry.get()
        param3 = "Talla " + param3entry.get()
        param4 = "Cnt " + param5entry.get()
        #param4 = "Cantidad: " + str(int(int(param4entry.get())/int(param5entry.get())))
        
        param5 = param6entry.get() # preguntar que fer
        param6 = param7entry.get()
        param7 = param8entry.get() # preguntar que fer
        param8 = param9entry.get() # preguntar que fer
        param9 = param5entry.get() # quantitat / grups de

        #calculate modulus+quantity value as int
        modulusQuantity = 0
        modulus = int(param4entry.get())%int(param5entry.get())
        if modulus != 0:
            if int(param4entry.get()) > int(param5entry.get()):
                modulusQuantity = "Cnt " + str(int(param4entry.get())%int(param5entry.get()))
            else:                    
                modulusQuantity = "Cnt " + str(int(param4entry.get())%int(param5entry.get())+int(param5entry.get()))
        #modulusQuantity = "Cantidad: " + str(int(param4entry.get())%int(param5entry.get())+int(int(param4entry.get())/int(param5entry.get())))
        print("Modulus + quantitat = " + str(modulusQuantity))
        params = [param1, param2, param3, param4, param5, param6, param7, param8, param9, modulusQuantity]
        print("Input validatin ok, printing")

        # calculate iterations per quantity (see above param 9)
        iterations = int(int(param4entry.get())/int(param5entry.get()))
        if (int(param4entry.get())%int(param5entry.get())) != 0:
            print("sum 1 to iterations")
            iterations += 1
            print("iterations: " + str(iterations))
        else:
            print("sum 1 to iterations ")
            iterations += 1

        #after validation successfull print data
        print_data(params, iterations)

# when the button is clicked, the function print_data will be executed
button = tkinter.Button(frame, text="Imprimir", command = validate_data)
button.grid(row=1, column=0)

# run/open the tk inter application window
window.mainloop()