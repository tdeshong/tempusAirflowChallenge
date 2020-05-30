from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import logging
import os
from challenge as c


NEWS_KEY = os.environ.get('NEWS_KEY')     #api key for newsapi.org
news = c.News(NEWS_KEY)                   #constructor from challenge
bucket, sourceName = os.environ.get('s3bucket'), os.environ.get('soureName')
LOGGER = logging.getLogger('airflow.task')

#function for the logs
def printContext(**kwargs):
    logging.info('top highlights - {}'.format(kwargs))
    return 'Success'


dag_id ="top_highlights"

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': seven_days_ago,
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
)

dag = DAG('tempus', default_args=default_args,
           description = 'Newsapi top highlights',
           schedule_interval = timedelta(days=1),
)

task = PythonOperator(
    task_id='top_highlights',
    provide_context=True,
    # provide params and additional kwargs to python_callable
    python_callable=news.flatten,
    op_kwargs={'s3bucket': bucket, 'sourceName':sourceName}
    dag=dag,
)

context =  PythonOperator(
    task_id='print_logs',
    provide_context=True,
    python_callable=printContext,
    dag=dag,
)
    
context << task
