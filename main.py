import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import numpy as np

class RealtimeGraphApp:
    def __init__(self, master):
        self.master = master
        master.title("Realtime Animated Graphs")

        # Create and pack the label
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
        self.line1, = self.ax1.plot(self.x_data, self.y_data1, label='Random Data 1')
        self.line2, = self.ax2.plot(self.x_data, self.y_data2, label='Random Data 2')

        # Set plot limits with some padding
        self.ax1.set_ylim(-1.1, 1.1)
        self.ax2.set_ylim(-1.1, 1.1)

        # Add legends to the plots
        self.ax1.legend()
        self.ax2.legend()

        # Animation function
        self.ani = FuncAnimation(self.fig, self.update_graph, interval=33, blit=False, cache_frame_data=False)

        # Protocol handler for closing the window
        master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def on_closing(self):
        self.master.quit()
        self.master.destroy()
        
    def update_graph(self, frame):
        # Generate new data points
        new_x = frame
        new_y1 = np.random.rand()
        new_y2 = np.random.rand()

        # Append new data points to the arrays
        self.x_data = np.append(self.x_data, new_x)
        self.y_data1 = np.append(self.y_data1, new_y1)
        self.y_data2 = np.append(self.y_data2, new_y2)

        # Update plot data
        self.line1.set_data(self.x_data, self.y_data1)
        self.line2.set_data(self.x_data, self.y_data2)

        # Adjust x-axis limits dynamically
        self.ax1.relim()
        self.ax1.autoscale_view(True, True, False)
        self.ax2.relim()
        self.ax2.autoscale_view(True, True, False)

        return self.line1, self.line2

if __name__ == "__main__":
    root = tk.Tk()
    app = RealtimeGraphApp(root)
    root.mainloop()