from pyspark import SparkContext
sc = SparkContext("local", "ADA")

data = sc.parallelize(range(1000))
print(data.sum())

print('THE END')