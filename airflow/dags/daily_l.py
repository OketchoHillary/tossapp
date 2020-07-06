from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
import time
from datetime import datetime, timedelta

import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tauth.settings")
django.setup()

from lotto_api.daily_l import create_daily_lotto, daily_draw



def daily_draw_wait():
    time.sleep(86100)

args = {
    'owner': 'Airflow',
    'start_date': datetime(2020, 6, 9),
    'depends_on_past': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='daily_lotto',
    schedule_interval='@daily',
    catchup=False,
    default_args=args
)

daily_lotto_creation = PythonOperator(
    task_id='new_daily_lotto',
    python_callable= create_daily_lotto,
    dag=dag,
)


daily_draw_waiter = PythonOperator(
    task_id='daily_draw_wait',
    python_callable= daily_draw_wait,
    dag=dag,
)

run_daily_draw = PythonOperator(
    task_id='daily_draw',
    python_callable= daily_draw,
    dag=dag,
)

daily_lotto_creation.set_downstream(daily_draw_waiter)
daily_draw_waiter.set_downstream(run_daily_draw)

# hello_bash_task = BashOperator(
#     task_id='hello_task_bash',
#     bash_command='python /mnt/c/Users/lucy/PycharmProjects/toss_api/manage.py d_sched',
#     dag=dag,
# )