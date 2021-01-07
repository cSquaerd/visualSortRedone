import tkinter as tk
import ccCanvasList as cl

elements = 400

base = tk.Tk()
myCanvas = tk.Canvas(base, width = 800, height = 600)
myCanvas.pack()
myList = cl.CanvasList(elements, (800, 600), "blue", "", myCanvas)
print("Randomizing...")
myList.randomize()
print("Bubble Sorting...")
myList.bubbleSort(0.0)
print("Done! Press any key to continue...")
input()
print("Randomizing...")
myList.randomize()
print("Quick Sorting (Right Pivots)...")
myList.quickSort(0, elements - 1, 0.001)
print("Done! Press any key to continue...")
input()
print("Randomizing...")
myList.randomize()
print("Quick Sorting (Random Pivots)...")
myList.quickSort(0, elements - 1, 0.001, True)
print("Complete! Press any key to exit...")
input()
