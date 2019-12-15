from google.cloud import storage
import argparse
import pyspark
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.ml.feature import *
from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.regression import GBTRegressionModel

# Parse customized input
parser = argparse.ArgumentParser(description='Process inputs for prediction')
parser.add_argument('--age', type=str, help='Age Group: 0 to 17, 18 to 29, 30 to 49, 50 to 69, 70 or older')
parser.add_argument('--zipcode', type=str, help='Zip Code: 100 to 149 and Out of State (OOS)')
parser.add_argument('--gender', type=str, help='Gender: M, F')
parser.add_argument('--race', type=str, help='Race: White, Black/African American/Other Race/Multi-racial')
parser.add_argument('--toa', type=str, help='Type of Admission: Emergency/Elective/Newborn/Not Available/Trauma/Urgent')
args = parser.parse_args()

# Create spark driver
spark = SparkSession.builder.master("local[*]").getOrCreate()

# Schema for 5 Fields customized test input
schema = StructType([StructField('Age Group',StringType(),True),
                     StructField('Zip Code - 3 digits',StringType(),True),
                     StructField('Gender',StringType(),True),
                     StructField('Race',StringType(),True),
                     StructField('Type of Admission',StringType(),True)])

# customized input data for testing
testDataWithTarget = spark.createDataFrame([Row(args.age, args.zipcode, args.gender, args.race, args.toa)], schema)

# reload pipelineModel
loadedModel = PipelineModel.load("gs://final-project-1/pipelineModel")
testDataWithTargetDF = loadedModel.transform(testDataWithTarget)

# reload pySpark Model
testModel = GBTRegressionModel.load("gs://final-project-1/pySparkModel")

predictions = testModel.transform(testDataWithTargetDF)
print (predictions.select('prediction').show())

storage_client = storage.Client()
bucket = storage_client.get_bucket('final-project-1')
blob = bucket.blob('output.txt')
blob.upload_from_string(str(predictions.select('prediction').collect()[0].__getitem__("prediction")))
