# Nathan Parker
# 04/22/25
# Program #3: Long-Distance Calls

import tkinter
import tkinter.messagebox

class LongDistanceCalls:

    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title('Long-Distance Calls')

        # Create three frames
        # one for the Radiobuttions,
        # one for a label widget and an entry widget,
        # and one for the Button widgets
        self.rb_frame = tkinter.Frame(self.main_window)
        self.min_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create an IntVar object to use with the Radiobuttons
        self.radio_var = tkinter.IntVar()

        # Set the IntVar object to 2
        self.radio_var.set(2)

        # Create the Radiobutton widgets in the rb_frame
        self.rb1 = tkinter.Radiobutton(self.rb_frame, text='Daytime (6:00 A.M. – 5:59 P.M.)', variable=self.radio_var, value=2)
        self.rb2 = tkinter.Radiobutton(self.rb_frame, text='Evening (6:00 P.M. – 11:59 P.M.)', variable=self.radio_var, value=12)
        self.rb3 = tkinter.Radiobutton(self.rb_frame, text='Off-Peak (midnight – 5:59 P.M.)', variable=self.radio_var, value=5)

        # Pack the Radiobuttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Create a label widget and an entry widget for the min_frame
        self.min_label = tkinter.Label(self.min_frame, text='Length of call in minutes:')
        self.min_entry = tkinter.Entry(self.min_frame, width=10)

        # Pack the widgets
        self.min_label.pack(side='left')
        self.min_entry.pack(side='left')

        # Create a calc_button and a quit_button for the button_frame
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate', command=self.calc)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        # Pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.rb_frame.pack(padx=20, pady=20)
        self.min_frame.pack(padx=20)
        self.button_frame.pack(padx=20, pady=20)

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the calc method
    def calc(self):
        # Set price to the rate times the entry of minutes
        price = (float(self.radio_var.get()) / 100) * float(self.min_entry.get())
        # Display the price in an info dialog box
        tkinter.messagebox.showinfo('Price', 'Price: $' + str(f'{price:.2f}'))

# Create an instance of the LongDistanceCalls class
if __name__ =='__main__':
    LongDistanceCall = LongDistanceCalls()
