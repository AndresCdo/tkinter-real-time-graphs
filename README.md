# Tkinter Real-Time Graphs

This is a simple Python application that demonstrates how to create real-time animated graphs using Tkinter for the GUI and Matplotlib for plotting.

## Features

- Displays two real-time graphs side-by-side.
- Generates random data for demonstration purposes.
- Smoothly updates the graphs with new data points.
- Handles window closing gracefully to stop the animation.

## Requirements

- Python 3.7 or higher
- Matplotlib
- NumPy

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AndresCdo/tkinter-real-time-graphs.git
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application:

```bash
python main.py
```

A window will appear displaying two animated graphs with random data.

## Customization

You can adjust the graph update interval by changing the interval value in the `FuncAnimation` call in `main.py`.
Modify the data generation logic in the `update_graph` function to plot your own data.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
