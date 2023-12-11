import tkinter as tk


def calculate_property_tax():
    try:
        # User Actual property input value
        actual_value = float(entry_actual_value.get())

        # Assessment value (60% of the actual value)
        assessment_value = 0.6 * actual_value

        # Property tax ($0.75 for each $100 of assessment value)
        property_tax = 0.75 * (assessment_value / 100)

        # Display the results
        result_text.set(f"Assessment Value: ${assessment_value:.2f}\nProperty Tax: ${property_tax:.2f}")
    except ValueError:
        result_text.set("Error! Please enter a valid numerical value.")


# Main window
root = tk.Tk()
root.title("Property Tax Calculator")

# Window Size
root.geometry('400x200')

# Result Widgets
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

# Textfield Label
label_actual_value = tk.Label(root, text="Enter Actual Property Value:")
label_actual_value.pack()

entry_actual_value = tk.Entry(root)
entry_actual_value.pack()

# Button
button_calculate = tk.Button(root, text="Calculate Property Tax", command=calculate_property_tax)
button_calculate.pack()

root.mainloop()
