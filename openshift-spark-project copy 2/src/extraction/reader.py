import os
from pyspark.sql import SparkSession

class DBReader:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def read_db(self):
        # Read credentials injected from OpenShift Secrets
        user = os.getenv("DB_USER")
        pwd = os.getenv("DB_PASS")
        
        if user:
            print(f"SUCCESS: Retrieved credentials from Vault-Sync Secret. User: {user}")
        else:
            print("NOTICE: No credentials found in environment. Using Mock Data.")

        schema = ["user_id", "user_name", "role_name", "department", "access_level"]
        data = [
            ("USR1001", "v_sinha", "Data_Engineer_Sr", "Data_Platform", "Admin"),
            ("USR1002", "a_smith", "Security_Analyst", "Cyber_Security", "Read_Only"),
            ("USR1003", "m_kumar", "DevOps_Lead", "Infrastructure", "Admin"),
            ("USR1004", "s_chen", "Data_Scientist", "Analytics", "Contributor"),
            ("USR1005", "j_doe", "Compliance_Officer", "Legal", "Auditor"),
            ("USR1006", "r_jones", "Cloud_Architect", "Infrastructure", "Admin"),
            ("USR1007", "p_sharma", "ML_Engineer", "AI_Labs", "Contributor"),
            ("USR1008", "l_white", "DBA_Specialist", "Data_Platform", "Admin"),
            ("USR1009", "k_patel", "Network_Engineer", "Connectivity", "Read_Only"),
            ("USR1010", "h_tanaka", "Product_Owner", "Digital_Exp", "Auditor")
        ]
        
        return self.spark.createDataFrame(data, schema)