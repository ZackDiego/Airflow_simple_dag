from airflow.decorators import dag, task

import pendulum

default_args = {
    "owner" : "Zack",
    "retries": 5,
    "retry_delay":pendulum.duration(minutes=5),
    "catchup":False
}

@dag(dag_id = "Greeting_v2",
    description = "this is a greeting function",
    default_args = default_args,
    start_date = pendulum.datetime(2023, 8, 6, tz = "Asia/Taipei"),
    schedule_interval = "@daily")
def hello_task_tel():
    @task(multiple_outputs = True)
    def getName():
        return {"first_name":"John", "last_name":"Wick"}

    @task
    def getAge():
        return 18

    @task
    def greet(firstname, lastname, age):
        print(f'hello {firstname} {lastname}, your age is {age}')
            
    name_dict = getName()
    age = getAge()
    greet(firstname = name_dict["first_name"], lastname= name_dict["last_name"],
        age = age)

greet_dag = hello_task_tel()