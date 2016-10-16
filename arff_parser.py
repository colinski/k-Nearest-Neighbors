from feature import Feature
class ArffParser:
	def __init__(self, filename):
		self.filename = filename
		self.file = open(filename)

	def parse(self):
		instances = []
		features  = []
		reached_data = False
		index = 0
		for line in self.file:
			line = line.strip()
			if '@data' in line:
				reached_data = True
				continue
			if reached_data:
				instances.append(line.split(','))
			elif '@attr' in line:
				if '{' not in line:	#numeric
					tokens = line.split(' ')
					features.append(Feature(tokens[1].replace("'", ''), 'numeric', index))
					index += 1
				else:
					tokens = line.split('{')
					name_tokens = tokens[0].split(' ');
					name = name_tokens[1].replace("'", '');
					cat_tokens = tokens[1].split(',');
					f = Feature(name, 'nominal', index)
					for token in cat_tokens:
						token = token.replace(',', '').replace('}', '')
						if token != '':
							f.values.append(token)
					features.append(f)
					index += 1
		labels = features.pop()
		self.file.close()
		if labels.name == 'response':
			return (instances, features, [])
		else:
			return (instances, features, labels.values)
