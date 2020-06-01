# Tempus Data Engineer Challenge
The data pipeline fetches data (top highlights in English and/or results from specified top) from [News API](https://newsapi.org),
 transform the data into a tabular structure,
 and store the transformed data on [Amazon S3](https://aws.amazon.com/s3/).
 This data pipeline uses [Apache Airflow](https://airflow.apache.org) to fetch the data daily.

## Quickstart
python 3.7\
Run `make init` to download project dependencies\
Run `make run` with docker running to bring up airflow
 * There should be 2 DAGs named `top_highlights` and `any_topic`


## Directory
    .
    ├── anyTopicDagBag                    # 2nd dag
    │   └── anyTopic_dag.py                          
    ├── config                            # Airflow
    │   └── airflow.cfg  
    ├── dags                    
    │   ├── challenge                     # News Api
    │   │    ├── __init__.py             
    │   │    └── news.py
    │   ├── __init__.py
    │   ├── add_dag_bags.py
    │   └── topHighlight_dag.py               
    ├── docker                    
    │   ├── script               
    │   │    └── entrypoint.sh
    │   ├── Dockerfile              
    │   └── docker-compose.yml               
    ├── Makefile
    ├── README.md
    ├── requirements-setup.txt
    ├── requirements-test.txt
    ├── requirements.txt
    ├── setup.cfg
    └── setup.py


## [News API](https://newsapi.org)
A simple REST API that can be used to retrieve breaking headlines and search for articles. **A free News API account is required to obtain an API key.**

| Route             | Description                                                                                                                |
|-------------------|----------------------------------------------------------------------------------------------------------------------------|
| [/v2/top-headlines](https://newsapi.org/docs/endpoints/top-headlines) | Returns live top and breaking headlines for a country, specific category in a country, single source, or multiple sources. |
| [/v2/sources](https://newsapi.org/docs/endpoints/sources) | Returns the subset of news publishers that top headlines are available from. |


## [Amazon S3](https://aws.amazon.com/s3/)
A simple cloud storage service run by Amazon Web Services (AWS). **An AWS account is needed to use AWS S3. Furthermore, AWS has a [free tier](https://aws.amazon.com/free/) that can be used for this challenge.**

Amazon provides a Python SDK (**[boto](http://boto3.readthedocs.io/en/latest/guide/resources.html)**), that provides an easy to use API for interacting with AWS S3.
