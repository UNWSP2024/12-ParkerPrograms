# Nathan Parker
# 04/22/25
# Program #1: MPG Calculator

import tkinter

class MPG:
    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()
        self.main_window.title('MPG Calculator')

        # Create four frames
        self.gallons_frame = tkinter.Frame(self.main_window)
        self.miles_frame = tkinter.Frame(self.main_window)
        self.mpg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create a label widget and an entry widget
        self.gallons_label = tkinter.Label(self.gallons_frame, text='Enter the number of gallons of gas the car can hold:                 ')
        self.gallons_entry = tkinter.Entry(self.gallons_frame, width=10)

        # Pack the widgets
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        # Create a label widget and an entry widget
        self.miles_label = tkinter.Label(self.miles_frame, text='Enter the number of miles the car can go on a full tank of gas:')
        self.miles_entry = tkinter.Entry(self.miles_frame, width=10)

        # Pack the widgets
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # Create the widgets for the MPG
        self.result_label = tkinter.Label(self.mpg_frame, text='MPG = ', font=('', 32))
        self.mpg = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mpg_frame, textvariable=self.mpg, font=('',32))

        # Pack the widgets for the MPG
        self.result_label.pack(side='left')
        self.mpg_label.pack(side='left')

        # Create two buttons
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate MPG', command=self.calc_MPG, height=2, width=15, font=('',20))
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy, height=2, width=15, font=('',20))

        # Pack the buttons
        self.calc_button.pack(side='left', padx=10)
        self.quit_button.pack(side='left', padx=10)

        # Pack the frames
        self.gallons_frame.pack(padx=20, pady=10)
        self.miles_frame.pack(padx=20, pady=10)
        self.mpg_frame.pack(padx=20, pady=10)
        self.button_frame.pack(padx=20, pady=10)

        # Start the main loop
        tkinter.mainloop()

    # Define the calc_MPG method
    def calc_MPG(self):
        # Get the gallons and miles
        self.gallons = float(self.gallons_entry.get())
        self.miles = float(self.miles_entry.get())

        # Calculate the MPG
        self.MPG = str(self.miles / self.gallons)

        # Update the mpg_label widget by storing the value of self.MPG in the StringVar
        self.mpg.set(self.MPG)

# Create an instance of the MPG class
if __name__ == '__main__':
    MPG = MPG()
