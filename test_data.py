import pyspark
import pandas as pd

from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, pandas_udf,PandasUDFType
from pyspark.sql import DataFrame
from pyspark import SparkContext
import os

conf = SparkConf()\
    .setAppName("weblogs processing")\
    .set("spark.executor.memory", "8g")
spark = SparkSession.builder.config(conf=conf).getOrCreate()

df = spark.SparkContext.parrallelize([("Hello","World","project"),("chaussure","ballon","fourchette"),("Dylane","Alexis","Guillaume")])
df.show()
