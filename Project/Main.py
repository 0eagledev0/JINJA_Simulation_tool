import tkinter as tk
from tkinter import filedialog, font
from tools_jinja import *
variable=""
jinja=""


def browse_file(lettre):
    global variable, jinja
    if(lettre):
        selected_value = selected_option.get()
        match selected_value:
            case "Variable (Jinja) + Template (Jinja)":
                file_path = filedialog.askopenfilename(
                    filetypes=[("Jinja Files", "*.jinja;*.j2")]
                )
            case "Variable (Yaml) + Template (Jinja)":
                file_path = filedialog.askopenfilename(
                    filetypes=[("Yaml Files", "*.yml")]
                )
            case "Variable (JSON) + Template (Jinja)":
                file_path = filedialog.askopenfilename(
                    filetypes=[("Jinja Files", "*.json")]
                )
        variable = file_path
        if file_path:
            subtitle.config(text=f"File selected: {file_path}",fg="blue")
        else:
            subtitle.config(text="File not selected",fg="red")

    else:
        file_path = filedialog.askopenfilename(
            filetypes=[("Jinja Files", "*.jinja;*.j2")]
        )
        jinja = file_path
        if file_path:
            subtitleb.config(text=f"File selected: {file_path}",fg="blue")
        else:
            subtitleb.config(text="File not selected",fg="red")


def submit_action():
    def copy_to_clipboard():
        content = text_box.get("1.0", tk.END)
        new_window.clipboard_clear()
        new_window.clipboard_append(content)
        tk.messagebox.showinfo("Copied", "Text copied to clipboard")

    if variable == "" or jinja == "":
        tk.messagebox.showerror("Error", f"An error occurred:  unselected variable or jinja")
        return

    selected_value = selected_option.get()
    print("The choice:", selected_value)
    print("The variables:", variable)
    print("The jinja:", jinja)
    result_message = ""
    try:
        match selected_value:
            case "Variable (Jinja) + Template (Jinja)":
                result_message = variable_jinja(variable, jinja)
            case "Variable (Yaml) + Template (Jinja)":
                result_message = variable_YAML(variable, jinja)
            case "Variable (JSON) + Template (Jinja)":
                result_message = variable_JSON(variable, jinja)

        result_message = str(result_message)  # Ensure result_message is a string

        new_window = tk.Toplevel(root)
        new_window.title("Result")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_x = (screen_width // 2) - (900 // 2)
        position_y = (screen_height // 2) - (200 // 2)
        new_window.geometry(f"{900}x{400}+{position_x}+{position_y}")

        copy_button = tk.Button(new_window, text="Copy to the Clipboard", command=copy_to_clipboard)
        copy_button.pack(pady=10, anchor="n")
        text_box = tk.Text(new_window, wrap="word", fg="white", bg="black")
        text_box.pack(side="left", expand=True, fill="both")
        scrollbar = tk.Scrollbar(new_window, command=text_box.yview)
        scrollbar.pack(side="right", fill="y")
        text_box.config(yscrollcommand=scrollbar.set)
        text_box.insert(tk.END, result_message)

    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")



root = tk.Tk()
root.title("Interface Graphique")
window_width = 800
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_x =(screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
root.configure(bg="black")

title_font = font.Font(family="Arial", size=20, weight="bold", underline=5)
dropdown_font = font.Font(family="Arial", size=12)
button_font = font.Font(family="Arial", weight="bold", size=12)
subtitle_font = font.Font(family="Arial", weight="bold", size=10)
submit_button_font = font.Font(family="Arial", weight="bold", size=20)

title1 = tk.Label(root, text="Choose the options",bg="black",fg="white", font=title_font)
title1.pack(pady=10)
options = [
    "Variable (Jinja) + Template (Jinja)",
    "Variable (Yaml) + Template (Jinja)",
    "Variable (JSON) + Template (Jinja)"
]
selected_option = tk.StringVar(root)
selected_option.set(options[0])
dropdown =tk.OptionMenu(root,selected_option,*options)
menu = dropdown.nametowidget(dropdown.menuname)
menu.configure( fg="black", bg="white", font=dropdown_font)
dropdown.config(fg="black", bg="white", highlightthickness=1, font=dropdown_font)
dropdown.pack(pady=10)

title2 = tk.Label(root, text="Choose the variable file", bg="black", fg="white", font=title_font)
title2.pack(pady=10)
subtitle = tk.Label(root, text="File not selected", fg="red", bg="black" , font=subtitle_font)
subtitle.pack(pady=5)
browse_button1 = tk.Button(root, text="Browse", command=lambda: browse_file(True),fg="black",bg="white", font=button_font)
browse_button1.pack(pady=10)

title3 = tk.Label(root, text="Choose the template file",bg="black",fg="white", font=title_font)
title3.pack(pady=10)
subtitleb = tk.Label(root, text="File not selected",fg="red",bg="black" , font=subtitle_font)
subtitleb.pack(pady=5)
browse_button2 = tk.Button(root, text="Browse", command=lambda: browse_file(False),fg="black",bg="white", font=button_font)
browse_button2.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_action,fg="white",bg="blue", font=submit_button_font)
submit_button.pack(pady=10)
root.mainloop()













