# Spark & PySpark Dataframe

## Basis

**Spark Master** coordinates workers and overall execution of tasks. Splits a Spark application into tasks and schedules them to run on executors

**Workers** execute one or more tasks in parallel on different partitions of the dataset

A **spark job** is created when there is an action on an RDD

- Within the job, there could be multiple **stages**, depending on whether or not we need to perform a wide transformation (shuffles)
- In each stage there can be one or multiple transformations, mapped to **tasks** in each executor.

RDD Transformation: operations (such as map, filter, join, union, and so on) that are performed on an RDD that yield a new RDD containing the result.

RDD Actions: Operations (such as reduce, count, first, and so on) that return a value after running a computation on an RDD.

## Dataframe & SQL

### SQL in Spark

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.enableHiveSupport().appName('ReadWriteData').getOrCreate()
spark.sql(...)
```

### Read from Hive table and build dataframe

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.enableHiveSupport().appName('ReadWriteData').getOrCreate()
df = spark.table(<table_name>)
```

https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.SparkSession.html#

