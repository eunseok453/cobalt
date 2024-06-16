import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


window=tk.Tk()
window.title("cobalt density")
window.geometry("600x400+100+100")
window.resizable(False,False)

def select(self):
    value = '농도(%) : ' + str(scale.get()) 
    label.config(text=value)
    
var=tk.IntVar()

scale=tk.Scale(window, variable=var, command=select, orient="horizontal", showvalue=False, tickinterval=100, to=100, length=300)
scale.pack()

label=tk.Label(window, text="값 : 0")
label.pack()

fig, ax = plt.subplots() 
ax.set_xlim(0,100) 
ax.set_ylim(0,100)
 
x = [0]
y = [0]



 
def animate(i, x, y):
    y_data = scale.get()

    x.append(x[-1] + 1)
    y.append(y_data)

    x = x[-100:]  
    y = y[-100:]

    ax.clear()
    ax.plot(x, y)
plt.yticks([0,10,20,30,40,50,60,70,80,90,100])
plt.axis([None,None,0,100])
animation = FuncAnimation(fig, animate, fargs=(x, y), interval=1)
figure=plt.show()

canvas = FigureCanvasTkAgg(figure, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

window.mainloop()
