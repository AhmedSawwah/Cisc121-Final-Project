# Bubble Sort Visualizer

## Demo
Screenshots or GIFs of the app running with sample inputs.
### Normal Case - Unsorted Array
![Normal Case](https://github.com/AhmedSawwah/Cisc121-Final-Project/blob/main/screenshots/Screenshot%202025-12-08%20165011.png?raw=true)

### Already Sorted
![Already Sorted](https://github.com/AhmedSawwah/Cisc121-Final-Project/blob/main/screenshots/Screenshot%202025-12-08%20165144.png?raw=true)

### Reverse Sorted Array
![reverse sorted](https://github.com/AhmedSawwah/Cisc121-Final-Project/blob/main/screenshots/Screenshot%202025-12-08%20165217.png?raw=true)

### Duplicates Array
![Duplicates Array](https://github.com/AhmedSawwah/Cisc121-Final-Project/blob/main/screenshots/Screenshot%202025-12-08%20165247.png?raw=true)

### Two Elements Array
![Two Elements Array](https://github.com/AhmedSawwah/Cisc121-Final-Project/blob/main/screenshots/Screenshot%202025-12-08%20165348.png?raw=true)

### One Element
![One Elemenet](https://github.com/AhmedSawwah/Cisc121-Final-Project/blob/main/screenshots/Screenshot%202025-12-08%20165422.png?raw=true)

---

## Problem Breakdown & Computational Thinking
Why did i choose bubblesort? Bubble Sort works so well that I chose it because it is one of the easiest sorting algorithms I can start to implement and understand. It works in very simple logic: compare those adjacent elements, then swap the elements if they are not in the right order. That makes it perfect for describing basic sorts, comparisons, swaps, iterative passes through a list. Even though Bubble Sort is not efficient with extensive data set at first glance (due to its time complexity of n squared), it is frequently used in introductory programming exercises since the algorithm can be easily traced from one end and debugged and modified. And its simplicity ensures that it is a useful jumping-off point before you master anything similar to merge sort or quicksort.

heres my huggingface space link: https://huggingface.co/spaces/AhmedSawwah/BubbleSortAlg

heres the flowchart:
![flowchart](https://github.com/AhmedSawwah/Cisc121-Final-Project/blob/main/screenshots/Screenshot%202025-12-11%20214038.png?raw=true)

### Decomposition
The bubble sort algorithm breaks down into these smaller steps:

Parse user input (comma-separated integers) into a list
Iterate through the list multiple times (n-1 passes for n elements)
In each pass, compare adjacent elements
Swap elements if they are in the wrong order
Track and record each comparison and swap
Repeat until no swaps are needed (list is sorted)
Display the step-by-step process and final result

### Pattern Recognition
The algorithm follows a repeating pattern:

Compare: Check if current element > next element
Swap: If true, exchange their positions
Record: Capture the state after each swap
Move: Advance to the next pair of adjacent elements
Repeat: Continue until reaching the end, then start a new pass
The largest unsorted element "bubbles up" to its correct position in each pass

### Abstraction
Details to SHOW the user:

The input array
Each comparison being made (highlighting which two elements)
Each swap that occurs with the updated array state
The final sorted array
Visual indication of sorting progress

Details to DISCARD (not shown):

Loop counters and index variables
Internal function calls
Memory addresses
Pass number details (unless you want to show which pass you're on)
Efficiency metrics (time complexity calculations)

### Algorithm Design
Input → Processing → Output Flow:
Input (GUI):

User enters comma-separated integers in a text box (e.g., "5,3,8,1")
Data type: String → converted to List of Integers

Processing:

Parse and validate input
Execute bubble sort algorithm
Capture each state change (comparison/swap) as a text description
Store all steps in a list

Output (GUI):

Display sorting steps in a scrollable text area showing each swap
Display the final sorted array in a separate output field
User clicks "Run Bubble Sort" button to trigger the process

GUI Structure:

Input: Gradio Textbox
Output 1: Gradio Textbox (multi-line) for step-by-step sorting process
Output 2: Gradio Textbox for final sorted result
Button: Triggers the sorting function

---

### Author and Acknowledgment
- Ahmed ElSawwah
- Gradio library for the UI framework
- Course Materials from Cisc121
- Project Guidelines
- Chatgpt 4 in commenting on the algorithm
