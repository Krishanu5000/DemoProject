from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
data = [(10, 500)]
schema = ["cust_id", "amount"]

df1 = spark.createDataFrame(data, schema)
df1.registerTempTable("SRC")

data = [(10 , 600)]
schema = ["cust_id", "amount"]

df2 = spark.createDataFrame(data, schema)

df2.registerTempTable("TRG")

spark.sql("""select * from TRG""")

spark.sql("""MERGE INTO TRG
USING SRC
ON SRC.cust_id = TRG.cust_id

WHEN MATCHED THEN
UPDATE SET
TRG.cust_id = SRC.cust_id

WHEN NOT MATCHED THEN
INSERT (cust_id)
VALUES (SRC.cust_id)""")

spark.sql("""select * from TRG""")


