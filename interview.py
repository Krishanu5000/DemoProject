from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col, when, from_json, array, substring, instr, expr
from pyspark.sql.types import StructType, StructField, StringType, ArrayType

import os

print(os.path.exists(
    r"C:\Users\krish\OneDrive\Documents\Sapmple_Data\interview.json"
))

spark = SparkSession.builder.getOrCreate()

df = spark.read.format("json").option("multiline", "true").load(r"C:\Users\krish\OneDrive\Documents\Sapmple_Data\interview.json")

df.show(truncate=False)

coupon_struct = StructType([
    StructField("April", StringType(), True),
    StructField("May", StringType(), True)
])

coupon_array = ArrayType(coupon_struct)

df2 = df.withColumn(
    "Coupons",
    when(
        col("Coupons").startswith("["),
        from_json(col("Coupons"), coupon_array)
    ).otherwise(
        array(
            from_json(col("Coupons"), coupon_struct)
        )
    )
)

df2.printSchema()

final_df = df2.select(
    explode("Coupons").alias("Coupon")
)

final_df.show(truncate=False)


final_df = final_df.select(col("Coupon.April"), col("Coupon.May"))

final_df.show(truncate=False)

final_df = final_df\
    .withColumn("April", expr("substring(April, 1, instr(April,'%')-1)"))\
    .withColumn("May", expr("substring(May, 1, instr(May,'%')-1)"))

final_df.show(truncate=False)

