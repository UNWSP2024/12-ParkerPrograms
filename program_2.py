# Nathan Parker
# 04/22/25
# Program #2: Joe's Automotive

import tkinter
import tkinter.messagebox

class JoesAutomotive:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive")

        # Create two frames
        # One for the Checkbuttons and another for the Button widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create seven IntVar objects to use with the Chechbuttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        # Set the IntVar objects to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        # Create the Checkbutton widgets in the top_frame
        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Oil Change - $30.00', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Lube Job - $20.00', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Radiator Flush - $40.00', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text='Transmission Fluid - $100.00', variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text='Inspection - $35.00', variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text='Muffler Replacement - $200.00', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text='Tire Rotation - $20.00', variable=self.cb_var7)

        # Pack the Checkbuttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        # Create a Select button and a Quit button
        self.select_button = tkinter.Button(self.bottom_frame, text='Select', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack the Buttons
        self.select_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack(padx=20, pady=20)
        self.bottom_frame.pack(padx=20, pady=20)

        # Start the mainloop
        tkinter.mainloop()

    # Define the show_choice method
    def show_choice(self):
        # Set the accumulator to 0
        self.accumulator = 0

        # Determine which Checkbuttons are selected
        # Add the correct amounts to the accumulator
        if self.cb_var1.get() == 1:
            self.accumulator += 30
        if self.cb_var2.get() == 1:
            self.accumulator += 20
        if self.cb_var3.get() == 1:
            self.accumulator += 40
        if self.cb_var4.get() == 1:
            self.accumulator += 100
        if self.cb_var5.get() == 1:
            self.accumulator += 35
        if self.cb_var6.get() == 1:
            self.accumulator += 200
        if self.cb_var7.get() == 1:
            self.accumulator += 20

        # Display the accumulator in the info dialog box
        tkinter.messagebox.showinfo('Selection', f'Total: ${self.accumulator:.2f}')

# Create an instance of the JoesAutomotive class
if __name__ == '__main__':
    JoesAutomotive = JoesAutomotive()
