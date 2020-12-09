from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
 
default_dag_args = {
    'owner': 'group3',
    'start_date': datetime.now(),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}
dag = DAG(
    dag_id='group3_dag',
    schedule_interval = timedelta(days=1),
    default_args=default_dag_args
)
 
task1 = BashOperator(
task_id = "group3_dag1",
bash_command = "echo hello world",
dag = dag)
 
task2 = BashOperator(
task_id = "group3_dag2",
bash_command = "echo {​​​​{​​​​ ds }​​​​}​​​​",
dag = dag)
 
task3 = BashOperator(
task_id = "group3_dag3",
bash_command = "echo {​​​​{​​​​ ds_nodash }​​​​}​​​​",
dag = dag)
 
task1 >> task2 >> task3
