from utils.spark_session import get_spark_session
from extraction.reader import DBReader
import sys

def main():
    print("========================================")
    print("  Spark Job Initializing on OpenShift   ")
    print("========================================")
    
    spark = get_spark_session("OpenShift-Final-Demo")
    
    try:
        reader = DBReader(spark)
        df = reader.read_db()
        
        print("Extraction Result:")
        df.show()
        
        print("SUCCESS: End-to-End Pipeline Verified!")
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        sys.exit(1)
    finally:
        spark.stop()

if __name__ == "__main__":
    main()
