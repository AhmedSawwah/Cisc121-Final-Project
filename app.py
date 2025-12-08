import gradio as gr  # Import Gradio for creating the web interface
import time          # Imported but not used in this code

# Function to perform bubble sort and log each step
def bubble_sort_visual(arr):
    steps = []          # List to store messages for each comparison/swap
    arr = arr.copy()    # Copy input array to avoid modifying the original

    n = len(arr)        # Get length of array
    for i in range(n):  # Outer loop for passes
        for j in range(0, n - i - 1):  # Inner loop for adjacent comparisons
            steps.append(f"Comparing {arr[j]} and {arr[j+1]}")  # Log comparison
            if arr[j] > arr[j + 1]:      # Check if a swap is needed
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                steps.append(f"Swapped → {arr}")        # Log swap
            else:
                steps.append(f"No swap → {arr}")       # Log no swap
    return "\n".join(steps), arr  # Return all step messages and sorted array

# Function to handle user input and run the sorting
def run_sort(input_text):
    try:
        arr = list(map(int, input_text.split(",")))  # Convert input string to list of integers
    except:
        # Return error message if conversion fails
        return "⚠️ Please enter a comma-separated list of integers.", []

    steps, sorted_arr = bubble_sort_visual(arr)  # Run bubble sort with logging
    return steps, sorted_arr                      # Return steps and final sorted array

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# 🫧 Bubble Sort Visualizer")  # Title
    gr.Markdown(
        "Enter a list of integers separated by commas. "
        "The app will show each comparison and swap step-by-step."
    )  # Instructions

    # Input and output components
    input_box = gr.Textbox(label="Input Array (e.g. 5,3,8,1)")
    output_steps = gr.Textbox(label="Sorting Steps", lines=12)
    output_array = gr.Textbox(label="Final Sorted Array")

    run_button = gr.Button("Run Bubble Sort")  # Button to start sorting
    run_button.click(run_sort, input_box, [output_steps, output_array])  # Link button to function

demo.launch()  # Launch the web app
