import DAG from airflow
 
dag = DAG(
dag_id = "group3",
start_date = "2020-12-09",
interval = "1 day")
 
task1 = BashOperator(
task_id = "group3_dag",
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
