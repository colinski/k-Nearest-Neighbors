import sys, copy
from arff_parser import ArffParser
import knn_learner as kl

def main():
	if len(sys.argv) == 4:
		(train_instances, features, labels) = ArffParser(sys.argv[1]).parse()
		test_instances = ArffParser(sys.argv[2]).parse()[0]
		k = int(sys.argv[3])
		err = kl.knn_learn(train_instances, test_instances, k, labels, True)
		print err

	elif len(sys.argv) == 6:
		(train_instances, features, labels) = ArffParser(sys.argv[1]).parse()
		print labels
		test_instances = ArffParser(sys.argv[2]).parse()[0]
		kvalues = [int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])]
		for k in kvalues:
			err = 0.0
			for i in range(len(train_instances)):
				train_copy = []
				inst = None
				for j in range(len(train_instances)):
					if j != i:
						train_copy.append(train_instances[j])
					else:
						inst = train_instances[j]
				#train_copy = copy.deepcopy(train_instances)
				#inst = train_copy.pop(i)
				err += kl.knn_learn(train_copy, [inst], k, labels, False)
			print 'err for k = ' + str(k) + ' is ' + str(err)
	else:
		print 'incorrect usage'

if __name__ == '__main__':
	main()
