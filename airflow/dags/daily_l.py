from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

def print_r():
    print('Raul')

args = {
    'owner': 'Airflow',
    'start_date': datetime(2020, 4, 1),
    'depends_on_past': True,
}

dag = DAG(
    dag_id='oketcho',
    schedule_interval='0 2 * * *',
    default_args=args,
    tags=['example']
)

hello_my_task = PythonOperator(
    task_id='hello_task',
    python_callable=print_r,
    dag=dag,
)