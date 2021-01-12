import tkinter as tk
import ccCanvasList as cl

base = tk.Tk()

canvasFrame = tk.LabelFrame(base, text = "Sorting Blocks")
canvasFrame.grid(row = 0, column = 0, rowspan = 8, columnspan = 3)
canvas = tk.Canvas(canvasFrame, width = 800, height = 600)
canvas.pack()

L = cl.CanvasList(10, "maroon", "normal", canvas)

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

randomizeButton = tk.Button(base, text = "Randomize", command = L.randomize)
randomizeButton.grid(row = 0, column = 3)
reverseButton = tk.Button(base, text = "Reverse", command = L.reverse)
reverseButton.grid(row = 1, column = 3)

bubbleSortButton = tk.Button(
	base, text = "Bubble Sort",
	command = lambda : L.bubbleSort(delaySlider.get())
)
bubbleSortButton.grid(row = 2, column = 3)
insertionSortButton = tk.Button(
	base, text = "Insertion Sort",
	command = lambda : L.insertionSort(delaySlider.get())
)
insertionSortButton.grid(row = 3, column = 3)
shellSortButton = tk.Button(
	base, text = "Shell Sort",
	command = lambda : L.shellSort(delaySlider.get())
)
shellSortButton.grid(row = 4, column = 3)
mergeSortButton = tk.Button(
	base, text = "Merge Sort",
	command = lambda : L.mergeSort(0, len(L.array), delaySlider.get())
)
mergeSortButton.grid(row = 5, column = 3)
quickSortButton = tk.Button(
	base, text = "Quick Sort",
	command = lambda : L.quickSort(0, len(L.array) - 1, delaySlider.get())
)
quickSortButton.grid(row = 6, column = 3)
heapSortButton = tk.Button(
	base, text = "Heap Sort",
	command = lambda : L.heapSort(delaySlider.get())
)
heapSortButton.grid(row = 7, column = 3)

base.mainloop()
