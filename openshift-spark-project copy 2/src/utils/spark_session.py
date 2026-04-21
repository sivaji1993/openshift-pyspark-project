from pyspark.sql import SparkSession
from pyspark import SparkConf

def get_spark_session(app_name):
    conf = SparkConf()
    # Disable event logging to prevent crashes in the Sandbox environment
    conf.set("spark.eventLog.enabled", "false")
    conf.set("spark.ui.enabled", "false")
    conf.set("spark.hadoop.fs.defaultFS", "file:///")
    
    return SparkSession.builder \
        .appName(app_name) \
        .config(conf=conf) \
        .getOrCreate()
