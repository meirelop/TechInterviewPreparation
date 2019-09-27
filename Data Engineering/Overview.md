# Hadoop 🐘


## Hadoop Common
Hadoop common is the core Java library used for supporting the other Hadoop modules.
HDFS is the backbone of Hadoop — can be thought of as the “cluster storage layer”. As the name suggests data is stored much like a file system in a normal computer — except it is distributed across many physical machines.

## YARN
YARN (Yet another resource manager) is used to manage compute power in a Hadoop cluster. Can be thought of as the “Cluster compute layer”. When you run applications such as “Hadoop MapReduce” or “Spark” on your Hadoop cluster, YARN will make sure they have sufficient resources to do so. An alternative to YARN would be “Apache Mesos”, however, the later attempts to manage/allocate resources to a much wider scope of applications (web servers etc.) and is not strictly part of the Hadoop ecosystem.

## Hadoop Mapreduce
Hadoop MapReduce is an application that performs MapReduce jobs against data stored in HDFS. MapReduce jobs can be written in a number of languages including Java and Python. MapReduce has largely fallen out of favour as Spark is up to 100x faster.
What made Hadoop so ground-breaking was the scalability of HDFS (Hadoop Distributed File System). Even now nothing comes close to the storage capacity of HDFS which max’s out at nearly 100PB

## Hadoop ecosystem

* Tez: Is a drop in replacement for Hadoop MapReduce before both were — for the most part — superseded by Spark. Tez utilized a DAG engine (same technique as Spark) to optimize workflows before processing started. This made Tez much faster than Hadoop MapReduce.
* Pig: Pig is a platform that allows you to write scripts in a language called “Pig Latin” which had a SQL-like syntax. It served as a more intuitive alternative to writing Hadoop MapReduce code in Python or Java. Once written Pig scripts could be translated into MapReduce commands and then run on your Hadoop cluster.


## Spark

Spark manages the processing of massive amounts of data and has largely superseded “Hadoop MapReduce” in the batch data processing field. Spark Core is the central part of Spark and provides all of its general purpose data processing functionality. Spark also has additional libraries for things such as real time data processing (spark streaming) and more.
Spark runs up to 100x faster than Hadoop MapReduce in memory and up to 10x faster on disk. It does this by working with data in memory as much as possible. It also uses a DAG (Directed Acyclic Graph) Engine to optimize workflows. The DAG engine essentially takes the tasks that needs to be completed and works backwards to determine the most optimum way to carry them out.
Spark isn’t strictly part of the Hadoop ecosystem as it can be run independently of a Hadoop cluster. It is however very common for it to be run as part of one.


## Hive 🐝
Hive makes your Hadoop cluster feel like a relational database (in reality it most certainly isn’t). It allows you to write SQL (Specifically HiveQL which has a slightly more limited syntax) queries against data stored in HDFS.
It does this by translating your SQL commands into Hadoop MapReduce/Tez commands (depending on which batch processing application you are using). Said commands are then passed to YARN in order to be executed on the cluster.
Hive is only suitable for OLAP (on-line analytics processing) systems. It is unsuitable for performing real-time transactions as part of an OLTP (on-line transaction processing) system (more on this later!).


## Zookeeper 👀
Without getting into too much detail Zookeeper is essentially a service that runs inside you Hadoop cluster (or any distributed system for that matter — it isn’t tightly coupled to Hadoop) which keeps track of information that must be synchronised across your cluster. Information such as:
* Which node is the master?
* What tasks are assigned to which workers?
* Which workers are currently unavailable?
Zookeeper can be queried by any application running within a Hadoop cluster such as MapReduce, Spark, etc.

## A brief Hadoop operations tangent 🔧
Instead of hiring a team of data infrastructure engineers to build onsite hadoop platforms many companies use a vendor.
Vendors take a number of forms. Some vendors provide cloud hosted services such as Amazon AWS EMR (Elastic Map Reduce) or Microsoft HDInsight. These services take a lot of the complexity out of setting up and managing your own Hadoop cluster.
Other vendors such as Cloudera/Hortonworks provide support/training/consulting to help companies build their own custom hadoop platforms on premises/in the cloud.


# Exporting data from Hadoop into a database 🚛
There is no silver bullet on exporting data from Hadoop to database. You will have to weigh up many considerations including CAP(Consistensy, Availability, Partition Tolerance)
The Hadoop Distributed File System(HDFS) chooses Partition Tolerance and consistency (CP)— three failed data nodes can render a file’s blocks unavailable if you are unlucky.



