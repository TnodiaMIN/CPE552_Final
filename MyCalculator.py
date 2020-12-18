# Name: Congmin Sui
import tkinter

# Check if the input is legal.
def check(entry, argu):
    # Get input from Entry.
    input_data = entry.get()

    # Legal operators include: "+" "-" "*" "/" "--" "**" "//" "+-"
    # If the input is not legal, it won't be put in.
    if not input_data[-1:].isdecimal() and (not argu.isdecimal()):
        if input_data[-2:] in ["--", "**", "//", "+-"]:
            return
        if (input_data[-1:] + argu) not in ["--", "**", "//", "+-"]:
            return
    
    # If the input is legal, it will be put in and shown out.
    entry.insert("end", argu)

# Backspace
def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)

# Clear
def clear(entry):
    entry.delete(0, "end")

# Calculate
def calculate(entry):
    input_data = entry.get()

    # Cease if the input is empty.
    if not input_data:
        return

    clear(entry)

    # Exception handling
    try:
        # The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
        output_data = str(eval(input_data))
    except Exception:
        # Throw out
        entry.insert("end", "Input Error")
    else:
        # Show the result
        if len(output_data) > 20:
            entry.insert("end", "Value overflow")
        else:
            entry.insert("end", output_data)


if __name__ == '__main__':

    root = tkinter.Tk()
    root.title("Calculator")
    root.resizable(0, 0)

    button_bg = 'white'
    math_bg = 'lightblue'
    func_bg = 'lightgreen'
    button_active_bg = 'lightgrey'

    # Set the position and the size of Entry grid.
    entry = tkinter.Entry(root, justify="right", font=1)
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Define a function for new buttons to simplify the procedure.
    def new_button(text, func, func_params, bg=button_bg, **position_params):
        nb = tkinter.Button(root, text=text, command=lambda: func(*func_params), bg=bg, padx=10, pady=3, activebackground=button_active_bg)
        nb.grid(**position_params)

    # Bind the functions and characters to buttons. Then put the buttons in their positions and set different colors.
    new_button('<-', backspace, (entry,), bg=func_bg, row=1, column=0, ipadx=5, padx=5, pady=5)
    new_button('C', clear, (entry,), bg=func_bg, row=1, column=1, pady=5, ipadx=5)
    new_button('=', calculate, (entry,), bg=func_bg, row=1, column=2, ipadx=5, padx=5, pady=5, columnspan=2, sticky=tkinter.E + tkinter.W)
    new_button('7', check, (entry, '7'), row=2, column=0, ipadx=5, pady=5)
    new_button('8', check, (entry, '8'), row=2, column=1, ipadx=5, pady=5)
    new_button('9', check, (entry, '9'), row=2, column=2, ipadx=5, pady=5)
    new_button('4', check, (entry, '4'), row=3, column=0, ipadx=5, pady=5)
    new_button('5', check, (entry, '5'), row=3, column=1, ipadx=5, pady=5)
    new_button('6', check, (entry, '6'), row=3, column=2, ipadx=5, pady=5)
    new_button('1', check, (entry, '1'), row=4, column=0, ipadx=5, pady=5)
    new_button('2', check, (entry, '2'), row=4, column=1, ipadx=5, pady=5)
    new_button('3', check, (entry, '3'), row=4, column=2, ipadx=5, pady=5)
    new_button('0', check, (entry, '0'), row=5, column=0, padx=8, pady=5, columnspan=2, sticky=tkinter.E + tkinter.W)
    new_button('.', check, (entry, '.'), row=5, column=2, ipadx=7, padx=5, pady=5)
    new_button('+', check, (entry, '+'), bg=math_bg, row=2, column=3, ipadx=5, pady=5)
    new_button('-', check, (entry, '-'), bg=math_bg, row=3, column=3, ipadx=5, pady=5)
    new_button('*', check, (entry, '*'), bg=math_bg, row=4, column=3, ipadx=5, pady=5)
    new_button('/', check, (entry, '/'), bg=math_bg, row=5, column=3, ipadx=5, pady=5)

    root.mainloop()