import sys
from arff_parser import ArffParser
import knn_learner as kl

def main():
	if len(sys.argv) == 4:
		(train_instances, features, labels) = ArffParser(sys.argv[1]).parse()
		test_instances = ArffParser(sys.argv[2]).parse()[0]
		k = int(sys.argv[3])
		err = kl.knn_learn(train_instances, test_instances, k, features, labels, True)
		print err

	elif len(sys.argv) == 6:
		(train_instances, features, labels) = ArffParser(sys.argv[1]).parse()
		test_instances = ArffParser(sys.argv[2]).parse()[0]
		kvalues = [int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])]
		for k in kvalues:
			err = 0.0
			for i in range(len(train_instances)):
				train_copy = list(train_instances)
				inst = train_copy.pop(i)
				err += kl.knn_learn(train_copy, [inst], k, features, labels, False)
			print 'err for k = ' + str(k) + ' is ' + str(err / len(train_instances))
	else:
		print 'incorrect usage'

if __name__ == '__main__':
	main()
