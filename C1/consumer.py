import pulsar 
 
# Create a pulsar client by supplying ip address and port 
client = pulsar.Client('pulsar://localhost:6650') 
  
# Subscribe to a topic and subscription  
consumer = client.subscribe('DEtopic', subscription_name='DE-sub') 
producer2 = client.create_producer('DEtopic2')    
# Display message received from producer 
msg = consumer.receive()     
try: 
    for i in str(msg.data().decode('utf-8')).split():
        producer2.send((i).encode('utf-8'))
             
    # Acknowledge for receiving the message  
    consumer.acknowledge(msg) 

except: 
      consumer.negative_acknowledge(msg) 
      # Destroy pulsar client
client.close()
