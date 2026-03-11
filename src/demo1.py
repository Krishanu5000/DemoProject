import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql.functions import col, max, row_number
# df = pd.read_csv('C:/Users/krish/IdeaProjects/DemoProject/src/banana_quality_dataset.csv')
#
# print(df)

spark = SparkSession.builder.getOrCreate()

df = spark.read.format("csv")\
    .option("header", "true").load("C:/Users/krish/IdeaProjects/DemoProject/src/banana_quality_dataset.csv")
print(df.count())
#df.filter(col("sample_id") <= 50).show(50, truncate=False)

#max = df.select(max(col("quality_score"))).collect()

w = Window.orderBy(col("quality_score").desc())


df.withColumn("rnum", row_number().over(w)).filter(col("rnum") == 1).show(truncate=False)

# employee
# emp_id dept_id salary emp_name
# 1      10      100    krishanu
# 2
#
# dept
# dept_id dept_name

# with temp as (select e.emp_name,row_number() over(partition by d.dept_name order by e.salary desc) as rnum
# employee e join dept d
# on e.dept_id = d.dept_id)
# select * from temp where rnum<=3
