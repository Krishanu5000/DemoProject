from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DecimalType, DoubleType, LongType, IntegerType
from pyspark.sql.functions import col

class RawExtractAndLoad():
    def __init__(self):
        self.spark = SparkSession.builder.getOrCreate()
        self.spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")
        self.customer_source_path = '/FileStore/tables/Customer.xlsx'
        self.product_source_path = '/FileStore/tables/Products.csv'

        self.customer_schema = StructType([
            StructField("Customer_ID", StringType(), True),
            StructField("Customer_Name", StringType(), True),
            StructField("email", StringType(), True),
            StructField("phone", StringType(), True),
            StructField("address", StringType(), True),
            StructField("Segment", StringType(), True),
            StructField("Country", StringType(), True),
            StructField("City", StringType(), True),
            StructField("State", StringType(), True),
            StructField("Postal_Code", StringType(), True),
            StructField("Region", StringType(), True)
        ])

        self.product_schema = StructType([
            StructField("Product_ID", StringType(), True),
            StructField("Category", StringType(), True),
            StructField("Sub_Category", StringType(), True),
            StructField("Product_Name", StringType(), True),
            StructField("State", StringType(), True),
            StructField("Price_per_product", DecimalType(27,6), True)
        ])

    def customer_file_read(self, customer_schema=None, customer_source_path=None):
        if customer_schema is None:
            customer_schema = self.customer_schema
        if customer_source_path is None:
            customer_source_path = self.customer_source_path

        customer = spark.read.format("com.crealytics.spark.excel") \
            .schema(customer_schema) \
            .option("header", "true") \
            .load(customer_source_path)

        return customer

    def customer_raw_data_load(self):
        self.customer_file_read().write.format("delta").mode("append").saveAsTable("raw_customer_data")

    # product = spark.read.format("csv").schema(product_schema).option("header","true").option("quote", "\"").option("escape", "\"").load(product_source_path)

    # product.write.format("delta").mode("append").saveAsTable("raw_product_data")

    # order = spark.read.format("json").option("multiline", "true").option("header","true").load("/FileStore/tables/Orders.json")

    # order_renamed = order.toDF(*[c.strip().replace(" ", "_") for c in order.columns])
    # order_casted = order_renamed \
    #     .withColumn("Price", col("Price").cast(DecimalType(27, 6))) \
    #     .withColumn("Discount", col("Discount").cast(DecimalType(27, 6))) \
    #     .withColumn("Profit", col("Profit").cast(DecimalType(27, 6))) \
    #     .withColumn("Quantity", col("Quantity").cast("int")) \
    #     .withColumn("Row_ID", col("Row_ID").cast("long"))

    # order_casted.write.format("delta").mode("append").saveAsTable("raw_order_data")