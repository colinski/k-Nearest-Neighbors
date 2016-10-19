import math, sys
from feature import Feature
from sorted_array import SortedArray

def knn_learn(train_instances, test_instances, k, features, labels, doPrint):
	mode = 'r' if labels == [] else 'c'
	err = 0.0
	for i in range(0, len(test_instances)):
		q = test_instances[i]
		neighbors = find_nearest_neighbors(q, k, train_instances)

		for n in neighbors:
			print get_label(n[0], mode)

		if mode == 'r':
			avg = 0.0
			for n in neighbors:
				avg += get_label(n[0], mode)
			avg /= len(neighbors)
			err += abs(avg - get_label(q, mode))
			if doPrint:
				print('Predicted value : ' + '{0:.6f}'.format(avg)
					+ '\tActual value : '  + '{0:.6f}'.format(get_label(q, mode)))
		else:
			guess = predict_class(neighbors, q, labels)
			if guess != get_label(q, mode):
				err += 1
			if doPrint:
				print 'Predicted class : ' + guess + '\t Actual class : ' + get_label(q, mode)

	if mode == 'r':
		if doPrint:
			print 'Mean absolute error : ' + '{0:.16f}'.format((err / len(test_instances)))
			print 'Total number of instances : ' + str(len(test_instances))
		return err / len(test_instances)
	else:
		if doPrint:
			print 'err is ' + str(err)
			print 'got ' + str(len(test_instances) - err) + ' right'
			print 'total ' + str(len(test_instances))
		return err

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

def predict_class(neighbors, q, labels):
	neighbor_sets = {}
	for n in neighbors:
		label = get_label(n[0], 'c')
		if not neighbor_sets.has_key(label):
			neighbor_sets[label] = []
		neighbor_sets[label].append(n)

	best = 0
	for key in neighbor_sets:
		if len(neighbor_sets[key]) > best:
			best = len(neighbor_sets[key])
	
	for key in neighbor_sets:
		if len(neighbor_sets[key]) != best:
			del neighbor_sets[key]

	best_index = float('inf')
	best_label = ''
	for key in neighbor_sets:
		index = label_to_index(key, labels)
		if index < best_index:
			best_index = index
			best_label = key
	return best_label

	

'''
	for key in neighbor_sets:
	if len(neighbor_sets.keys()) == 1:
		#print 'returning because size is 1'

		return get_label(neighbor_sets[0][0], 'c')


	best_index = float('inf')
	best_label = ''
	for n in best_neighbors:
		index = label_to_index(n[0], labels)
		if index < best_index:
			best_index = index
			best_label = get_label(n[0], 'c')
	return best_label


	best_neighbors.sort(key = lambda x : x[1])
	best_dist = float(best_neighbors[0][1])
	closest_neighbors = []
	for n in best_neighbors:
		if n[1] == best_dist:
			closest_neighbors.append(n)

	best_index = 10000
	best_label = ''
	for n in closest_neighbors:
		index = label_to_index(n[0], labels)
		if index < best_index:
			best_index = index
			best_label = get_label(n[0], 'c')
	#closest_neighbors.sort(key = lambda n : label_to_index(n[0], features))
	return best_label
'''


def label_to_index(l, labels):
	for i in range(0, len(labels)):
		if labels[i] == l:
			return i


	#if get_label(best_neighbors[0][0], 'c') != get_label(best_neighbors[1][0], 'c') and\
			#		best_neighbors[0][1] == best_neighbors[1][1]:
			#	return get_label(q, 'c')
	#else:
	#	return get_label(best_neighbors[0][0], 'c')
	#check class and dist of firs two
	#otherwise return

	#print type(sets)
	#print type(sorted(sets, key = lambda k : len(sets[k])))
	#print '-------'
	#if len(best_sets) > 1:
		#	print best_sets
	#for key in sorted_sets:
	#	pass
	#	print key + ' ' + str(len(sorted_sets[key]))
	#prinot '\n-------'