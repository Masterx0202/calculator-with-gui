import tkinter as tk

window = tk.Tk()
window.title('Calculator')
window.geometry("430x500")

a = []
act = "+"
b = []
mainlist = a
blocker = False
operator_count = 0

def button_click(value):
    global mainlist, act, blocker, operator_count

    if value in ["+", "-", "*", "/"]:
        operator_count += 1
        if operator_count > 1:
            return 
        act = value
        mainlist = b if len(a) > 0 else a 
    else:
        mainlist.append(value)

    text.config(state=tk.NORMAL)
    text.insert(tk.END, value)
    text.config(state=tk.DISABLED)

def convert_list_to_float(num_list):
    num_str = ''.join(num_list)
    return float(num_str)

def calculate():
    global a, b, act, mainlist, operator_count

    num1 = convert_list_to_float(a)
    num2 = convert_list_to_float(b)

    if act == "+":
        result = num1 + num2
    elif act == "-":
        result = num1 - num2
    elif act == "*":
        result = num1 * num2
    elif act == "/":
        if num2 == 0:
            result = "Error: Division by zero"
        else:
            result = num1 / num2

    text.config(state=tk.NORMAL)
    if isinstance(result, str):
        text.insert(tk.END, result + "\n")
    else:
        text.insert(tk.END, f"={result}\n")
    text.config(state=tk.DISABLED)

    a = [str(result)]
    b = []
    mainlist = a
    operator_count = 0

def clear():
    global a, b, mainlist, operator_count
    text.config(state=tk.NORMAL)
    text.delete("1.0", tk.END)
    text.config(state=tk.DISABLED)
    a.clear()
    b.clear()
    mainlist = a
    operator_count = 0

text = tk.Text(window, height=3, width=33)
text.place(x=30, y=10)
text.config(state=tk.DISABLED)

bt1 = tk.Button(window, text="1", padx=10, pady=10, command=lambda: button_click('1'))
bt2 = tk.Button(window, text="2", padx=10, pady=10, command=lambda: button_click('2'))
bt3 = tk.Button(window, text="3", padx=10, pady=10, command=lambda: button_click('3'))
bt4 = tk.Button(window, text="4", padx=10, pady=10, command=lambda: button_click('4'))
bt5 = tk.Button(window, text="5", padx=10, pady=10, command=lambda: button_click('5'))
bt6 = tk.Button(window, text="6", padx=10, pady=10, command=lambda: button_click('6'))
bt7 = tk.Button(window, text="7", padx=10, pady=10, command=lambda: button_click('7'))
bt8 = tk.Button(window, text="8", padx=10, pady=10, command=lambda: button_click('8'))
bt9 = tk.Button(window, text="9", padx=10, pady=10, command=lambda: button_click('9'))
btp = tk.Button(window, text=".", padx=10, pady=10, command=lambda: button_click('.'))
bt0 = tk.Button(window, text="0", padx=10, pady=10, command=lambda: button_click('0'))

btad = tk.Button(window, text="+", padx=10, pady=10, command=lambda: button_click('+'))
btsu = tk.Button(window, text="-", padx=10, pady=10, command=lambda: button_click('-'))
btdi = tk.Button(window, text="/", padx=10, pady=10, command=lambda: button_click('/'))
btmu = tk.Button(window, text="*", padx=10, pady=10, command=lambda: button_click('*'))

eql = tk.Button(window, text="=", padx=10, pady=10, command=calculate)
clear_btn = tk.Button(window, text="C", padx=10, pady=10, command=clear)

bt1.place(x=30, y=80, width=70, height=70)
bt2.place(x=130, y=80, width=70, height=70)
bt3.place(x=230, y=80, width=70, height=70)
bt4.place(x=30, y=180, width=70, height=70)
bt5.place(x=130, y=180, width=70, height=70)
bt6.place(x=230, y=180, width=70, height=70)
bt7.place(x=30, y=280, width=70, height=70)
bt8.place(x=130, y=280, width=70, height=70)
bt9.place(x=230, y=280, width=70, height=70)
btp.place(x=230, y=380, width=70, height=70)
bt0.place(x=30, y=380, width=170, height=70)

btad.place(x=330, y=80, width=70, height=70)
btsu.place(x=330, y=180, width=70, height=70)
btdi.place(x=330, y=280, width=70, height=70)
btmu.place(x=330, y=380, width=70, height=70)

eql.place(x=365, y=10, width=35, height=35)
clear_btn.place(x=325, y=10, width=35, height=35)

window.mainloop()
