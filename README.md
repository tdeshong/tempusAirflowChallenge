# Tempus Data Engineer Challenge
The data pipeline fetches data from [News API](https://newsapi.org),
 transform the data into a tabular structure,
 and store the transformed data on [Amazon S3](https://aws.amazon.com/s3/).
 This data pipeline uses Airflow [Apache Airflow](https://airflow.apache.org) to fetch the data daily.

## Quickstart
python 3.7   docker ------\
Run `make init` to download project dependencies\
Run `make run` with docker running to bring up airflow\
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


## Requirements
- [ ] Use Airflow to construct a new data pipeline (DAG) named 'tempus_challenge_dag'.
- [ ] Data pipeline must be scheduled to run once a day.
- [ ] Data pipeline will:
  - [ ] Retrieve all English news sources.
  - [ ] For each news source, retrieve the top headlines.
    - [ ] Top headlines must be flattened into a CSV file. CSV Filename: `<pipeline_execution_date>_top_headlines.csv`
    - [ ] Result CSV must be uploaded to the following s3 location `<s3_bucket>/<source_name>`
- [ ] The solution must contain at least one test for your headline transformation.
- [ ] The solution must be start-able via `make run`.
- [ ] The solution must be pep-8 compliant.
- [ ] Bonus: Build a separate pipeline that uses the following keywords instead of English news sources: Tempus Labs, Eric Lefkofsky, Cancer, Immunotherapy
- [ ] Bonus: Write an integration test for any of the external services your solution connects to.


## Rules of engagement
* We suggest that you establish a four hour timebox to complete the challenge.
* The solution must perform a Python transformation of the data;
 feel free to add any open-source libraries you wish and add additional output files.
* Please document changes required to make the solution resilient to
 failure by taking the following actions:
  * add developer-friendly requirements to functions
  * add comments in the main function that list failures that the solution should
  be designed to handle
* Please run `make clean` and deliver your Python code via repo or zip ahead of the meeting.

## Grading
We will grade your solution with the following guidelines.
 This list is ordered with highest-weighted factors at the top:
1. **Functional correctness**: The solution meets all functional requirements,
 including bonuses.
2. **Code composition and style**: Code follows appropriate coding standards and pep-8 guidelines.
3. **Communication**: The project includes a README and the code is well-commented.




## [News API](https://newsapi.org)
A simple REST API that can be used to retrieve breaking headlines and search for articles. **A free News API account is required to obtain an API key.**

| Route             | Description                                                                                                                |
|-------------------|----------------------------------------------------------------------------------------------------------------------------|
| [/v2/top-headlines](https://newsapi.org/docs/endpoints/top-headlines) | Returns live top and breaking headlines for a country, specific category in a country, single source, or multiple sources. |
| [/v2/sources](https://newsapi.org/docs/endpoints/sources) | Returns the subset of news publishers that top headlines are available from. |


## [Amazon S3](https://aws.amazon.com/s3/)
A simple cloud storage service run by Amazon Web Services (AWS). **An AWS account is needed to use AWS S3. Furthermore, AWS has a [free tier](https://aws.amazon.com/free/) that can be used for this challenge.**

Amazon provides a Python SDK (**[boto](http://boto3.readthedocs.io/en/latest/guide/resources.html)**), that provides an easy to use API for interacting with AWS S3.
