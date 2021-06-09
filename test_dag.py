from airflow import DAG
from airflow.operators.bash_operator import BashOperator

DAG_ID='test_dag'                                                                                                                                                                                
default_args = {
'owner':'datalakers.lucas',
'start_date': '2021-02-02',
'email': ['datalakers.lucas@grupofleury.com.br'],
'email_on_failure': False,
'email_on_success': False,
}



with DAG(DAG_ID, default_args = default_args, schedule_interval="30 10 * * *",tags=["prd"]) as dag:
    test = BashOperator(
        task_id='hello_airflow_k8s',
        bash_command='echo "Hello Airflow Again!!!!"',
        retries=3
        )
    
