import tkinter as tk # Import the tkinter library with the alias 'tk'
from tkinter import messagebox  # Import the messagebox module from tkinter
import smtplib  # Import the smtplib module for sending emails
from email.mime.text import MIMEText  # Import MIMEText for creating email messages
from email.mime.multipart import MIMEMultipart  # Import MIMEMultipart for creating email messages with attachments

root = tk.Tk()  # Create a Tkinter window instance
root.title("Email Application")  # Set the title of the window
root.geometry("600x500")
root.resizable(False,False)

def send_email():
    # Get user input from the entry widgets
    sender_email = sender_email_entry.get()  # Retrieve the sender email address from the entry widget
    receiver_email = receiver_email_entry.get()  # Retrieve the receiver email address from the entry widget
    subject = subject_entry.get()  # Retrieve the email subject from the entry widget
    body = body_text.get("1.0", tk.END)  # Retrieve the email body from the text widget
    password = password_entry.get() # Retrieve the password from the entry


    # Create the message
    message = MIMEMultipart()  # Create a MIMEMultipart instance for the email message
    message['From'] = sender_email  # Set the sender email address in the message
    message['To'] = receiver_email  # Set the receiver email address in the message
    message['Subject'] = subject  # Set the email subject in the message
    message.attach(MIMEText(body, 'plain'))  # Attach the email body to the message

    try:
        # Connect to SMTP server and send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as mail_server:  # Connect to the Gmail SMTP server securely
            mail_server.login(sender_email, password)  # Login to the SMTP server with the sender's email and password
            mail_server.send_message(message)  # Send the email message
        messagebox.showinfo("Success", f"Message has been sent to {receiver_email} successfully.")  # Display success message
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")  # Display error message if sending fails


# Labels
sender = tk.Label(root, text="Sender:", font="Arial 15 underline")
receiver = tk.Label(root, text="Receiver:", font="Arial 15 underline")
subject_line = tk.Label(root, text="Subject:", font="Arial 15 underline")
body_message = tk.Label(root, text="Body:", font="Arial 15 underline")
password_label = tk.Label(root, text="Password:", font="Arial 15 underline")

# Place the labels
sender.place(x=10, y=10)
password_label.place(x=10, y=40)  # Adjusted placement of password label
receiver.place(x=10, y=70)
subject_line.place(x=10, y=100)
body_message.place(x=10, y=130)

# Add the text entry widgets
sender_email_entry = tk.Entry(root, width=30, bg="light grey", font=("Arial", 12))
sender_email_entry.place(x=110, y=15)

password_entry = tk.Entry(root, show="*", width=30, bg="light grey", font=("Arial", 12))
password_entry.place(x=110, y=45)  # Adjusted placement of password entry

receiver_email_entry = tk.Entry(root, width=30, bg="light grey", font=("Arial", 12))
receiver_email_entry.place(x=110, y=75)

subject_entry = tk.Entry(root, width=30, bg="light grey", font=("Arial", 12))
subject_entry.place(x=110, y=105)

body_text = tk.Text(root, bg="light grey", width=55, height=12, font=("Arial", 12))
body_text.place(x=80, y=135)

send_button = tk.Button(root, bg="light grey", text="Send", font=("Arial Bold", 12), width=10, height=2, command=send_email)
send_button.place(x=250, y=400)

root.mainloop()



