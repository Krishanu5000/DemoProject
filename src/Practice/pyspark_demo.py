from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

l = [('krishanu'),]
schema = ['name']

df = spark.createDataFrame([l,schema])

df.show()