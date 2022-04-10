import pulsar
client = pulsar.Client('pulsar://localhost:6650') 
 
# Subscribe to a topic and subscription  
consumer = client.subscribe('DEtopic3', subscription_name='DE-sub3')
sentence = ''
while(True):
    msg = consumer.receive()
    try:
        #merge upper-cased words into a sentence 
        sentence = sentence + msg.data().decode('utf-8') + ' '
    
        consumer.acknowledge(msg)
    except:
        consumer.negative_acknowledge(msg)
    print(sentence)
client.close()
