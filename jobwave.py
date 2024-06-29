# instructions: install your virtual environments
# import the needed libraries
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# download your needed pictures from the internet
# Please note that all pictures I have used so far were created by myself on the website: Canva

# whenopening the GUI you will be greeted by a front page and a enter button
# afterwards a login page will be opened. You need the login information to get to the website.
# Username: user  .  Password: 12345


# Initialize global variables
appointments = {}
current_file = None

# Function to load appointments from a file
def load_appointments():
    if current_file:
        appointments.clear()
        with open(current_file, 'r') as file:
            for line in file:
                parts = line.strip().split(': ')
                if len(parts) == 2:
                    date, appointment = parts
                    appointments[date] = appointment
        update_calendar()

# Function to add or edit an appointment
def add_edit_appointment():
    date = date_var.get()
    appointment = appointment_entry.get()
    if date and appointment:
        appointments[date] = appointment
        update_calendar()
        clear_entry_fields()

# Function to clear date and appointment entry fields
def clear_entry_fields():
    date_var.set('')
    appointment_entry.delete(0, tk.END)

# Function to update the calendar display
def update_calendar():
    calendar_display.config(state=tk.NORMAL)
    calendar_display.delete(1.0, tk.END)
    for date, appointment in sorted(appointments.items()):
        calendar_display.insert(tk.END, f"{date}: {appointment}\n")
    calendar_display.config(state=tk.DISABLED)

