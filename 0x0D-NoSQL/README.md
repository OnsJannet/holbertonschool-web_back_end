# 0x0D. NoSQL

## Resources:
	https://docs.mongodb.com/manual/reference/command/listDatabases/#mongodb-dbcommand-dbcmd.listDatabases
	https://docs.mongodb.com/manual/reference/method/
	https://docs.mongodb.com/manual/aggregation/
	https://riak.com/resources/nosql-databases/
	https://www.youtube.com/watch?v=qUV2j3XBRHc
	https://www.youtube.com/watch?v=CB9G5Dvv-EE
	https://realpython.com/introduction-to-mongodb-and-python/

## General: 
in this project we will learn the following:

    What NoSQL means
    What is difference between SQL and NoSQL
    What is ACID
    What is a document storage
    What are NoSQL types
    What are benefits of a NoSQL database
    How to query information from a NoSQL database
    How to insert/update/delete information from a NoSQL database
    How to use MongoDB


## Install MongoDB 4.2 in Ubuntu 18.04

Official installation guide

	$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
	$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
	$ sudo apt-get update
	$ sudo apt-get install -y mongodb-org
	...
	$  sudo service mongod status
	mongod start/running, process 3627
	$ mongo --version
	MongoDB shell version v4.2.8
	git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
	OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
	allocator: tcmalloc
	modules: none
	build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
	$  
	$ pip3 install pymongo
	$ python3
	>>> import pymongo
	>>> pymongo.__version__
	'3.10.1'


