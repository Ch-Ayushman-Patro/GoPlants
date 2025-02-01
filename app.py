import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import threading

# Load the pre-trained model
model = tf.keras.models.load_model('model2.keras')

# Define the class labels
class_labels = ['aloevera', 'banana', 'bilimbi', 'cantaloupe', 'cassava', 'coconut', 
                'corn', 'cucumber', 'curcuma', 'eggplant', 'galangal', 'ginger', 
                'guava', 'kale', 'longbeans', 'mango', 'melon', 'orange', 'paddy', 
                'papaya', 'peper chili', 'pineapple', 'pomelo', 'shallot', 'soybeans', 
                'spinach', 'sweet potatoes', 'tobacco', 'waterapple', 'watermelon']

# Function to preprocess the image
def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize
    return img_array

# Function to classify the uploaded image
def classify_image():
    global img_path
    if not img_path:
        messagebox.showerror("Error", "Please upload an image first!")
        return

    def show_spinner():
        result_label.config(text="🔄 Classifying...")

    def perform_classification():
        img_array = prepare_image(img_path)
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)[0]
        confidence = np.max(predictions)

        # Update result label based on confidence level
        if confidence < 0.40:
            result_label.config(
                text="⚠️ Unpredictable: The uploaded item cannot be reliably classified.",
                wraplength=400, justify="center"
            )
        else:
            result_label.config(
                text=f"🌿 Predicted Class: {class_labels[predicted_class]}\nConfidence Level: {confidence:.2f}",
                wraplength=400, justify="center"
            )

    # Show spinner and classify in a separate thread to keep the UI responsive
    threading.Thread(target=show_spinner).start()
    threading.Thread(target=perform_classification).start()

# Function to upload and display image
def upload_image():
    global img_path
    img_path = filedialog.askopenfilename()

    if img_path:
        # Load and display the image using LANCZOS for resizing
        img = Image.open(img_path)
        img = img.resize((200, 200), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        # Update the image label
        image_label.config(image=img_tk)
        image_label.image = img_tk  # Keep a reference to avoid garbage collection
        result_label.config(text="")  # Clear previous results

# Function to create a gradient background
def create_gradient(canvas, width, height, color1, color2):
    '''Creates a gradient background from color1 to color2 on the canvas'''
    limit = 256
    r1, g1, b1 = root.winfo_rgb(color1)
    r2, g2, b2 = root.winfo_rgb(color2)

    r_ratio = (r2 - r1) / limit
    g_ratio = (g2 - g1) / limit
    b_ratio = (b2 - b1) / limit

    for i in range(limit):
        r = int(r1 + (r_ratio * i))
        g = int(g1 + (g_ratio * i))
        b = int(b1 + (b_ratio * i))
        color = f'#{r:04x}{g:04x}{b:04x}'
        canvas.create_rectangle(0, i * (height / limit), width, (i + 1) * (height / limit), outline=color, fill=color)

# Function to handle resizing of the window
def on_resize(event):
    # Clear the canvas
    canvas.delete("all")
    # Redraw the gradient based on new window dimensions
    create_gradient(canvas, event.width, event.height, "#e0f7fa", "#00695c")

# Enhanced UI with gradient background
root = tk.Tk()
root.title("🌿 Plant Image Classifier 🌱")
root.geometry("600x750")

# Create a canvas to hold the gradient background
canvas = tk.Canvas(root, width=600, height=750)
canvas.pack(fill="both", expand=True)

# Bind the resize event to the canvas
canvas.bind("<Configure>", on_resize)

# Create initial gradient
create_gradient(canvas, 600, 750, "#e0f7fa", "#00695c")  # Light teal to deep teal gradient

# Frame for central alignment with rounded corners
frame = tk.Frame(canvas, bg="#ffffff", bd=10, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=450, height=550)

# Custom fonts and styles
HEADER_FONT = ("Poppins", 20, "bold")
BUTTON_FONT = ("Arial", 12, "bold")
RESULT_FONT = ("Helvetica", 12, "bold")
THEME_COLOR = '#2d6a4f'  # Darker green for theme
BUTTON_COLOR = '#52b788'
HOVER_COLOR = '#d9ed92'

# Header Label
header_label = tk.Label(frame, text="🌿 Plant Image Classifier 🌱", font=HEADER_FONT, bg='#ffffff', fg=THEME_COLOR, bd=2)
header_label.pack(pady=20)

# Frame for image upload and classification buttons
button_frame = tk.Frame(frame, bg='#ffffff')
button_frame.pack(pady=10)

# Button styling with hover effect
def on_enter(e):
    e.widget['background'] = HOVER_COLOR

def on_leave(e):
    e.widget['background'] = BUTTON_COLOR

# Upload Button
upload_button = tk.Button(button_frame, text="Upload Image", command=upload_image, font=BUTTON_FONT, bg=BUTTON_COLOR, fg='white', padx=15, pady=5, relief='flat')
upload_button.grid(row=0, column=0, padx=20)
upload_button.bind("<Enter>", on_enter)
upload_button.bind("<Leave>", on_leave)

# Classify Button
classify_button = tk.Button(button_frame, text="Classify Image", command=classify_image, font=BUTTON_FONT, bg=BUTTON_COLOR, fg='white', padx=15, pady=5, relief='flat')
classify_button.grid(row=0, column=1, padx=20)
classify_button.bind("<Enter>", on_enter)
classify_button.bind("<Leave>", on_leave)

# Label to display the uploaded image
image_label = tk.Label(frame, bg='#ffffff', relief='solid', bd=2)
image_label.pack(pady=20)

# Label to display the prediction result
result_label = tk.Label(frame, text="", font=RESULT_FONT, bg='#ffffff', fg=THEME_COLOR, wraplength=400, justify="center")
result_label.pack()

# Footer with an enhanced design
footer_label = tk.Label(frame, text="Developed by The Perfect Mix", font=("Poppins", 10, "italic"), bg='#ffffff', fg=THEME_COLOR)
footer_label.pack(side=tk.BOTTOM, pady=10)

# Initialize img_path
img_path = ""

# Run the application
root.mainloop()
