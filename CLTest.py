import tkinter as tk
import ccCanvasList as cl

elements = 50

base = tk.Tk()
myCanvas = tk.Canvas(base, width = 800, height = 600)
myCanvas.pack()

myList = cl.CanvasList(elements, "blue", "RANDOM", myCanvas)
print("Randomizing...")
myList.randomize()
print("Bubble Sorting...")
myList.bubbleSort(0.010)
print("Done! Press enter to continue...")
input()

del myList
myList = cl.CanvasList(elements, "navy", "RANDOM", myCanvas)
print("Randomizing...")
myList.randomize()
print("Insertion Sorting...")
myList.insertionSort(0.010)
print("Done! Press enter to continue...")
input()

del myList
myList = cl.CanvasList(elements, "purple", "RANDOM", myCanvas)
print("Randomizing...")
myList.randomize()
print("Shell Sorting...")
myList.shellSort(0.010)
print("Done! Press enter to continue...")
input()

del myList
myList = cl.CanvasList(elements, "gray", "RANDOM", myCanvas)
print("Randomizing...")
myList.randomize()
print("Quick Sorting (Right Pivots)...")
myList.quickSort(0, elements - 1, 0.100)
print("Done! Press enter to continue...")
input()

del myList
myList = cl.CanvasList(elements, "magenta", "RANDOM", myCanvas)
print("Randomizing...")
myList.randomize()
print("Quick Sorting (Random Pivots)...")
myList.quickSort(0, elements - 1, 0.100, True)
print("Done! Press enter to continue...")
input()

del myList
myList = cl.CanvasList(elements, "orange", "RANDOM", myCanvas)
print("Randomizing...")
myList.randomize()
print("Merge Sorting (O(n) space)...")
myList.mergeSort(0, elements, 0.100)
print("Done! Press enter to continue...")
input()

del myList
myList = cl.CanvasList(elements, "green", "RANDOM", myCanvas)
print("Randomizing...")
myList.randomize()
print("Heap Sorting...")
myList.heapSort(0.100)
print("Complete! Press enter to exit...")
input()
del myList
