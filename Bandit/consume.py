from json import loads, dumps
from kafka import KafkaConsumer
import mysql.connector

# Initialize the Kafka Consumer
my_consumer = KafkaConsumer(
    'testtopic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

print(my_consumer.__dict__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '#sh@h2a!B',
    'database': 'kafka'  # Use the name of your MySQL database
}

# Create a context manager for the MySQL connection
class MySQLContextManager:
    def __enter__(self):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


# Loop to consume messages and insert into the MySQL table
with MySQLContextManager() as cursor:
    for message in my_consumer:
        data = message.value
        # Insert data into the MySQL table
        sql = "INSERT INTO mytable (data) VALUES (%s)"
        val = (dumps(data),)

        cursor.execute(sql, val)
        
        print(f"Data {data} added to mytable in MySQL")
        q = input("Press 'q' or 'Q' to quit:")
        if q.lower() == 'q':
            break
