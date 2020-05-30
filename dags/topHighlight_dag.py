from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
import os
from challenge as c


NEWS_KEY = os.environ.get('NEWS_KEY')     #api key for newsapi.org
news = c.News(NEWS_KEY)                   #constructor from challenge
bucket, sourceName = os.environ.get('s3bucket'), os.environ.get('soureName')


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
    python_callable=news.flatten,
    op_kwargs={'s3bucket': bucket, 'sourceName':sourceName}
    dag=dag
)

end = DummyOperator(
    task_id='end',
    dag=dag
)
    
end << task
