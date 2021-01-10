import tkinter as tk
import random as rnd
import time

class CanvasList:
	def __init__(
		self, items : int, color : str,
		mode : str, canvas : tk.Canvas, **kwargs : dict
	):
		self.canvas = canvas
		self.color = color
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
		elif mode.upper() == "RANDOM":
			self.array = [
				self.canvas.create_rectangle(
					i * dw, self.dims[1],
					(i + 1) * dw, self.dims[1] - rnd.randint(1, items) * dh,
					fill = color, width = 0
				) for i in range(items)
			]
		elif mode.upper() == "MERGE":
			x0 = kwargs["offset"]
			self.array = [
				self.canvas.create_rectangle(
					x0 + i * dw, self.dims[1],
					x0 + (i + 1) * dw, kwargs["heights"][i],
					fill = color, width = 0
				) for i in range(len(kwargs["heights"]))
			]
		#	for r in self.array:
		#		self.canvas.tag_lower(r)

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
			x, self.dims[1], x + self.dw, source.value(iSource),
			fill = self.color, width = 0
		) # Make a new shape and store it's new ID in the spot of the old shape

	def write(self, index : int, value : float, delay : float):
		x = self.xpos(index)
		self.canvas.delete(self.array[index])
		time.sleep(delay)
		self.array[index] = self.canvas.create_rectangle(
			x, self.dims[1], x + self.dw, value,
			fill = self.color, width = 0
		)
		self.canvas.update()

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
		self, low : int, high : int,
		delay : float, random : bool
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
		self, low : int, high : int,
		delay : float = 0.050,random : bool = False
	):
		if low < high:
			p = self.partitionRightPivot(low, high, delay, random)
			self.quickSort(low, p - 1, delay)
			self.quickSort(p + 1, high, delay)

	def mergeOver(
		self, baseL : int, lenL : int,
		baseR : int, lenR : int, delay : float
	):
		source = CanvasList(
			len(self.array),
			"red",
			"MERGE",
			self.canvas,
			offset = self.xpos(baseL),
			heights = [self.value(i) for i in range(baseL, baseL + lenL + lenR)]
		)
	#	print("Source", source.array)
		sourceL = 0
		sourceR = lenL

		for i in range(baseL, baseL + lenL + lenR):
		#	print("\t", end = '')
		#	print(i, sourceL, sourceR)
			if sourceR == lenL + lenR or ( \
				sourceL < lenL and source.compare(sourceL, sourceR, "les") \
			):
				self.copyOver(i, source, sourceL)
				sourceL += 1
			else:
				self.copyOver(i, source, sourceR)
				sourceR += 1

			time.sleep(delay)
			self.canvas.update()

	def mergeSort(self, base : int, length : int, delay : float = 0.050):
		if length > 1:
			lenL = length // 2
			lenR = length - lenL
			baseL = base
			baseR = base + lenL
		#	print(baseL, lenL, baseR, lenR)

			self.mergeSort(baseL, lenL, delay)
			self.mergeSort(baseR, lenR, delay)

			self.mergeOver(baseL, lenL, baseR, lenR, delay)

	def heapify(self, iHead : int, heapSize : int, delay : float):
		iLeft = 2 * iHead + 1
		iRight = 2 * iHead + 2
		iMax = iHead

		if iLeft < heapSize and self.compare(iLeft, iHead, "grt"):
			iMax = iLeft
		if iRight < heapSize and self.compare(iRight, iMax, "grt"):
			iMax = iRight

		if iMax != iHead:
			time.sleep(delay)
			self.swap(iMax, iHead)

	def buildHeap(self, length : int, delay : float):
		for i in range(length // 2, -1, -1):
			self.heapify(i, length, delay)

	def heapSort(self, delay : float = 0.050):
		self.buildHeap(len(self.array), delay)

		for i in range(len(self.array) -1, 0, -1):
			time.sleep(delay)
			self.swap(0, i)
			self.buildHeap(i, delay)

	def insertionSort(self, delay : float):
		for i in range(1, len(self.array)):
			j = i - 1
			while j >= 0 and self.compare(j, j + 1, "grt"):
				time.sleep(delay)
				self.swap(j, j + 1)
				j -= 1

	def shellSort(self, delay : float):
		gaps = [1]
		k = 2
		while gaps[0] < len(self.array):
			gaps.insert(0, 2 ** k - 1)
			k += 1

		for g in gaps:
			for i in range(g, len(self.array)):
				temp = self.value(i)
				j = i
				while j >= g and self.value(j - g) < temp: # Recall, direct value comparisons must be done backwards
					self.write(j, self.value(j - g), delay)
					j -= g

				self.write(j, temp, delay)
