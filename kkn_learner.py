import math, sys
from arff_parser import ArffParser
from feature import Feature
from sorted_array import SortedArray

def main():
	(train_instances, features, labels) = ArffParser(sys.argv[1]).parse()
	test_instances = ArffParser(sys.argv[2]).parse()[0]
	k = int(sys.argv[3])
	mode = 'r' if labels == [] else 'c'
	err = 0.0
	for i in range(0, len(test_instances)):
		q = test_instances[i]
		neighbors = find_nearest_neighbors(q, k, train_instances)
		if mode == 'r':
			avg = 0.0
			for n in neighbors:
				avg += get_label(n[0], mode)
			avg /= len(neighbors)
			err += abs(avg - get_label(q, mode))
			print('Predicted value : ' + '{0:.6f}'.format(avg)
				+ '\tActual value : '  + '{0:.6f}'.format(get_label(q, mode)))
		else:
			guess = predict_class(neighbors, q)


	if mode == 'r':
		print 'Mean absolute error : ' + '{0:.16f}'.format((err / len(test_instances)))
		print 'Total number of instances : ' + str(len(test_instances))

def find_nearest_neighbors(q, k, train_instances):
	neighbors = SortedArray(k)
	for x in train_instances:
		dist = calc_dist(q, x)
		neighbors.add((x, dist))
	return neighbors.array

def calc_dist(v, w):
	dist = 0
	for i in range(0, len(v) - 1):
		dist += (float(v[i]) - float(w[i])) ** 2.0
	return math.sqrt(dist)

def get_label(n, mode):
	val = n[len(n) - 1]
	return float(val) if mode == 'r' else str(val)

def predict_class(neighbors, q):
	neighbor_sets = {}
	for n in neighbors:
		label = get_label(n[0], 'c')
		if not neighbor_sets.has_key(label):
			neighbor_sets[label] = []
		neighbor_sets[label].append(n)

	print type(sets)
	print type(sorted(sets, key = lambda k : len(sets[k])))
	print '-------'
	#for key in sorted_sets:
	#	pass
	#	print key + ' ' + str(len(sorted_sets[key]))
	print '\n-------'


if __name__ == '__main__':
	main()