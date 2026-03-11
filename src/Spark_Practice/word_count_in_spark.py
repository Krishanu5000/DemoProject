import re
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.format("csv").load("C:/Users/krish/IdeaProjects/DemoProject/Data/sample3.txt")

df.show(truncate=False)

df.printSchema()

l = list(df.rdd.flatMap(lambda x: (x._c0.split(" "))).map(lambda x: (re.sub(r'[^a-zA-Z0-9]', '', x), 1)).reduceByKey(
    lambda x, y: x + y).collect())

print(l)