# Function to add an image to the frame
def add_image(root, file_path):
    global pic, f1
    f1 = tk.Frame(root)
    img = Image.open(file_path)
    img = img.resize((650, 450), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

# Function for the third page with calendar functionality
# Here you can add or edit your appointments. Fill in the name of your appointment and the date and it will be listed in the calender.
def page_three():
    global next_label, september_label, date_var, appointment_entry, calendar_display, add_edit_button, calendar_info_label

    f1.destroy()
    enter_button.destroy()
    add_image(root, file_path="pictures/p11.png")
    next_label = tk.Label(text="Calendar",
                          relief=tk.RAISED,
                          bg='#291b62',
                          fg='#ffffff',
                          borderwidth=3,
                          font=("Georgia", 34),
                          padx=20,
                          pady=10,
                          )
    next_label.place(x=10, y=10)

    # Create a Frame for adding/editing appointments
    add_edit_frame = ttk.LabelFrame(root, text="Add/Edit Appointment")
    add_edit_frame.place(x=10, y=80, width=630)

    # Date entry
    date_label = ttk.Label(add_edit_frame, text="Date:")
    date_label.grid(row=0, column=0, padx=5, pady=5)
    date_var = tk.StringVar()
    date_entry = ttk.Entry(add_edit_frame, textvariable=date_var)
    date_entry.grid(row=0, column=1, padx=5, pady=5)

    # Appointment entry
    appointment_label = ttk.Label(add_edit_frame, text="Appointment:")
    appointment_label.grid(row=1, column=0, padx=5, pady=5)
    appointment_entry = ttk.Entry(add_edit_frame)
    appointment_entry.grid(row=1, column=1, padx=5, pady=5)

    # Add/Edit button
    add_edit_button = ttk.Button(add_edit_frame, text="Add/Edit", command=add_edit_appointment)
    add_edit_button.grid(row=2, columnspan=2, padx=5, pady=10)

    # Create a Frame for displaying appointments
    calendar_frame = ttk.LabelFrame(root, text="Calendar")
    calendar_frame.place(x=10, y=220, width=630, height=180)

    # Calendar display
    calendar_display = tk.Text(calendar_frame, wrap=tk.WORD, state=tk.DISABLED)
    calendar_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    calendar_info_label = tk.Label(text="Add or Edit a job in your calendar to keep track",
                          relief=tk.RAISED,
                          bg='#291b62',
                          fg='#ffffff',
                          borderwidth=1,
                          font=("Georgia", 14),
                          padx=20,
                          pady=10,
                          )
    calendar_info_label.place(x=225, y=30)

# with this button you will be redirected to the main page
    back_button_2 = tk.Button(text="Back",
                             font='georgia 17 bold',
                             command=back_3,
                             fg="black"
                            )
    back_button_2.place(x=515, y=405)

# Function definitions for other pages and the main window setup

def back():
    f1.destroy()
    back_button.destroy()
    page_one()

def back_2():
    f1.destroy()
    start_label.destroy()
    page_two()

def back_3():
    f1.destroy()
    start_label.destroy()
    appointment_entry.destroy()
    calendar_display.destroy()
    page_two()

def back_5():
    f1.destroy()
    back_button.destroy()

    page_five()

def back_6():
    f1.destroy()
    back_button.destroy()

    page_six()

def page_one():
    global enter_button, welcome, start_label, second_label
    add_image(root, file_path="pictures/p1.png")

    enter_button = tk.Button(text="Click here to enter the site",
                             font='georgia 18',
                             command=page_login,
                             fg="RoyalBlue1",
                             bg="RoyalBlue1",
                             )
    enter_button.place(x=370, y=260)

    welcome = tk.Label(text="JOBWAVE",
                      font="georgia 68",
                      fg="White",
                      bg="RoyalBlue3"
                       )
    welcome.place(x=150, y=40)

    start_label = tk.Label(text="WHERE YOU CAN FIND PART TIME JOBS",
                       font="georgia 22 bold",
                       bg="RoyalBlue3",
                       fg="White"
                       )
    start_label.place(x=75, y=140)

    second_label = tk.Label(text="PERFECTLY FITTING TO YOUR SCHEDULE",
                           font="georgia 17 bold",
                           bg="RoyalBlue3",
                           fg="White"
                           )
    second_label.place(x=115, y=180)

# On the login page, you have the possibility to access the website by using a username and a password. 
# Please note that you have to click next to them, so that the box will appear. 

def page_login():
    global frame, username_entry, password_entry, login_button, new_label
    f1.destroy()
    enter_button.destroy()
    start_label.destroy()
    welcome.destroy()
    second_label.destroy()

    frame = tk.Frame(root, bg='#4876ff')

    new_label = tk.Label(text="Click next to the Username/Password and fill in the box",
                           font="georgia 14 bold",
                           bg="RoyalBlue3",
                           fg="White"
                           )
    new_label.place(x=110, y=410)
    
    login_label = tk.Label(frame, text="Login", bg='#4876ff', fg="#FFFFFF", font=("Georgia", 45))
    username_label = tk.Label(frame, text="Username", bg='#4876ff', fg="#FFFFFF", font=("Georgia", 16))
    username_entry = tk.Entry(frame, font=("Arial", 16))
    password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
    password_label = tk.Label(frame, text="Password", bg='#4876ff', fg="#FFFFFF", font=("Georgia", 16))
    login_button = tk.Button(frame, text="Login", bg="#333333", fg="#333333", font=("Georgia", 16), command=login)

    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    frame.pack(pady=50)

# A message will appear, whether you used the correct login information. 
def login():
    username = "user"
    password = "12345"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        frame.destroy()
        page_two()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def page_two():
    global  test_label
    f1.destroy()
    new_label.destroy()
    add_image(root, file_path="pictures/p2.png")
    test_label = tk.Label(text="OUR SERVICES",
                          relief=tk.RAISED,
                          bg='#291b62',
                          fg='#ffffff',
                          borderwidth=3,
                          font=("Georgia", 34),
                          padx=20,
                          pady=10,
                          )
    test_label.place(x=20, y=10)
    enter_news = tk.Button(text="NEWS",
                           font="georgia 24",
                           height=1,
                           width=11,
                           command=news
                           )
    enter_news.place(x=390, y=320)
    enter_the_calender = tk.Button(text="CALENDAR",
                                   font="georgia 24",
                                   height=1,
                                   width=11,
                                   command=calender
                                   )
    enter_the_calender.place(x=390, y=250)
    enter_previous_jobs = tk.Button(text="PREVIOUS JOBS",
                                    font="georgia 23 ",
                                    height=1,
                                    width=11,
                                    command=new_jobs,
                                    )
    enter_previous_jobs.place(x=390, y=180)
    enter_new_jobs = tk.Button(text="NEW JOBS",
                               font="georgia 24 ",
                               height=2,
                               width=11,
                               command=previous_jobs,
                               )
    enter_new_jobs.place(x=390, y=80)


def calender():
    f1.destroy()
    page_three()

def news():
    f1.destroy()
    page_four()

def previous_jobs():
    f1.destroy()
    page_five()

def new_jobs():
    f1.destroy()
    page_six()

def page_four():
    global next_label, message_news
    f1.destroy()
    enter_button.destroy()
    add_image(root, file_path="pictures/p7.png")
    next_label = tk.Label(text=f"NEWS",
                          relief=tk.RAISED,
                          bg='#291b62',
                          fg='#ffffff',
                          borderwidth=3,
                          font=("Georgia", 34),  # Adjust the font size here
                          padx=20,  # Horizontal padding
                          pady=10,  # Vertical padding
                          )
    next_label.place(x=10, y=10)
    message_news = tk.Label(text="Here you will be able to see all upcoming news ordered by date.",
                              font="lucida 18 bold",
                              bg="antique white",
                              fg="midnight blue",
                              )
    message_news.place(x=50, y=90)

    news_1 = tk.Label(text="Currently no news",
                            font="lucida 15",
                            bg="antique white",
                            fg="midnight blue",
                            )
    news_1.place(x=50, y=150)
    back_button = tk.Button(text="Back",
                              font='georgia 17 bold',
                              command=back_2,
                              fg="black"
                              )
    back_button.place(x=515, y=400)

def page_five():
    global next_label, label_new_jobs, label_this_week, label_next_week, label_next_month
    f1.destroy()
    enter_button.destroy()
    add_image(root, file_path="pictures/p3.png")
    label_new_jobs= tk.Label(text=f"NEW JOBS",
                             relief=tk.RAISED,
                             bg='#291b62',
                             fg='#ffffff',
                             borderwidth=3,
                             font=("Georgia", 34),  # Adjust the font size here
                             padx=20,  # Horizontal padding
                             pady=10,  # Vertical padding
                          )
    label_new_jobs.place(x=10, y=10)
    label_this_week = tk.Label(text=f"WITHIN THIS WEEK",
                          relief=tk.RAISED,
                          bg='#291b62',
                          fg='#ffffff',
                          borderwidth=5
                          )
    label_this_week.place(x=22, y=100)
    label_next_week = tk.Label(text=f"WITHIN NEXT WEEK",
                          relief=tk.RAISED,
                          bg='#291b62',
                          fg='#ffffff',
                          borderwidth=5
                          )
    label_next_week.place(x=240, y=100)
    label_next_month = tk.Label(text=f"WITHIN NEXT MONTH",
                          relief=tk.RAISED,
                          bg='#291b62',
                          fg='#ffffff',
                          borderwidth=5
                          )
    label_next_month.place(x=450, y=100)
    example_button = tk.Button(text="Waiter/Waitress",
                                 font="lucida 16 bold",
                                 height=2,
                                 width=12,
                                 command=example_1
                                 )
    example_button.place(x=20, y=160)

    example_button_2 = tk.Button(text="Cook",
                               font="lucida 16 bold",
                               height=2,
                               width=12,
                               command=example_2
                               )
    example_button_2.place(x=20, y=220)

    example_button_3 = tk.Button(text="Eventhelper",
                                 font="lucida 16 bold",
                                 height=2,
                                 width=12,
                                 command=example_3
                                 )
    example_button_3.place(x=235, y=160)
    back_button_2 = tk.Button(text="Back",
                              font='georgia 17 bold',
                              command=back_2,
                              fg="black"
                              )
    back_button_2.place(x=515, y=400)

def page_six():
    global next_label, documents_label, message_1, getlocalFile
    f1.destroy()
    enter_button.destroy()
    add_image(root, file_path="pictures/4.png")
    next_label = tk.Label(text=f"PREVIOUS JOBS",
                          relief=tk.RAISED,
                          bg='#291b62',
                          fg='#ffffff',
                          borderwidth=3,
                          font=("Georgia", 34),  # Adjust the font size here
                          padx=20,  # Horizontal padding
                          pady=10,  # Vertical padding
                          )
    next_label.place(x=10, y=10)

    example_button = tk.Button(text="Barkeeper",
                               font="lucida 16 bold",
                               height=2,
                               width=12,
                               command=previous_job_1
                               )
    example_button.place(x=30, y=150)


    message_1 = tk.Label(text="Here you can find all needed documents of yours. As well as all the previous jobs you did.",
                              font="georgia 14",
                              bg="Lemon Chiffon",
                              fg="midnight blue"
                              )
    message_1.place(x=30, y=110)
    back_button = tk.Button(text="Back",
                              font='georgia 17 bold',
                              command=back_2,
                              fg="black"
                              )
    back_button.place(x=515, y=400)


def example_1():
    global label_example_1, time_example_1, place_example_1, pay_example_1, back_button, add_button_1
    f1.destroy()
    enter_button.destroy()
    add_image(root, file_path="pictures/p5.png")
    label_example_1 = tk.Label(text=f"Waiter/Waitress",
                               relief=tk.RAISED,
                               bg='#291b62',
                               fg='#ffffff',
                               borderwidth=3,
                               font=("Georgia", 34),  # Adjust the font size here
                               padx=20,  # Horizontal padding
                               pady=10,
                          )
    label_example_1.place(x=70, y=40)

    time_example_1 = tk.Label(text="01/06/2024 11AM - 5PM",
                            font="georgia 18 ",
                            bg="antique white",
                            fg="midnight blue",
                            )
    time_example_1.place(x= 100, y=160)
    place_example_1 = tk.Label(text="Place = Am Sande, Lüneburg, 21335, Germany ",
                               font="georgia 18 ",
                               bg="antique white",
                               fg="midnight blue",
                               )
    place_example_1.place(x=100, y=220)

    pay_example_1 = tk.Label(text="Pay = 12 €/h ",
                             font="georgia 18 ",
                             bg="antique white",
                             fg="midnight blue",
                               )
    pay_example_1.place(x=100, y=280)
    back_button = tk.Button(text="Back",
                              font='georgia 17 bold',
                              command=back_5,
                              fg="black"
                              )
    back_button.place(x=515, y=400)

    # Here you have the option to add this date to your calendar. Click on the button to be redirected to the calendar. 
    add_button_1 = tk.Button(text="Add to my Calendar",
                              font='georgia 17 bold',
                              command=calender,
                              fg="black"
                              )
    add_button_1.place(x=215, y=350)

def example_2():
    global label_example_2, time_example_2, place_example_2, pay_example_2, back_button, add_button_2
    f1.destroy()
    enter_button.destroy()
    add_image(root, file_path="pictures/p5.png")
    label_example_2 = tk.Label(text=f"Cook",
                               relief=tk.RAISED,
                               bg='#291b62',
                               fg='#ffffff',
                               borderwidth=3,
                               font=("Georgia", 34),  # Adjust the font size here
                               padx=20,  # Horizontal padding
                               pady=10,
                               )
    label_example_2.place(x=70, y=40)

    time_example_2 = tk.Label(text="04/07/2024 9AM - 5PM",
                              font="georgia 18 ",
                              bg="antique white",
                              fg="midnight blue",
                              )
    time_example_2.place(x=100, y=160)
    place_example_2 = tk.Label(text="Place = Häcklingen, Lüneburg, 21335, Germany ",
                               font="georgia 18 ",
                               bg="antique white",
                               fg="midnight blue",
                               )
    place_example_2.place(x=100, y=220)

    pay_example_2 = tk.Label(text="Pay = 14,50 €/h ",
                             font="georgia 18 ",
                             bg="antique white",
                             fg="midnight blue",
                             )
    pay_example_2.place(x=100, y=280)
    back_button = tk.Button(text="Back",
                              font='georgia 17 bold',
                              command=back_5,
                              fg="black"
                              )
    back_button.place(x=515, y=400)

    add_button_2 = tk.Button(text="Add to my Calendar",
                              font='georgia 17 bold',
                              command=calender,
                              fg="black"
                              )
    add_button_2.place(x=215, y=350)

def example_3():
    global label_example_3, time_example_3, place_example_3, pay_example_3, back_button, add_button_3
    f1.destroy()
    enter_button.destroy()
    add_image(root, file_path="pictures/p5.png")
    label_example_2 = tk.Label(text=f"Eventhelper",
                               relief=tk.RAISED,
                               bg='#291b62',
                               fg='#ffffff',
                               borderwidth=3,
                               font=("Georgia", 34),  # Adjust the font size here
                               padx=20,  # Horizontal padding
                               pady=10,
                               )
    label_example_2.place(x=70, y=40)

    time_example_2 = tk.Label(text="08/07/2024 9AM - 3PM",
                              font="georgia 18 ",
                              bg="antique white",
                              fg="midnight blue",
                              )
    time_example_2.place(x=100, y=160)
    place_example_2 = tk.Label(text="Place = Rotes Feld, Lüneburg, 21335, Germany ",
                               font="georgia 18 ",
                               bg="antique white",
                               fg="midnight blue",
                               )
    place_example_2.place(x=100, y=220)

    pay_example_2 = tk.Label(text="Pay = 15 €/h ",
                             font="georgia 18 ",
                             bg="antique white",
                             fg="midnight blue",
                             )
    pay_example_2.place(x=100, y=280)
    back_button = tk.Button(text="Back",
                              font='georgia 17 bold',
                              command=back_5,
                              fg="black"
                              )
    back_button.place(x=515, y=400)

    add_button_3 = tk.Button(text="Add to my Calendar",
                              font='georgia 17 bold',
                              command=calender,
                              fg="black"
                              )
    add_button_3.place(x=215, y=350)

def previous_job_1():
    global label_example_3, time_example_3, place_example_3, pay_example_3, back_button, add_button_3
    f1.destroy()
    enter_button.destroy()
    add_image(root, file_path="pictures/p4.png")
    label_example_2 = tk.Label(text=f"Barkeeper",
                               relief=tk.RAISED,
                               bg='#291b62',
                               fg='#ffffff',
                               borderwidth=3,
                               font=("Georgia", 34),  # Adjust the font size here
                               padx=20,  # Horizontal padding
                               pady=10,
                               )
    label_example_2.place(x=70, y=40)

    time_example_2 = tk.Label(text="18/06/2024 9PM - 5AM",
                              font="georgia 18 ",
                              bg="antique white",
                              fg="midnight blue",
                              )
    time_example_2.place(x=100, y=160)
    place_example_2 = tk.Label(text="Place = Rotes Feld, Lüneburg, 21335, Germany ",
                               font="georgia 18 ",
                               bg="antique white",
                               fg="midnight blue",
                               )
    place_example_2.place(x=100, y=220)

    pay_example_2 = tk.Label(text="Pay = 15 €/h ",
                             font="georgia 18 ",
                             bg="antique white",
                             fg="midnight blue",
                             )
    pay_example_2.place(x=100, y=280)

    message_one = tk.Label(text="You completed this job. ",
                             font="georgia 11 ",
                             bg="antique white",
                             fg="midnight blue",
                             )
    message_one.place(x=100, y=330)
    message_two = tk.Label(text="After a review from the management team you will be paid at the end of the month.",
                           font="georgia 11 ",
                           bg="antique white",
                           fg="midnight blue",
                           )
    message_two.place(x=100, y=350)

    label_completed = tk.Label(text=f"Completed",
                               relief=tk.RAISED,
                               bg='#291b62',
                               fg='#ffffff',
                               borderwidth=3,
                               font=("Georgia", 14),  # Adjust the font size here
                               padx=20,  # Horizontal padding
                               pady=10,
                               )
    label_completed.place(x=230, y=380)
    back_button = tk.Button(text="Back",
                              font='georgia 17 bold',
                              command=back_6,
                              fg="black"
                              )
    back_button.place(x=515, y=400)


# Main Tkinter window setup
root = tk.Tk()
root.geometry("650x450")
root.title("JobWave")
root.configure(bg='RoyalBlue3')
page_one()
root.mainloop()
