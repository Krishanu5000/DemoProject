from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, avg, udf
from pyspark.sql.types import BooleanType
import re

spark = SparkSession.builder.getOrCreate()

data = [(10, [100, 200, 300]), (20, [400, 500, 600]), (30, [700, 800, 900])]
schema = ["cust_id", "purchase_items"]

df = spark.createDataFrame(data, schema)

df.show(truncate=False)
df.printSchema()

df = df \
    .select(col("cust_id"), explode(col("purchase_items")).alias("purchase_items")) \
    .groupby(col("cust_id")).agg(avg(col("purchase_items")).alias("avg_purchase_items"))

df.show()


def null_check(value):
    if value is None:
        return True
    else:
        return False


def blank_check(value):
    if str(value).strip() == "":
        return True
    else:
        return False


def alpha_numeric_check(value):
    if re.search(r'[a-zA-Z]', str(value)):
        return True
    else:
        return False


null_check = udf(null_check, BooleanType())
blank_check = udf(blank_check, BooleanType())
alpha_numeric_check = udf(alpha_numeric_check, BooleanType())

for i in df.columns:
    df = df \
        .withColumn(i + '_null_check', null_check(i)) \
        .withColumn(i + '_blank_check', blank_check(i))
    if i == 'avg_purchase_items':
        df = df.withColumn(i + 'alph_numeric_check', alpha_numeric_check(i))

df.show()
