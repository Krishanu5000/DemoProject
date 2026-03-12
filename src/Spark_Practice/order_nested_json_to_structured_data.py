from pyspark.sql import SparkSession
from pyspark.sql.functions import col,explode

spark = SparkSession.builder.getOrCreate()
path = r"C:\Users\krish\IdeaProjects\DemoProject\Data\orders.json"
df = spark.read.format("json").option("multiline", "true").load(path)
df.show(truncate=False)
df.printSchema()

df = df.select(col("customer.id"),col("customer.name"), explode(col("items")).alias("items"),col("order_id"))

df = df.select(col("id"),col("name"),col("items.price"), col("items.product"),col("order_id"))

df.show(truncate= False)