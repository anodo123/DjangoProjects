# RabbitMQ Message Consumer

Welcome to the RabbitMQ Message Consumer project! This project demonstrates how to set up a RabbitMQ consumer in Python to process messages from a queue. By following the instructions below, you'll be able to set up RabbitMQ using Docker, configure the Python consumer, and start processing messages.

## Overview

The RabbitMQ Message Consumer project showcases the integration of RabbitMQ, a robust message broker, to facilitate asynchronous communication between components. The Python consumer script listens to a specified RabbitMQ queue, processes incoming messages, and performs designated actions.

## Setup RabbitMQ using Docker

To set up RabbitMQ using Docker, follow these steps:

1. Install Docker on your machine if you haven't already. You can download Docker from [here](https://www.docker.com/get-started).

2. Pull the RabbitMQ Docker image by running the following command in your terminal:

    ```bash
    docker pull rabbitmq:management
    ```

3. Run RabbitMQ Docker container with the following command:

    ```bash
    docker run -d --name rabbitmq -p 5672:5672 -p 8005:15672 rabbitmq:management
    ```

   This command will start a RabbitMQ container with management UI available at `http://localhost:8005`. You can access the RabbitMQ dashboard by opening this URL in your web browser.

## Configure and Run the Python Consumer

Before running the Python consumer script, make sure you have Python and the necessary dependencies installed. You can install dependencies by running:

```bash
pip install pika
Now, follow these steps to configure and run the Python consumer:

Clone this repository to your local machine.

Navigate to the project directory in your terminal.

Open the consumers.py file and update the RabbitMQ connection settings according to your RabbitMQ setup. You can modify the following variables:

python
Copy code
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 8005
RABBITMQ_USERNAME = 'guest'
RABBITMQ_PASSWORD = 'guest'
RABBITMQ_QUEUE = 'comments'
Save the changes and close the file.

Run the Python consumer script using the following command:

bash
Copy code
python consumers.py
The consumer script will start listening for messages on the specified RabbitMQ queue. You'll see output indicating that it's waiting for messages.

To stop the consumer script, press CTRL+C in your terminal.

Contributing
Contributions to this project are welcome! If you have any ideas for improvements or find any issues, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
