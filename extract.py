from setup import *

def extract(spark,sql):
    try : 
        df = spark.read.format('jdbc').options(
            driver = 'org.postgresql.Driver',
            user = user_id,
            password = pwd,
            url = src_url,
            query = sql
        ).option('inferSchema','true').option('header','true').load()

        return df
    except Exception as e :
        print("data extract error : ", str(e))

if __name__ == "__main__":
    import pyspark
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder.appName('ETLPipeline').config("spark.jars", "C:\spark\jars\postgresql-42.7.3.jar").getOrCreate()
    sql = "select * from superstore"
    df = extract(spark=spark, sql=sql)
    # print(df)
    print(df.show(5))
