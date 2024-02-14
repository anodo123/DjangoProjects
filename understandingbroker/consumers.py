# consumer.py
import pika
from . import settings
from messagebrokerapp.models import Comment
def callback(ch, method, properties, body):
    new_comment = Comment.objects.create(post_id=body.blog_id, comment=body.comment, author=body.username)
    print("Received message:", body)

connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.RABBITMQ_HOST,
                                                               port=settings.RABBITMQ_PORT,
                                                               credentials=pika.PlainCredentials(settings.RABBITMQ_USERNAME,
                                                                                                  settings.RABBITMQ_PASSWORD)))
channel = connection.channel()
channel.queue_declare(queue=settings.RABBITMQ_QUEUE)
channel.basic_consume(queue=settings.RABBITMQ_QUEUE,
                      on_message_callback=callback,
                      auto_ack=True)
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()