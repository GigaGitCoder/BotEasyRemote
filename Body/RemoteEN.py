import tkinter as tk
from tkinter import filedialog
import webbrowser
import pystray
from PIL import Image, ImageTk
from pystray import MenuItem, Icon
import threading
import os
from colorama import Fore
import subprocess




process = None
Project_Path = os.path.dirname(__file__)

# Author information
username = "GigaGitCoder"
repository = "BotEasyRemote"
donateun = "ava_channel_live"

# Global variable for the icon
tray_icon = None

# Bot state flags
bot_running = False




def refresh_code_repair():
    if checkbox_var.get() == True:
        checkbox.config(bg="#5B009E", fg="white")
        
    elif checkbox_var.get() == False:
        checkbox.config(bg="#380061", fg="white")

# Path to the bot file
def bot_main():
    return open(rf"{Project_Path}\path.txt", 'r', encoding='utf-8').read() 

# Function to select a file
def select_file():
    file_path = filedialog.askopenfilename(title="Select bot file", filetypes=[("Python files", "*.py")])
    if file_path:
        entry_bot_path.delete(0, tk.END)  # Clear the current value
        entry_bot_path.insert(0, file_path)  # Insert the selected path

# Function to send the path to another file
def send_path():
    bot_path = entry_bot_path.get()
    open(rf"{Project_Path}\path.txt", 'w', encoding='utf-8').write(bot_path)  # Write the path to the file
    print(f"\n\nThe path to the bot file is now: {bot_path}\nOverwritten in path.txt\n")
    # Here you can add code to send the path to another file

def start_bot():
    file_path = bot_main()  # Specify the path to your file

    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        global bot_running
        global process
        bot_running = True


        if checkbox_var.get() == True:
            print("\n========start=======")

            # Open a new terminal and start the bot
            process = subprocess.Popen(['python', f'{file_path}'])        
            print("     Bot started!") 
            print("====================\n")  

        elif checkbox_var.get() == False:
            print(Fore.CYAN + "\n========start=======" + Fore.RESET)

            # Open a new terminal and start the bot
            process = subprocess.Popen(['python', f'{file_path}'])        
            print(Fore.GREEN + "     Bot started!" + Fore.RESET) 
            print(Fore.CYAN + "====================\n" + Fore.RESET)  
            
        update_button_states()

    except FileNotFoundError as e:
        print(e)
        tk.messagebox.showerror("Error", str(e))
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e}")
        tk.messagebox.showerror("Error", f"Error executing script: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        tk.messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def restart_bot():
    global process


    if checkbox_var.get() == True:
        print("\n~~~~~~~restart~~~~~~~")
        print("Bot is restarting!")  

        stop_bot()  # Stop the bot
        start_bot()  # Start the bot again

        print("~~~~~~~~~~~~~~~~~~~~~\n")
        
    elif checkbox_var.get() == False:
        print(Fore.CYAN + "\n~~~~~~~restart~~~~~~~" + Fore.RESET)
        print(Fore.YELLOW + "Bot is restarting!" + Fore.RESET + "\n")  

        stop_bot()  # Stop the bot
        start_bot()  # Start the bot again

        print(Fore.CYAN + "\n~~~~~~~~~~~~~~~~~~~~~\n" + Fore.RESET)
    
def stop_bot():
    global bot_running
    global process
    bot_running = False


    if checkbox_var.get() == True:
        print("\n========exit========")
        print("Bot is stopping!") 
        
        if process is not None:
            process.terminate()  # Stop the process
            process.wait()  # Wait for the process to finish
            process = None  # Reset the process variable

        print("   Bot stopped!") 
        print("====================\n") 

    elif checkbox_var.get() == False:
        print(Fore.CYAN + "\n========exit========" + Fore.RESET)
        print(Fore.YELLOW + "Bot is stopping!" + Fore.RESET) 
        
        if process is not None:
            process. terminate()  # Stop the process
            process.wait()  # Wait for the process to finish
            process = None  # Reset the process variable

        print(Fore.RED + "   Bot stopped!") 
        print(Fore.CYAN + "====================\n" + Fore.RESET) 
    update_button_states()

def open_author_github():
    webbrowser.open(f"https://github.com/{username}")

def open_repository_github():
    webbrowser.open(f"https://github.com/{username}/{repository}")

def open_cat_link(event):
    webbrowser.open(f"https://donationalerts.com/r/{donateun}")

def minimize_app():
    root.withdraw()  # Hide the main window

def restore_app():
    root.after(0, lambda: root.deiconify())  # Show the main window

def exit_app():
    global process
    if process is not None:
        print(Fore.RED + f"\n\nThe bot file {bot_main()} will be forcefully closed due to application exit!\n" + Fore.RESET)
        stop_bot()
    if tray_icon:
        tray_icon.stop()  # Stop the tray icon
    root.destroy()  # Close the application


# Update button states
def update_button_states():
    if bot_running:
        btn_start.config(state=tk.DISABLED)
        btn_start.config(bg="#41377B")
        btn_restart.config(state=tk.NORMAL)
        btn_restart.config(bg="#6A5ACD")
        btn_stop.config(state=tk.NORMAL)
        btn_stop.config(bg="#6A5ACD")
        btn_select_file.config(state=tk.DISABLED)
        btn_select_file.config(bg="#A51D2D")
        btn_send_path.config(state=tk.DISABLED)
        btn_send_path.config(bg="#A51D2D")
    else:
        btn_start.config(state=tk.NORMAL)
        btn_start.config(bg="#6A5ACD")
        btn_restart.config(state=tk.DISABLED)
        btn_restart.config(bg="#41377B")
        btn_stop.config(state=tk.DISABLED)
        btn_stop.config(bg="#41377B")
        btn_select_file.config(state=tk.NORMAL)
        btn_select_file.config(bg="#E1233A")
        btn_send_path.config(state=tk.NORMAL)
        btn_send_path.config(bg="#E1233A")

# Create a system tray icon
def create_tray_icon():
    global tray_icon
    # Load the icon from a file
    icon_path = os.path.join(os.path.dirname (__file__), rf'{Project_Path}\BER_Content\icon.png')  
    image = Image.open(icon_path)
    tray_icon = Icon("test_icon", image, "Bot Easy Remote", menu=pystray.Menu(
        MenuItem("Support", open_cat_link),
        MenuItem("Restore", restore_app),
        MenuItem("Exit", exit_app)
    ))
    tray_icon.run()

# Handle window closing
def on_closing():
    minimize_app()  # Hide the window instead of closing




# Create the main window
root = tk.Tk()
root.title("Bot Easy Remote")
root.geometry("650x540")  # Increase window size for log block
root.resizable(False, False)  # Prevent window resizing
root.configure(bg="#4B0082")  # Dark purple background


# Set the icon for the window
icon_path = os.path.join(os.path.dirname(__file__), rf'{Project_Path}\BER_Content\icon.png')  # Path to the icon
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)

