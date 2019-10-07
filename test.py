

import findspark
print(findspark.init("/usr/local/spark/"))
print(findspark.find())








from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster('local[*]').setAppName('word_count')
sc = SparkContext(conf=conf)
d = ['a b c d', 'b c d e', 'c d e f']
# d_rdd = sc.parallelize(d)
# rdd_res = d_rdd.flatMap(lambda x: x.split(' ')).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
# print(rdd_res)
# print(rdd_res.collect())

rdd = sc.textFile("file.txt")
# print(rdd.take(1))
print(rdd.count())
# print(rdd)
