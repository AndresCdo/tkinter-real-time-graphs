
import tkinter as Tk
import matplotlib.pyplot as plt
from numpy import random
from itertools import count
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Set the style for the graphs
plt.style.use('fivethirtyeight')

# Initialize the data lists for the two graphs
x_vals = []
y_vals = []
y_vals2 = []

# Initialize the iterators for the two graphs
index = count()
index2 = count()

def _quit():
    root.quit()    # stops mainloop

def animate(i):
    """The function that will be called by the FuncAnimation object to update the graphs.
    
    Args:
    i (int): The frame number (not used in this function).
    """
    
    # Generate new random data for the two graphs
    x_vals.append(next(index))
    y_vals.append(random.rand())
    y_vals2.append(random.rand())
    
    # Get the two axes of the figure
    ax1, ax2 = plt.gcf().get_axes()
    
    # Clear the previous data on the axes
    ax1.cla()
    ax2.cla()
    
    # Plot the new data on the axes
    ax1.plot(x_vals, y_vals)
    ax2.plot(x_vals, y_vals2)

# Initialize the GUI window
root = Tk.Tk()
root.protocol("WM_DELETE_WINDOW", _quit)
root.title("Realtime Animated Graphs")

# Set the label for the GUI window
label = Tk.Label(root, text="Realtime Animated Graphs").grid(column=0, row=0)

# Initialize the canvas for the two graphs
canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
canvas.get_tk_widget().grid(column=0, row=1)

# Create two subplots on the figure for the two graphs
plt.gcf().subplots(1, 2)

# Initialize the FuncAnimation object to update the graphs
ani = FuncAnimation(plt.gcf(), animate, interval=330, blit=False, save_count=50)

# Start the GUI event loop
Tk.mainloop()
print('Exited')