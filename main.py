import sys
import knn_learner as kl
from scipy.io import arff

def main():
	if len(sys.argv) == 4:
		train_data, train_meta = arff.loadarff(sys.argv[1])
		test_data, test_meta   = arff.loadarff(sys.argv[2])
		try:
			labels = train_meta['class'][1]
		except KeyError:
			labels = None
		mode = 'r' if labels == None else 'c'
		k = int(sys.argv[3])
		print 'k value : ' + str(k)
		err = kl.knn_learn(train_data, test_data, k, labels, mode, True)

	elif len(sys.argv) == 6:
		train_data, train_meta = arff.loadarff(sys.argv[1])
		test_data, test_meta   = arff.loadarff(sys.argv[2])
		try:
			labels = train_meta['class'][1]
		except KeyError:
			labels = None
		mode = 'r' if labels == None else 'c'
		kvalues = [int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])]
		best_k = -1
		lowest_err = float('inf')
		for k in kvalues:
			err = 0.0
			for i in range(len(train_data)):
				train_copy = list(train_data)
				inst = train_copy.pop(i)
				err += kl.knn_learn(train_copy, [inst], k, labels, mode, False)
			if err < lowest_err:
				lowest_err = err
				best_k = k
			if mode == 'r':
				print('Mean absolute error for k = ' + str(k) + ' : ' 
					+ '{0:.16f}'.format(err / len(train_data)))
			else:
				print('Number of incorrectly classified instances for k = ' 
					+ str(k) + ' : ' + str(int(err)))
		print 'Best k value : ' + str(best_k)
		kl.knn_learn(train_data, test_data, best_k, labels, mode, True)
	
	else:
		print 'incorrect usage'

if __name__ == '__main__':
	main()
