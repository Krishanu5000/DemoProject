import os
from pyspark.sql import SparkSession

# Ensure Hadoop path visible to Python
os.environ["HADOOP_HOME"] = "C:\\hadoop"
os.environ["PATH"] += ";C:\\hadoop\\bin"


spark = SparkSession.builder \
    .appName("HiveExample") \
    .config("spark.sql.warehouse.dir", "C:/spark-warehouse") \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .config("spark.hadoop.hadoop.native.lib", "false") \
    .enableHiveSupport() \
    .getOrCreate()

data = [(10, 500)]
schema = ["cust_id", "amount"]

df1 = spark.createDataFrame(data, schema)
# df1.registerTempTable("SRC")
df1.write.mode("append").saveAsTable("SRC")

# data = [(10, 600)]
# schema = ["cust_id", "amount"]
#
# df2 = spark.createDataFrame(data, schema)
#
# df2.registerTempTable("TRG")
#
# spark.sql("""select * from TRG""")
#
spark.sql("""MERGE INTO TRG
USING SRC
ON SRC.cust_id = TRG.cust_id

WHEN MATCHED THEN
UPDATE SET
TRG.cust_id = SRC.cust_id

WHEN NOT MATCHED THEN
INSERT (cust_id)
VALUES (SRC.cust_id)""")
#
# spark.sql("""select * from TRG""")
