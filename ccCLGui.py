import tkinter as tk
import ccCanvasList as cl

base = tk.Tk()

canvasFrame = tk.LabelFrame(base, text = "Sorting Blocks")
canvasFrame.grid(row = 0, column = 0, rowspan = 8, columnspan = 3)
canvas = tk.Canvas(canvasFrame, width = 800, height = 600)
canvas.pack()

L = cl.CanvasList(10, "maroon", "normal", canvas)

def runSort(algo : str):
	# Disable input on all controls
	controls = (
		delaySlider, elementsSlider,
		randomizeButton, reverseButton,
		bubbleSortButton, insertionSortButton,
		shellSortButton, mergeSortButton,
		quickSortButton, heapSortButton
	)
	for widget in controls:
		widget.configure(state = tk.DISABLED)
	# Run the sort or list method
	if algo == "random":
		L.randomize()
	elif algo == "reverse":
		L.reverse()
	elif algo == "bubble":
		L.bubbleSort(delaySlider.get())
	elif algo == "insert":
		L.insertionSort(delaySlider.get())
	elif algo == "shell":
		L.shellSort(delaySlider.get())
	elif algo == "merge":
		L.mergeSort(0, len(L.array), delaySlider.get())
	elif algo == "quick":
		L.quickSort(0, len(L.array) - 1, delaySlider.get())
	elif algo == "heap":
		L.heapSort(delaySlider.get())
	
	for widget in controls:
		widget.configure(state = tk.NORMAL)

delayFrame = tk.LabelFrame(base, text = "Delay on Swap or Write")
delayFrame.grid(row = 8, column = 0)
delaySlider = tk.Scale(
	delayFrame, orient = tk.HORIZONTAL,
	from_ = 0.0, to = 0.250,
	resolution = 0.002, length = 300
)
delaySlider.pack()

elementsFrame = tk.LabelFrame(base, text = "Sortable Elements")
elementsFrame.grid(row = 8, column = 1, columnspan = 2, sticky = tk.W)
elementsSlider = tk.Scale(
	elementsFrame, orient = tk.HORIZONTAL,
	from_ = 10, to = 800,
	resolution = 10, length = 300,
	command = lambda newSize : L.changeElements(int(newSize), "maroon", "normal")
)
elementsSlider.pack()

randomizeButton = tk.Button(
	base, text = "Randomize",
	command = lambda : runSort("random")
)
randomizeButton.grid(row = 0, column = 3)
reverseButton = tk.Button(
	base, text = "Reverse",
	command = lambda : runSort("reverse")
)
reverseButton.grid(row = 1, column = 3)

bubbleSortButton = tk.Button(
	base, text = "Bubble Sort",
	command = lambda : runSort("bubble")
)
bubbleSortButton.grid(row = 2, column = 3)
insertionSortButton = tk.Button(
	base, text = "Insertion Sort",
	command = lambda : runSort("insert")
)
insertionSortButton.grid(row = 3, column = 3)
shellSortButton = tk.Button(
	base, text = "Shell Sort",
	command = lambda : runSort("shell")
)
shellSortButton.grid(row = 4, column = 3)
mergeSortButton = tk.Button(
	base, text = "Merge Sort",
	command = lambda : runSort("merge")
)
mergeSortButton.grid(row = 5, column = 3)
quickSortButton = tk.Button(
	base, text = "Quick Sort",
	command = lambda : runSort("quick")
)
quickSortButton.grid(row = 6, column = 3)
heapSortButton = tk.Button(
	base, text = "Heap Sort",
	command = lambda : runSort("heap")
)
heapSortButton.grid(row = 7, column = 3)

base.mainloop()
