perf record -F 9999 -g -o perf.data python3 5.excercise.py 
perf report --stdio -n -g