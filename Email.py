import os
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


sender_email = ""
password = ""

def signup():
    global sender_email, password
    sender_email = sender_email_entry.get()
    password = password_entry.get()
    messagebox.showinfo("Signup", "Credentials saved successfully.")
    
def toggle_password_visibility():
    current_show_state = password_entry.cget('show')
    new_show_state = '' if current_show_state else '*'
    password_entry.config(show=new_show_state)

def save_draft():
    # Add functionality to save draft
    messagebox.showinfo("Save Draft", "Draft saved successfully.")

def load_draft():
    # Add functionality to load draft
    messagebox.showinfo("Load Draft", "Draft loaded successfully.")

def open_single_mail_window():
    single_mail_window = tk.Toplevel(root)
    single_mail_window.title("Single Mail")
    
        # Add image at the top
    single_mail_image = Image.open("SpeedySend.png").resize((500, 100))
    single_mail_image = ImageTk.PhotoImage(single_mail_image)
    image_label = tk.Label(single_mail_window, image=single_mail_image)
    image_label.image = single_mail_image  # Retain reference to image
    image_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)  # Adjusted columnspan

    # Create menu button with submenus
    menu_button_icon = Image.open("menu_icon.png").resize((20, 20))
    menu_button_icon = ImageTk.PhotoImage(menu_button_icon)

    menu_button = tk.Menubutton(single_mail_window, image=menu_button_icon, relief=tk.RAISED)
    menu_button.grid(row=1, column=0, padx=10, pady=5, sticky="e")  # Adjusted column position
    menu_button.image = menu_button_icon  # Retain reference to the image
    menu_button.menu = tk.Menu(menu_button, tearoff=0)
    menu_button["menu"] = menu_button.menu

    # Add submenus
    menu_button.menu.add_command(label="Save Draft", command=save_draft)
    menu_button.menu.add_command(label="Load Draft", command=load_draft)

    receiver_email_label = tk.Label(single_mail_window, text="Receiver Email:")
    receiver_email_label.grid(row=1, column=1, padx=10, pady=5, sticky="e")  # Adjusted column position

    receiver_email_entry = tk.Entry(single_mail_window, width=40)
    receiver_email_entry.grid(row=1, column=2, padx=10, pady=5, columnspan=2)  # Adjusted columnspan and position

    subject_label = tk.Label(single_mail_window, text="Subject:")
    subject_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")  # Adjusted column position

    subject_entry = tk.Entry(single_mail_window, width=40)
    subject_entry.grid(row=2, column=2, padx=10, pady=5, columnspan=2)  # Adjusted columnspan and position

    message_label = tk.Label(single_mail_window, text="Message:")
    message_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")  # Adjusted column position

    message_entry = tk.Text(single_mail_window, width=40, height=10)
    message_entry.grid(row=3, column=2, padx=10, pady=5, columnspan=2)  # Adjusted columnspan and position

    # Attachment
    attachment_label = tk.Label(single_mail_window, text="Attachment:")
    attachment_label.grid(row=4, column=1, padx=10, pady=5, sticky="e")  # Adjusted row and column position

    attachment_entry = tk.Entry(single_mail_window, width=40)
    attachment_entry.grid(row=4, column=2, padx=10, pady=5)  # Adjusted row and column position

    def attach_file():
        file_path = filedialog.askopenfilename()
        attachment_entry.delete(0, tk.END)
        attachment_entry.insert(0, file_path)

    attach_button_icon = Image.open("attachment.png").resize((20, 20))
    attach_button_icon = ImageTk.PhotoImage(attach_button_icon)

    attach_button = tk.Button(single_mail_window, image=attach_button_icon, command=attach_file)
    attach_button.image = attach_button_icon
    attach_button.grid(row=4, column=3, padx=5)  # Adjusted row and column position

    def send_email():
        receiver_email = receiver_email_entry.get()
        subject = subject_entry.get()
        message = message_entry.get("1.0", tk.END)
        attachment_path = attachment_entry.get()  # Retrieve the attachment path
        # Add code to send email with attachment
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            
            # Create a MIME base
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            
            # Attach the message
            msg.attach(MIMEText(message, 'plain'))
            
            # Attach the file
            if attachment_path:
                with open(attachment_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
                msg.attach(part)
                
            # Send the email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            messagebox.showinfo("Email Sent", "Email has been sent successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    send_email_button = tk.Button(single_mail_window, text="Send Email", bg="#008000", command=send_email)
    send_email_button.grid(row=5, column=1, columnspan=3, pady=10)  # Adjusted columnspan
    
def open_multiple_mail_window():
    multiple_mail_window = tk.Toplevel(root)
    multiple_mail_window.title("Multiple Mail")

    # Add image at the top
    multiple_mail_image = Image.open("SpeedySend.png")
    multiple_mail_image = ImageTk.PhotoImage(multiple_mail_image)
    image_label = tk.Label(multiple_mail_window, image=multiple_mail_image)
    image_label.image = multiple_mail_image  # Retain reference to image
    image_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Create menu button with submenus
    menu_button_icon = Image.open("menu_icon.png").resize((20, 20))
    menu_button_icon = ImageTk.PhotoImage(menu_button_icon)

    menu_button = tk.Menubutton(multiple_mail_window, image=menu_button_icon, relief=tk.RAISED)
    menu_button.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    menu_button.image = menu_button_icon  # Retain reference to the image
    menu_button.menu = tk.Menu(menu_button, tearoff=0)
    menu_button["menu"] = menu_button.menu

    # Add submenus
    menu_button.menu.add_command(label="Save Draft", command=save_draft)
    menu_button.menu.add_command(label="Load Draft", command=load_draft)

    receiver_email_label = tk.Label(multiple_mail_window, text="Receiver Email:")
    receiver_email_label.grid(row=1, column=1, padx=10, pady=5, sticky="e")
    receiver_email_entry = tk.Entry(multiple_mail_window, width=40)
    receiver_email_entry.grid(row=1, column=2, padx=10, pady=5)

    subject_label = tk.Label(multiple_mail_window, text="Subject:")
    subject_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")
    subject_entry = tk.Entry(multiple_mail_window, width=40)
    subject_entry.grid(row=2, column=2, padx=10, pady=5)

    message_label = tk.Label(multiple_mail_window, text="Message:")
    message_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")
    message_entry = tk.Text(multiple_mail_window, width=40, height=10)
    message_entry.grid(row=3, column=2, padx=10, pady=5)

    # Attachment
    attachment_label = tk.Label(multiple_mail_window, text="Attachment:")
    attachment_label.grid(row=4, column=1, padx=10, pady=5, sticky="e")  # Adjusted row and column position

    attachment_entry = tk.Entry(multiple_mail_window, width=40)
    attachment_entry.grid(row=4, column=2, padx=10, pady=5)  # Adjusted row and column position

    def attach_file():
        file_path = filedialog.askopenfilename()
        attachment_entry.delete(0, tk.END)
        attachment_entry.insert(0, file_path)

    attach_button_icon = Image.open("attachment.png").resize((20, 20))
    attach_button_icon = ImageTk.PhotoImage(attach_button_icon)

    attach_button = tk.Button(multiple_mail_window, image=attach_button_icon, command=attach_file)
    attach_button.image = attach_button_icon
    attach_button.grid(row=4, column=3, padx=5)  # Adjusted row and column position

    def send_email():
        receiver_email = receiver_email_entry.get()
        subject = subject_entry.get()
        message = message_entry.get("1.0", tk.END)
        attachment_path = attachment_entry.get()  # Get the attachment path

        # Add code to send email with attachment
        try:
            # Create a multipart message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject

            # Add message body
            msg.attach(MIMEText(message, 'plain'))

            # Open the file to be sent
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(attachment_path)}",
            )

            # Add attachment to message and convert message to string
            msg.attach(part)
            text = msg.as_string()

            # Send the email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            server.quit()

            messagebox.showinfo("Email Sent", "Email has been sent successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    send_email_button = tk.Button(multiple_mail_window, text="Send Email", bg="#008000", command=send_email)
    send_email_button.grid(row=5, column=1, columnspan=3, pady=10)  # Adjusted columnspan
    
def open_csv_mail_window():
    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            csv_file_entry.delete(0, tk.END)  # Clear any previous text
            csv_file_entry.insert(0, file_path)  # Insert the selected file path

    def send_email_from_csv():
        csv_file_path = csv_file_entry.get()
        subject = subject_entry.get()
        message = message_entry.get("1.0", tk.END)
        attachment_path = attachment_entry.get()  # Get the attachment path

        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.reader(file)
                id_row = next(reader)  # Get the ID row
                id_index = id_row.index("ID")  # Find the index of the "ID" column
                for row in reader:
                    receiver_email = row[id_index]  # Get email from the ID row
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(sender_email, password)

                    # Create a multipart message
                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = receiver_email
                    msg['Subject'] = subject

                    # Add message body
                    msg.attach(MIMEText(message, 'plain'))

                    # Add attachment if provided
                    if attachment_path:
                        with open(attachment_path, "rb") as attachment:
                            part = MIMEBase("application", "octet-stream")
                            part.set_payload(attachment.read())

                        # Encode file in ASCII characters to send by email
                        encoders.encode_base64(part)

                        # Add header as key/value pair to attachment part
                        part.add_header(
                            "Content-Disposition",
                            f"attachment; filename= {os.path.basename(attachment_path)}",
                        )

                        # Add attachment to message
                        msg.attach(part)

                    # Send the email after adding attachment
                    server.sendmail(sender_email, receiver_email, msg.as_string())
                    server.quit()

                    # Display success message for each email
                    messagebox.showinfo("Email Sent", f"{sender_email} has sent email successfully to {receiver_email}.")

            # Display success message after sending all emails
            messagebox.showinfo("Email Sent", "All emails have been sent successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
    csv_mail_window = tk.Toplevel(root)
    csv_mail_window.title("Multiple Mail with CSV")

    # Add image at the top
    csv_mail_image = Image.open("SpeedySend.png")
    csv_mail_image = ImageTk.PhotoImage(csv_mail_image)
    csv_image_label = tk.Label(csv_mail_window, image=csv_mail_image)
    csv_image_label.image = csv_mail_image  # Retain reference to image
    csv_image_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # Create menu button with submenus
    menu_button_icon = Image.open("menu_icon.png").resize((20, 20))
    menu_button_icon = ImageTk.PhotoImage(menu_button_icon)

    menu_button = tk.Menubutton(csv_mail_window, image=menu_button_icon, relief=tk.RAISED)
    menu_button.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    menu_button.image = menu_button_icon  # Retain reference to the image
    menu_button.menu = tk.Menu(menu_button, tearoff=0)
    menu_button["menu"] = menu_button.menu

    # Add submenus
    menu_button.menu.add_command(label="Save Draft", command=save_draft)
    menu_button.menu.add_command(label="Load Draft", command=load_draft)

    # Upload CSV label
    upload_label = tk.Label(csv_mail_window, text="Upload CSV:")
    upload_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

    # Entry field for displaying selected CSV file path
    csv_file_entry = tk.Entry(csv_mail_window, width=40)
    csv_file_entry.grid(row=1, column=1, padx=10, pady=5)

    # Browse button to select CSV file
    browse_button = tk.Button(csv_mail_window, text="Browse", command=browse_file)
    browse_button.grid(row=1, column=2, padx=10, pady=5)

    # Subject label and entry field
    subject_label = tk.Label(csv_mail_window, text="Subject:")
    subject_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    subject_entry = tk.Entry(csv_mail_window, width=40)
    subject_entry.grid(row=3, column=1, padx=10, pady=5)

    # Message label and text field
    message_label = tk.Label(csv_mail_window, text="Message:")
    message_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
    message_entry = tk.Text(csv_mail_window, width=40, height=10)
    message_entry.grid(row=4, column=1, padx=10, pady=5)

    # Attachment
    attachment_label = tk.Label(csv_mail_window, text="Attachment:")
    attachment_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")

    attachment_entry = tk.Entry(csv_mail_window, width=40)
    attachment_entry.grid(row=5, column=1, padx=10, pady=5)

    def attach_file():
        file_path = filedialog.askopenfilename()
        attachment_entry.delete(0, tk.END)
        attachment_entry.insert(0, file_path)

    attach_button_icon = Image.open("attachment.png").resize((20, 20))
    attach_button_icon = ImageTk.PhotoImage(attach_button_icon)

    attach_button = tk.Button(csv_mail_window, image=attach_button_icon, command=attach_file)
    attach_button.image = attach_button_icon
    attach_button.grid(row=5, column=2, padx=5)

    # Send Email button
    send_email_button = tk.Button(csv_mail_window, text="Send Email", bg="#008000", command=send_email_from_csv)
    send_email_button.grid(row=6, column=1, columnspan=2, pady=5)


root = tk.Tk()
root.title("Email Sender Login")
root.geometry("500x400")

# Header Image
header_image = Image.open("SpeedySend.png")
header_image = ImageTk.PhotoImage(header_image)
header_label = tk.Label(root, image=header_image)
header_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Center the login frame
login_frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
login_frame.grid(row=1, column=0, columnspan=3, padx=50, pady=20)

sender_email_entry = tk.Entry(login_frame, width=30, fg='grey', font=("Helvetica", 10))
sender_email_entry.insert(0, "Sender Email")
sender_email_entry.bind("<FocusIn>", lambda event: sender_email_entry.delete(0, "end"))
sender_email_entry.grid(row=0, column=1, padx=10, pady=5)

password_entry = tk.Entry(login_frame, show='*', width=30, fg='grey', font=("Helvetica", 10))
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", lambda event: password_entry.delete(0, "end"))
password_entry.grid(row=1, column=1, padx=10, pady=5)

show_password_button_icon = Image.open("eye.png").resize((20, 20))
show_password_button_icon = ImageTk.PhotoImage(show_password_button_icon)

show_password_button = tk.Button(login_frame, image=show_password_button_icon, command=toggle_password_visibility)
show_password_button.grid(row=1, column=2, padx=5)

signup_icon = Image.open("signup.png").resize((30, 30))
signup_icon = ImageTk.PhotoImage(signup_icon)

signup_button = tk.Button(login_frame, text="Signup", bg="#FF4F00", image=signup_icon, compound=tk.LEFT, command=signup)
signup_button.grid(row=2, column=1, padx=(5, 0), pady=2, columnspan=2)

# Create buttons for opening windows
single_mail_icon = Image.open("singlemail.png").resize((50, 50))
single_mail_icon = ImageTk.PhotoImage(single_mail_icon)
single_mail_button = tk.Button(root, text="Single Mail", bg="#3944BC", image=single_mail_icon, compound=tk.BOTTOM, command=open_single_mail_window)
single_mail_button.image = single_mail_icon
single_mail_button.grid(row=2, column=0, padx=50, pady=10, sticky='w')

multiple_mail_icon = Image.open("mutiplemail.png").resize((50, 50))
multiple_mail_icon = ImageTk.PhotoImage(multiple_mail_icon)
multiple_mail_button = tk.Button(root, text="Multiple Mail",bg="#3944BC", image=multiple_mail_icon, compound=tk.BOTTOM, command=open_multiple_mail_window)
multiple_mail_button.image = multiple_mail_icon
multiple_mail_button.grid(row=2, column=1, pady=10, sticky='n')

csv_mail_icon = Image.open("csvmail.png").resize((50, 50))
csv_mail_icon = ImageTk.PhotoImage(csv_mail_icon)
csv_mail_button = tk.Button(root, text="Mail with CSV",bg="#3944BC", image=csv_mail_icon, compound=tk.BOTTOM, command=open_csv_mail_window)
csv_mail_button.image = csv_mail_icon
csv_mail_button.grid(row=2, column=2, padx=(10, 50), pady=10, sticky='e')

root.mainloop()