# Function to create buttons with fixed size
def create_button(parent, text, command):
    button = tk.Button(parent, text=text, command=command, 
                       bg="#6A5ACD", fg="white", borderwidth=0,
                       relief="flat", padx=20, pady=10, font=("Arial", 12),
                       width=12, height=1, activebackground="#7D6FD3",
                       activeforeground="white", disabledforeground="#A8A8A8")  # Set fixed size
    return button




# Load Logo
logo_image_path = os.path.join(os.path.dirname(__file__), rf'{Project_Path}\BER_Content\BER_Logo.png')  # Ensure the file name matches
logo_image = Image.open(logo_image_path)
logo_photo = ImageTk.PhotoImage(logo_image)
cat_label = tk.Label(root, image=logo_photo, bg="#4B0082")
cat_label.pack(pady=0)


# Create buttons in the first row
frame1 = tk.Frame(root, bg="#4B0082")
frame1.pack(pady=20)

btn_start = create_button(frame1, "Start Bot", start_bot)
btn_start.grid(row=0, column=0, padx=10)

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(frame1, text="CodeFix (NonColor)", variable=checkbox_var, 
                          command=refresh_code_repair, bg="#380061", font=("Arial", 12), 
                          fg="white", selectcolor="#380061", activebackground="#4B0082", 
                          activeforeground="white", relief="sunken")
checkbox.grid(row=1, column=0, pady=(10, 0))

btn_restart = create_button(frame1, "Restart Bot", restart_bot)
btn_restart.grid(row=0, column=1, padx=10)
btn_restart.config(state=tk.DISABLED, bg="#41377B")  # Initially disabled

btn_stop = create_button(frame1, "Stop Bot", stop_bot)
btn_stop.grid(row=0, column=2, padx=10)
btn_stop.config(state=tk.DISABLED, bg="#41377B")  # Initially disabled


# Create an entry field for the bot file path
entry_bot_path = tk.Entry(root, width=50, font=("Arial", 12))
entry_bot_path.pack(padx=10, pady=(20,10))
entry_bot_path.insert(0, bot_main())

frame2 = tk.Frame(root, bg="#4B0082")
frame2.pack(pady=(0,60))

# Button to select a file
btn_select_file = tk.Button(frame2, text="Select File", command=select_file, bg="#E1233A", 
                            fg="white", borderwidth=0, relief="flat", padx=20, pady=10, font=("Arial", 12), 
                            activebackground="#EE4458", activeforeground="white", disabledforeground="#A8A8A8")
btn_select_file.grid(row=0, column=0, padx=30)

# Button to send the path
btn_send_path = tk.Button(frame2, text="Send Path", command=send_path, bg="#E1233A", 
                          fg="white", borderwidth=0, relief="flat", padx=20, pady=10, font=("Arial", 12), 
                          activebackground="#EE4458", activeforeground="white", disabledforeground="#A8A8A8")
btn_send_path.grid(row=0, column=1, padx=30)


# Create buttons in the second row
frame3 = tk.Frame(root, bg="#4B0082")
frame3.pack(pady=10)

btn_author = create_button(frame3, "Author on GitHub", open_author_github)
btn_author.grid(row=0, column=0, padx=10)

btn_repo = create_button(frame3, "Repository on GitHub", open_repository_github)
btn_repo.grid(row=0, column=1, padx=10)

btn_minimize = create_button(frame3, "Exit", exit_app)
btn_minimize.grid(row=0, column=2, padx=10)


# Load cat image
cat_image_path = os.path.join(os.path.dirname(__file__), rf'{Project_Path}\BER_Content\cat.png')  # Ensure the file name matches
cat_image = Image.open(cat_image_path)
cat_image = cat_image.resize((50, 50), Image.LANCZOS)  # Resize the image
cat_photo = ImageTk.PhotoImage(cat_image)

# Add the cat image to the bottom right corner
cat_label = tk.Label(root, image=cat_photo, bg="#4B0082")
cat_label.pack(side=tk.BOTTOM, anchor='se', padx=10, pady=10)  # Bottom right corner with padding

# Add action to the cat image
cat_label.bind("<Button-1>", open_cat_link)


# Bind the window closing event to the on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the tray icon in a separate thread
threading.Thread(target=create_tray_icon, daemon=True).start()

# Start the main application loop
root.mainloop()