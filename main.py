import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import numpy as np

class RealtimeGraphApp:
    def __init__(self, master):
        self.master = master
        master.title("Realtime Animated Graphs")

        self.label = tk.Label(master, text="Realtime Animated Graphs")
        self.label.pack()

        # Create Matplotlib figure and axes
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Initialize data arrays
        self.x_data = np.array([])
        self.y_data1 = np.array([])
        self.y_data2 = np.array([])

        # Create initial plots
        self.line1, = self.ax1.plot(self.x_data, self.y_data1)
        self.line2, = self.ax2.plot(self.x_data, self.y_data2)

        # Set plot limits with some padding
        self.ax1.set_ylim(-1.1, 1.1)  
        self.ax2.set_ylim(-1.1, 1.1)  

        # Animation function
        self.ani = FuncAnimation(self.fig, self.update_graph, interval=33, blit=False)

    def update_graph(self, i):
        # Generate new data points
        self.x_data = np.append(self.x_data, i)
        self.y_data1 = np.append(self.y_data1, np.random.rand())
        self.y_data2 = np.append(self.y_data2, np.random.rand())

        # Update plot data
        self.line1.set_data(self.x_data, self.y_data1)
        self.line2.set_data(self.x_data, self.y_data2)

        # Adjust x-axis limits dynamically
        self.ax1.relim()  
        self.ax1.autoscale_view(True, True, False)  
        self.ax2.relim()
        self.ax2.autoscale_view(True, True, False)

        return self.line1, self.line2

root = tk.Tk()
app = RealtimeGraphApp(root)
root.mainloop()
