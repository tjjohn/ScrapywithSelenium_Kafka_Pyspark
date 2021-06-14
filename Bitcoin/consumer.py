from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import time

kafka_topic_name = "coin"
kafka_bootstrap_servers = 'localhost:9092'
if __name__ == "__main__":
    print("Welcome to DataMaking !!!")
    print("Stream Data Processing Application Started ...")
    print(time.strftime("%Y-%m-%d %H:%M:%S"))

    spark = SparkSession \
        .builder \
        .appName("PySpark Structured Streaming with Kafka and Message Format as JSON") \
        .master("local[*]") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    # Construct a streaming DataFrame that reads from test-topic
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
        .option("subscribe", kafka_topic_name) \
        .load()
    df.selectExpr("CAST(key AS varchar)", "CAST(value AS varchar)")
    print("Printing Schema of orders_df: ")
    df.printSchema()

    # Write final result into console for debugging purpose
    orders_agg_write_stream = df\
        .writeStream \
        .trigger(processingTime='5 seconds') \
        .outputMode("update") \
        .option("truncate", "false") \
        .format("console") \
        .start()

    orders_agg_write_stream.awaitTermination()

    print("Stream Data Processing Application Completed.")