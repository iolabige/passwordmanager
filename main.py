import tkinter as tk
import gui

# Main execution starts here
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    gui.setup_ui(root)  # Setup the UI elements in the main window
    root.mainloop()  # Start the GUI event loop
