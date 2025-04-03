import tkinter as tk
from tkinter import messagebox
from openai_process import process_openai

# This is used to track previous responses to allow for context in the conversation.
history = []

def submit_form():
    global history

    user_input = input_field.get()
    if user_input.strip():
        try:
            # Call the process_openai function with the user input
            result = process_openai(user_input, history)
            print('results from chatform:')
            # print(result.output_text)
            # print(result)
            print(result.choices[0].message.content)

            history = []
            for item in result.choices:
                print(item)
                history.append({"role": item.message.role, "content": item.message.content})

            # print('History variable value:')
            # print(history)

            # Display the output from process_openai
            messagebox.showinfo("Response", result.choices[0].message.content)

            # Append the response to the textbox
            response_box.insert(tk.END, f"User: {user_input}\nAI: {result.choices[0].message.content}\n\n")
            response_box.see(tk.END)  # Scroll to the bottom
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Input Error", "Please enter some text.")

# Create the main application window
app = tk.Tk()
app.title("Chatter")

# Create and place the input field
tk.Label(app, text="What do you want Chatter to do?").pack(pady=5)
input_field = tk.Entry(app, width=50)
input_field.pack(pady=5)

# Create and place the submit button
submit_button = tk.Button(app, text="Submit", command=submit_form)
submit_button.pack(pady=10)

# Create and place the response textbox
response_box = tk.Text(app, height=15, width=60, state=tk.NORMAL)
response_box.pack(pady=10)

# Run the application
app.mainloop()