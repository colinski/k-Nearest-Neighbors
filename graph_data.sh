for k in 1 2 3 5 10
do
	echo "k = " $k
    . run.sh wine $k >> tmp.txt
	tail -n 2 tmp.txt >> wine_graph.txt
	rm -f tmp.txt	
done

