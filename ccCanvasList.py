import tkinter as tk
import random as rnd
import time

class CanvasList:
	def __init__(
		self,
		items : int,
		color : str,
		mode : str,
		canvas : tk.Canvas,
		**kwargs : dict
	):
		self.canvas = canvas
		self.dims = (
			int(
				self.canvas.config()["width"][-1]
			),
			int(
				self.canvas.config()["height"][-1]
			)
		)

		dw = self.dims[0] / items
		dh = self.dims[1] / items
		self.dw = dw

		if mode.upper() == "NORMAL":
			self.array = [
				self.canvas.create_rectangle(
					i * dw, self.dims[1],
					(i + 1) * dw, self.dims[1] - (i + 1) * dh,
					fill = color, width = 0
				) for i in range(items)
			]
		elif mode.upper() == "MERGE":
			offset = kwargs["offset"]
			x0 = dw * offset
			self.array = [
				self.canvas.create_rectangle(
					x0 + i * dw, self.dims[1],
					x0 + (i + 1) * dw, height
				) for height in kwargs["heights"]
			]

	def __del__(self):
		for i in self.array:
			self.canvas.delete(i)

	def value(self, i):
		return self.canvas.coords(self.array[i])[1]

	def xpos(self, i):
		return self.canvas.coords(self.array[i])[0]

	def swap(self, a, b):
		if a == b:
			return

		xA = self.xpos(a) 
		xB = self.xpos(b)
		distance = abs(xA - xB)

		if xA > xB:
			self.canvas.move(self.array[a], -distance, 0)
			self.canvas.move(self.array[b], distance, 0)
		else:
			self.canvas.move(self.array[a], distance, 0)
			self.canvas.move(self.array[b], -distance, 0)
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

	def copyOver(self, iSelf, source, iSource):
		x = self.xpos(iSelf) # Get the x-position of the shape
		self.canvas.delete(self.array[iSelf]) # Delete the old shape
		self.array[iSelf] = self.canvas.create_rectangle(
			x, self.dims[1], x + self.dw, source.value(iSource)
		) # Make a new shape and store it's new ID in the spot of the old shape

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

