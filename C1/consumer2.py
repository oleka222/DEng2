import pulsar
client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('DEtopic2', subscription_name = 'DE-sub2')
producer3 = client.create_producer('DEtopic3')
while(True):
    msg = consumer.receive()
    try:
        print(msg.data().decode('utf-8').upper())
        producer3.send((msg.data().decode('utf-8').upper()).encode('utf-8'))
        
    # Acknowledge for receiving the message  
        consumer.acknowledge(msg)
    except:
        consumer.negative_acknowledge(msg)

client.close()
