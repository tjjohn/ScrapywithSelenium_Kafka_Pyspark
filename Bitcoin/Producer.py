from kafka import KafkaProducer
from datetime import datetime
import time
from json import dumps
import random
import sys
import json

KAFKA_TOPIC_NAME_CONS = "coin"
KAFKA_BOOTSTRAP_SERVERS_CONS = 'localhost:9092'

if __name__ == "__main__":
    print("Kafka Producer Application Started ... ")

    kafka_producer_obj = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS_CONS,
                                       value_serializer=lambda x: dumps(x).encode('utf-8'))

    with open('coin_data.json') as f:
        d = json.load(f)
        print(d)


    kafka_producer_obj.send(KAFKA_TOPIC_NAME_CONS, d)  # data sent to consumer
    time.sleep(1)
    print("Kafka Producer Application Completed. ")
    # print(message_list)
