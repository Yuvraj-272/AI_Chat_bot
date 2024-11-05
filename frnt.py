import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext

# Configure Google Generative AI API
genai.configure(api_key="AIzaSyBsCw7_w-E_RBq-hF2mI8p9t51fHbp8xdw")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
system_prompt = "Pretend as a medieval era servant "

# Function to handle user input and display response
def get_response():
    user_input = user_entry.get()  # Get user input from entry widget
    if user_input.strip().lower() == "bye":
        root.destroy()  # Close the window if user says "bye"
        return

    # Combine system prompt with user input and send to AI model
    prompt = system_prompt + user_input
    try:
        response = model.generate_content(prompt=prompt)  # Generate AI response
        ai_response = response.text
    except Exception as e:
        ai_response = f"Error: {e}"  # Handle any errors gracefully

    # Display conversation in the chat log
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    chat_log.insert(tk.END, "AI: " + ai_response + "\n\n")
    chat_log.yview(tk.END)  # Scroll to the end of the chat log
    user_entry.delete(0, tk.END)  # Clear input field

# Set up the main application window
root = tk.Tk()
root.title("Medieval AI Servant")

# Text area to display conversation
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_log.pack(padx=10, pady=10)
chat_log.insert(tk.END, "Welcome! I am your medieval AI servant. Type 'bye' to exit.\n\n")

# Entry field for user input
user_entry = tk.Entry(root, width=50, font=("Arial", 12))
user_entry.pack(padx=10, pady=5)
user_entry.focus()

# Button to send the input
send_button = tk.Button(root, text="Send", command=get_response, font=("Arial", 12))
send_button.pack(pady=5)

# Run the application
root.mainloop()
