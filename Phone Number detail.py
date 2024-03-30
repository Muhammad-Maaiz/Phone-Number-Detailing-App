# PHONE NUMBER DETAILING APP:

# Import necessary libraries
from tkinter import *
from tkinter import messagebox
import phonenumbers
from phonenumbers import timezone, geocoder, carrier


def phone_number():
    """
    Function to fetch and display details of the provided phone number.
    """
    number = num_entry.get()
    if not number:
        messagebox.showerror("Error", "Enter a Number")
        return  # Exit the function if number is not provided
    
    try:
        # Parse the phone number and retrieve details
        phone = phonenumbers.parse(number)
        if not phonenumbers.is_valid_number(phone):
            messagebox.showerror("Error", "Invalid Phone Number")
            return  # Exit the function if the phone number is invalid
        
        time = timezone.time_zones_for_number(phone)
        car =  carrier.name_for_number(phone, "en")
        reg = geocoder.description_for_number(phone, "en")
        
        # Update the detail box with fetched details
        detail_box.config(state="normal")  # Enable editing temporarily
        detail_box.delete("1.0", END)
        detail_box.insert(END,"Information:\n")
        detail_box.insert(END, f"Phone Number: {phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}\n")
        detail_box.insert(END, f"Timezone: {', '.join(time)}\n")
        detail_box.insert(END, f"Carrier: {car}\n")
        detail_box.insert(END, f"Region: {reg}")
        detail_box.config(state="disabled")  # Disable editing again
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def clear():
    """
    Function to clear the input field and detail box.
    """
    num_entry.delete(0, END)
    detail_box.config(state="normal")  # Enable editing temporarily
    detail_box.delete("1.0", END)
    detail_box.config(state="disabled")  # Disable editing again

# Create a GUI 
root = Tk()
root.title("Phone Number Detail")
root.geometry("305x430")
root.iconbitmap("phonelogo.ico")
root.resizable(width=False, height=False)

# Create a main frame inside the root window
main_frame = Frame(root, bg="yellow")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Create an app label inside the main frame
lbl = Label(main_frame, text="𝓟𝓱𝓸𝓷𝓮 𝓝𝓾𝓶𝓫𝓮𝓻\n𝓓𝓮𝓽𝓪𝓲𝓵𝓲𝓷𝓰 𝓐𝓹𝓹", font=("Bold", 20), bg="yellow")
lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create a phone number label inside the main frame
num_lbl = Label(main_frame, text="Phone Number:", font="Bold", bg="yellow")
num_lbl.grid(row=1, column=0, padx=10, pady=10)

# Create an entry field to get phone number inside the main frame
num_entry = Entry(main_frame, bd=2)
num_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a button to search details inside the main frame
btn = Button(main_frame, text="Search Detail", font="bold", fg="White", bg="green", width=12, command=phone_number)
btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a text box to display details inside the main frame
detail_box = Text(main_frame, width=35, height=5,state="disabled")
detail_box.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create an exit button inside the main frame
exit_btn = Button(main_frame, text="Exit", font="bold", fg="White", bg="red", width=5, command=root.destroy)
exit_btn.grid(row=4, column=0, padx=10, pady=10)

# Create a button to clear input and details inside the main frame
clear_btn = Button(main_frame, text="Clear", font="bold", fg="White", bg="blue", width=5, command=clear)
clear_btn.grid(row=4, column=1, padx=10, pady=10)

# Create a label with app creator's name inside the main frame
name_lbl = Label(main_frame, text="𝓜𝓪𝓭𝓮 𝓑𝔂:\n𝓜𝓾𝓱𝓪𝓶𝓶𝓪𝓭 𝓜𝓪𝓪𝓲𝔃", font=("Bold", 20), bg="yellow")
name_lbl.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()