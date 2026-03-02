from pyspark.sql import SparkSession
from pyspark.sql.functions import explode_outer, col, from_json, explode
from pyspark.sql.types import StructType, StructField,StringType,IntegerType, ArrayType

spark = SparkSession.builder.getOrCreate()

schema = StructType([StructField("order_id", StringType(), True),
                     StructField("order_date", StringType(), True),
                     StructField("customer",
                                          StructType([
                                              StructField("customer_id", StringType(), True)
                                              ,StructField("customer_name", StringType(), True)
                                              ,StructField("email", StringType(), True)
                                          ]
                                          ),True),
                     StructField("items",ArrayType(
                         StructType([
                            StructField("product_id",StringType(),True)
                            ,StructField("product_name",StringType(),True)
                            ,StructField("quantity",IntegerType(),True)
                            ,StructField("price",IntegerType(),True)
                         ])
                        ), True)
                     ])

df = spark.read.format("json").option("multiline", "true").schema(schema).load(r"C:/Users/krish/OneDrive/Documents/Sapmple_Data/sales.json")

df.printSchema()
# df = df.select(from_json(col("customer"), customer_schema).alias("customer"))

df = df.select(
    col("order_id")
    , col("order_date")
    , col("customer.customer_id")
    , col("customer.customer_name")
    , col("customer.email")
    , explode_outer(col("items")).alias("items")
)

df = df.select(
    col("order_id"), col("order_date"), col("customer_id"), col("customer_name")
    ,col("email"), col("items.product_id"), col("items.product_name"), col("items.quantity")
    , col("items.price")
)

df.show(truncate = False)
