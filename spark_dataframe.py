# import findspark
# print(findspark.init("/usr/local/spark-2.4.0-bin-hadoop2.7"))
# print(findspark.find())


from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
l = [('Alice', 1)]

conf = SparkConf().setAppName('Elephas_App').setMaster('local[*]')
sc = SparkContext(conf=conf)
sess = SparkSession(sc)
print(sess.createDataFrame(l).collect())



data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)
print(distData)
a=distData.reduce(lambda a, b: a + b)
print(a)


d = [{'name': 'Neha', 'age': 1}]
distData22 = sc.parallelize(d)
df = sess.createDataFrame(distData22)
# print(df)
df.show()

# range_seq=sess.range(1, 7, 2).collect()
# print(range_seq)

