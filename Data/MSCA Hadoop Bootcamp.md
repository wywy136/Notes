# MSCA Hadoop Bootcamp

## Hadoop

Two major components

- HDFS
- MapReduce

Hadoop related tools

- Hive
- HBase
- Pig - data processing language built on top of HDFS and Mapreduce
- Spark

## HDFS

FIle -> blocks 128M

Blocks are spread across the cluster

The calculations are done on DataNodes

`-put` copy the file from linux file system into HDFS 

`hdfs dfs -ls -h` show the size of files in a more readable way

`-setrep` change the replication num of file

`-get` get the file from HDFS to linux filesystem

## MapReduce

Map: convert each record into (key, value) pairs

- Done in parallel

Reduce: apply reduce operation to resulting set of pairs

- Apply local reduce between local map and global reduce

Streaming: An interface to any language

## Hive

Run a hive script

```
nohup hive -f HIVESCRIPT > OUTFILE &
yarn application -list
```

## HBase

`list` command shows all the table in HBase

`describe TABLE`  show the metadata of the table

`alter <TABLE> NAME=> '<CFNAME>, VERSIONS => 5'`  set the version of a column family of the table

- can have up to 5 versions

`scan TABLENAME, (VERSIONS => 2)` show 2 versions of the table

