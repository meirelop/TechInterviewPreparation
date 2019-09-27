# OLAP vs OLTP

OLTP (On-line Transaction Processing) is involved in the operation of a particular system. OLTP is characterized by a large number of short on-line transactions (INSERT, UPDATE, DELETE). The main emphasis for OLTP systems is put on very fast query processing, maintaining data integrity in multi-access environments and an effectiveness measured by number of transactions per second. In OLTP database there is detailed and current data, and schema used to store transactional databases is the entity model (usually 3NF). It involves Queries accessing individual record. Populated via batch query.

OLAP (On-line Analytical Processing) deals with Historical Data or Archival Data. OLAP is characterized by relatively low volume of transactions. Queries are often very complex and involve aggregations. For OLAP systems a response time is an effectiveness measure. OLAP applications are widely used by Data Mining techniques. In OLAP database there is aggregated, historical data, stored in multi-dimensional schemas (usually star schema). Sometime query need to access large amount of data in Management records like what was the profit of your company in last year.

2 examples scenarios :

* Scenario 1 :

You are building an online store/website, and you want to be able to:
store user data, passwords, previous transactions...
store actual products, their associated price.
You want to be able to find data for a particular user, change it's name... Basically perform INSERT, UPDATE, DELETE operations on a user data. Same with products, etc.

You want to be able to make transactions, possibly involving a user buying a product (that's a relation). Then OLTP is probably a good fit.

* Scenario 2 :

You have an online store/website, and you want to compute things like

the "total money spend for all users"
"what is the most sold product"
This falls into the analytics/business intelligence domain, therefore OLAP is probably more suited.

If you think in terms of "It would be nice to know how/what/how much"..., and that involves all "object" of one or more kind (ex. all the users and most of the products to know the total spent) then OLAP is probably better suited.


It follows that :

- OLTP databases are meant to be used to do many small transactions, and usually serve as a "single source of truth".
- OLAP databases on the other hand are more suited for analytics, data mining, less queries but they are usually bigger (they operate on more data, e.g Hadoop).



# CAP Theorem

CAP Theorem is a concept that a distributed database system can only have 2 of the 3: Consistency, Availability and Partition Tolerance.

![alt CAP triangle](https://raw.githubusercontent.com/meirelop/TechInterviewPreparation/master/Data%20Engineering/cap.png)

## Partition Tolerance

This condition states that the system continues to run, despite the number of messages being delayed by the network between nodes. A system that is partition-tolerant can sustain any amount of network failure that doesn’t result in a failure of the entire network. Data records are sufficiently replicated across combinations of nodes and networks to keep the system up through intermittent outages. When dealing with modern distributed systems, **Partition Tolerance is not an option. It’s a necessity. Hence, we have to trade between Consistency and Availability.**


