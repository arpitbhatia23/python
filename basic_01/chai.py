import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output_label.config(text=f"Result: {result}")
    except:
        output_label.config(text="Error")

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("600x250")

entry = tk.Entry(window, width=40)
entry.pack(pady=20)

btn = tk.Button(window, text="Calculate", command=calculate)
btn.pack()

output_label = tk.Label(window, text="Result:")
output_label.pack()

window.mainloop()
