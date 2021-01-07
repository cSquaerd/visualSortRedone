import tkinter as tk
import random as rnd
import time

class CanvasList:
	def __init__(
		self,
		items : int,
		dims : tuple,
		color : str,
		mode : str,
		canvas : tk.Canvas
	):
		dw = dims[0] / items
		dh = dims[1] / items
		self.canvas = canvas
		self.array = [
			self.canvas.create_rectangle(
				0 + i * dw, dims[1],
				dw + i * dw, dims[1] - (i + 1) * dh,
				fill = color, width = 0
			) for i in range(items)
		]
		self.deltaWidth = dw

	def destroy(self):
		self.canvas.delete("all")
		self.array = []

	def value(self, i):
		return self.canvas.coords(self.array[i])[1]

	def swap(self, a, b):
		if a == b:
			return

		A = self.array[a]
		B = self.array[b]
		xA = self.canvas.coords(A)[0]
		xB = self.canvas.coords(B)[0]
		distance = abs(xA - xB)

		if xA > xB:
			self.canvas.move(A, -distance, 0)
			self.canvas.move(B, distance, 0)
		else:
			self.canvas.move(A, distance, 0)
			self.canvas.move(B, -distance, 0)
		self.canvas.update()

		temp = self.array[a]
		self.array[a] = self.array[b]
		self.array[b] = temp

	def compare(self, a, b, op):
		if op.upper() not in ("LEQ", "LES", "GRT", "GEQ", "EQL"):
			print("Operation Error in CanvasList.compare: Bad Operation '" + op + "'")
			return None
		
		if op.upper() == "EQL":
			return self.value(a) == self.value(b)
		# Note: The signs are reversed since a smaller y-coord means a taller rectangle
		# since the y-axis of a Canvas points down, not up
		elif op.upper() == "LEQ":
			return self.value(a) >= self.value(b)
		elif op.upper() == "GEQ":
			return self.value(a) <= self.value(b)
		elif op.upper() == "GRT":
			return self.value(a) < self.value(b)
		elif op.upper() == "LES":
			return self.value(a) > self.value(b)

	def randomize(self):
		for i in range(len(self.array)):
			self.swap(i, rnd.randint(0, len(self.array) - 1))

	def bubbleSort(self, delay : float = 0.050):
		length = len(self.array)
		for i in range(length):
			swaps = 0
			for j in range(length - 1 - i):
				if self.compare(j, j + 1, "geq"):
					time.sleep(delay)
					self.swap(j, j + 1)
					swaps += 1
			if swaps == 0:
				break

	def partitionRightPivot(
		self,
		low : int,
		high : int,
		delay : float,
		random : bool = False
	) -> int:
		i = low # Mark the beginning the lesser partition

		if random: # Choose a random pivot
			time.sleep(delay)
			self.swap(high, rnd.randint(low, high))

		for j in range(low, high + 1): # For every element
			if self.compare(j, high, "les"): # Swap lesser items
				time.sleep(delay)
				self.swap(i, j) # into the lesser partition
				i += 1 # and mark it accordingly
		time.sleep(delay)
		self.swap(i, high) # Move the pivot in between the partitions to sort it
		return i

	def quickSort(
		self,
		low : int,
		high : int,
		delay : float = 0.050,
		random : bool = False
	):
		if low < high:
			p = self.partitionRightPivot(low, high, delay, random)
			self.quickSort(low, p - 1, delay)
			self.quickSort(p + 1, high, delay)
