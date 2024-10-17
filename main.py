from extract import extract
from transform import transform
from load import load
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('ETLPipeline').config("spark.jars", "C:\spark\jars\postgresql-42.7.3.jar").getOrCreate()

sql = "select * from superstore"
df = extract(spark=spark, sql=sql)
print(df)
orders_df, rfm_df = transform(df)
# print(orders_df.show(5))
# print(rfm_df.show(5))

load(df=orders_df, tabel_name="superstore")
load(df=rfm_df, tabel_name="rfm")