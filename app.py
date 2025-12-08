import gradio as gr
import time

def bubble_sort_visual(arr):
    steps = []
    arr = arr.copy()

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            steps.append(f"Comparing {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(f"Swapped → {arr}")
            else:
                steps.append(f"No swap → {arr}")
    return "\n".join(steps), arr


def run_sort(input_text):
    try:
        arr = list(map(int, input_text.split(",")))
    except:
        return "⚠️ Please enter a comma-separated list of integers.", []

    steps, sorted_arr = bubble_sort_visual(arr)
    return steps, sorted_arr


with gr.Blocks() as demo:
    gr.Markdown("# 🫧 Bubble Sort Visualizer")
    gr.Markdown(
        "Enter a list of integers separated by commas. "
        "The app will show each comparison and swap step-by-step."
    )

    input_box = gr.Textbox(label="Input Array (e.g. 5,3,8,1)")
    output_steps = gr.Textbox(label="Sorting Steps", lines=12)
    output_array = gr.Textbox(label="Final Sorted Array")

    run_button = gr.Button("Run Bubble Sort")
    run_button.click(run_sort, input_box, [output_steps, output_array])

demo.launch()
