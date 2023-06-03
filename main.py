import subprocess
import tkinter as tk
from tkinter import messagebox
import webbrowser

def get_wifi_password():
    try:
        # Run the command to get the saved Wi-Fi profiles
        profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profile_names = [line.split(':')[1].strip() for line in profiles if "All User Profile" in line]

        # Get the password for each profile
        passwords = []
        for name in profile_names:
            # Run the command to get the Wi-Fi password for the given profile
            password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8').split('\n')
            password = [line.split(':')[1].strip() for line in password if "Key Content" in line]

            # Append the Wi-Fi profile name and password to the list
            if len(password) > 0:
                passwords.append((name, password[0]))

        # Create a custom dialog window to display the Wi-Fi passwords
        dialog = tk.Toplevel(window)
        dialog.title("Wi-Fi Passwords")
        dialog.geometry("400x300")
        dialog.configure(bg='#F2F2F2')
        dialog.resizable(False, False)

        # Create a text widget to show the passwords
        text_widget = tk.Text(dialog, font=("Arial", 12), bg='#F2F2F2')
        text_widget.pack(fill=tk.BOTH, expand=True)

        # Display the Wi-Fi passwords in the text widget
        if len(passwords) > 0:
            for profile in passwords:
                text_widget.insert(tk.END, f"Wi-Fi Profile: {profile[0]}\nPassword: {profile[1]}\n\n")
        else:
            text_widget.insert(tk.END, "No saved Wi-Fi profiles found.")

        # Disable text editing
        text_widget.configure(state="disabled")

        # Run the dialog window
        dialog.mainloop()

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", "Error occurred while retrieving Wi-Fi passwords.")

def open_github():
    webbrowser.open("https://github.com/Onionkey")

# Create the main window
window = tk.Tk()
window.title("Wi-Fi Password Viewer")
window.geometry("400x350")
window.configure(bg='#F2F2F2')

# Create a button to trigger the password retrieval
button = tk.Button(window, text="Get Wi-Fi Passwords", font=("Arial", 12), command=lambda: get_wifi_password(), bg='#007BFF', fg='white')
button.pack(pady=10)

# Create a label with the creator information and GitHub link
creator_label = tk.Label(window, text="Created by Hoso", font=("Arial", 10), bg='#F2F2F2')
creator_label.pack()

github_link = tk.Label(window, text="GitHub", font=("Arial", 10, "underline"), fg="blue", bg='#F2F2F2', cursor="hand2")
github_link.pack(pady=5)
github_link.bind("<Button-1>", lambda e: open_github())

# Create a label for your logo (replace the 'logo.png' with the actual path to your logo image)
logo_image = tk.PhotoImage(file='lg/Onionkey.png')
logo_label = tk.Label(window, image=logo_image, bg='#F2F2F2')
logo_label.pack(pady=10)

# Run the main event loop
window.mainloop()
