import os
import django
import pika

import sys
#from models import Comment
#from models import Comment

# Configure Django settings

def callback(ch, method, properties, body):
    #new_comment = Comment.objects.create(post_id=body.blog_id, comment=body.comment, author=body.username)
    print("Received message:", body)

# settings.py
RABBITMQ_HOST = '0.0.0.0'
RABBITMQ_PORT = 8005
RABBITMQ_USERNAME = 'guest'
RABBITMQ_PASSWORD = 'guest'
RABBITMQ_QUEUE = 'comments'
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST,
                                                               port=RABBITMQ_PORT,
                                                               credentials=pika.PlainCredentials(RABBITMQ_USERNAME,
                                                                                                  RABBITMQ_PASSWORD)))
channel = connection.channel()
channel.queue_declare(queue=RABBITMQ_QUEUE)
channel.basic_consume(queue=RABBITMQ_QUEUE,
                      on_message_callback=callback,
                      auto_ack=True)
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
