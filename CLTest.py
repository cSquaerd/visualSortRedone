import tkinter as tk
import ccCanvasList as cl

elements = 400

base = tk.Tk()
myCanvas = tk.Canvas(base, width = 800, height = 600)
myCanvas.pack()

myList = cl.CanvasList(elements, "blue", "NORMAL", myCanvas)
print("Randomizing...")
myList.randomize()
print("Bubble Sorting...")
myList.bubbleSort(0.0)
print("Done! Press enter to continue...")
input()

del myList
myList = cl.CanvasList(elements, "gray", "NORMAL", myCanvas)
print("Randomizing...")
myList.randomize()
print("Quick Sorting (Right Pivots)...")
myList.quickSort(0, elements - 1, 0.001)
print("Done! Press enter to continue...")
input()

del myList
myList = cl.CanvasList(elements, "magenta", "NORMAL", myCanvas)
print("Randomizing...")
myList.randomize()
print("Quick Sorting (Random Pivots)...")
myList.quickSort(0, elements - 1, 0.001, True)
print("Done! Press enter to continue...")
input()

del myList
myList = cl.CanvasList(elements, "orange", "NORMAL", myCanvas)
print("Randomizing...")
myList.randomize()
print("Merge Sorting (O(n) space)...")
myList.mergeSort(0, elements, 0.001)
print("Complete! Press enter to exit...")
input()
del myList
