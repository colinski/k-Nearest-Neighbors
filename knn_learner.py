import sys, math
from sorted_array import SortedArray

def knn_learn(train_data, test_data, k, labels, mode, doPrint):
	err = 0.0
	i = 0
	for q in test_data:
		neighbors = find_nearest_neighbors(q, k, train_data)
		if mode == 'r':
			avg = 0.0
			for n in neighbors:
				avg += get_label(n[0], mode)
			avg /= float(len(neighbors))
			err += abs(avg - get_label(q, mode))
			if doPrint:
				print('Predicted value : ' + '{0:.6f}'.format(avg)
					+ '\tActual value : '  + '{0:.6f}'.format(get_label(q, mode)))
		else:
			guess = predict_class(neighbors, labels)
			if guess != get_label(q, mode):
				err += 1
			if doPrint:
				print 'Predicted class : ' + guess + '\tActual class : ' + get_label(q, mode)
	
	if mode == 'r':
		if doPrint:
			print('Mean absolute error : ' + '{0:.16f}'.format((err / len(test_data))) 
				+ '\nTotal number of instances : ' + str(len(test_data)))
		return err / len(test_data)
	else:
		if doPrint:
			num_correct = int(len(test_data) - err)
			print('Number of correctly classified instances : ' + str(num_correct)
				+ '\nTotal number of instances : ' + str(len(test_data)) 
				+ '\nAccuracy : ' + '{0:.16f}'.format((float(num_correct) / len(test_data))))
		return err

def find_nearest_neighbors(q, k, train_data):
	neighbors = SortedArray(k)
	for x in train_data:
		dist = calc_dist(q, x)
		neighbors.add((x, dist))
	return neighbors.array

def calc_dist(v, w):
	dist = 0
	for i in range(len(v) - 1):
		dist += (float(v[i]) - float(w[i])) ** 2.0
	return math.sqrt(dist)

def predict_class(neighbors, labels):
	neighbor_sets = {}
	for l in labels:
		neighbor_sets[l] = 0
	
	for n in neighbors:
		label = get_label(n[0], 'c')
		neighbor_sets[label] += 1

	best = 0
	for key in neighbor_sets:
		if neighbor_sets[key] > best:
			best = neighbor_sets[key]
	
	best_index = float('inf')
	best_label = ''
	for key in neighbor_sets.keys():
		if neighbor_sets[key] == best:
			index = label_to_index(key, labels)
			if index < best_index:
				best_index = index
				best_label = key
	return best_label

def get_label(n, mode):
	val = n[len(n) - 1]
	return float(val) if mode == 'r' else str(val)

def label_to_index(l, labels):
	for i in range(len(labels)):
		if labels[i] == l:
			return i