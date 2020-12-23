import sys
from pprint import pprint
import re

class Tile:
	def __init__(self, tilemap, id):
		self.id = id
		self.top = tilemap[0]
		self.bottom = tilemap[-1]
		self.left = [s[0] for s in tilemap]
		self.right = [s[-1] for s in tilemap]
	
	def linesupwith(self, other):
		ret = 0
		if self.top == other.top or self.top == other.bottom or self.top[::-1] == other.top or self.top[::-1] == other.bottom:
			ret += 1
		if self.bottom == other.top or self.bottom == other.bottom or self.bottom[::-1] == other.top or self.bottom[::-1] == other.bottom:
			ret += 1
		if self.left == other.left or self.left == other.right or self.left[::-1] == other.left or self.left[::-1] == other.right:
			ret += 1
		if self.right == other.left or self.right == other.right or self.right[::-1] == other.left or self.right[::-1] == other.right:
			ret +=  1
		return ret

if __name__=="__main__":
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	else:
		filename = "input.txt"

	with open(filename, "rt") as infile:
		text = infile.read().split("\n\n")[:-1]
	
	tiles = [Tile(tile.split(":")[1].split(), int(tile.split(":")[0].split()[1])) for tile in text]
	tile_length = len(text[0].split(":")[1].split()[0])
	tile_height = len(text[0].split(":")[1].split())
	
	print(len(tiles))
	print(tile_length)
	print(tile_height)
	
	##### Part 1: rotate, flip and rearrange the tiles in a square pattern
	##### so that their edges line up. Output the product of the corner IDs
	
	## count, for each tile, all the tiles it lines up with
	counts = {}
	counts_set = set()
	for t1 in tiles:
		counts_t1 = 0
		for t2 in tiles:
			counts_t1 += t1.linesupwith(t2)
		counts_set.add(counts_t1)
		if counts_t1 == 5:
			print(t1.id)
	
	print(counts_set)