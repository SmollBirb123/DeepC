import math, random, scipy.special

class net:
	def __init__(self, *layer_depth): # *layer_depth arbitrary position arg (tuple)
		self.web = [] 
		for x in range(len(layer_depth)):  # loop for layer
			self.web.append([])
			for y in range(layer_depth[x]):    # loop for node within layers
				self.web[x].append({'b' : 0, 'w' : [], 'v' : 0, 'c' : 0})
				if x == 0: continue
				for _y in range(len(self.web[x - 1])):
					self.web[x][y]['w'].append(round(random.uniform(-2, 2), 7))
					
	def forwardProp(self, *inputs):
		for y in range(len(self.web[0])):
			self.web[0][y]['v'] = scipy.special.expit(inputs[y] + self.web[0][y]['b'])
			pass
		for x in range(len(self.web)):
			if x == 0: continue
			for y in range(len(self.web[x])):
				self.web[x][y]['v'] = self.web[x][y]['b']
				for _y in range(len(self.web[x-1])):
					self.web[x][y]['v'] += self.web[x-1][_y]['v'] * self.web[x][y]['w'][_y]
				self.web[x][y]['v'] = 1 / 1 + math.exp(-self.web[x][y]['v'])
		out = []
		for y in range(len(self.web[-1])):
			out.append(self.web[-1][y]['v'])
		return out

	def printWeb(self):
		for layer in self.web: 
			for node in layer: print(node, end = "\n\n")
			print("\n\n")