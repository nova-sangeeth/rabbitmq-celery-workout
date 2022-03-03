#!/bin/sh

# Create Rabbitmq user
( rabbitmqctl wait --timeout 60 $RABBITMQ_PID_FILE ; \
rabbitmqctl add_user $RABBITMQ_USER $RABBITMQ_PASSWORD 2>/dev/null ; \
rabbitmqctl set_user_tags $RABBITMQ_USER administrator ; \
rabbitmqctl set_permissions -p / $RABBITMQ_USER  ".*" ".*" ".*" ; \
# Creating second user
rabbitmqctl add_user $RABBITMQ_USER_1 $RABBITMQ_PASSWORD_1 2>/dev/null ; \
rabbitmqctl set_user_tags $RABBITMQ_USER_1 administrator ; \
rabbitmqctl set_permissions -p / $RABBITMQ_USER_1  ".*" ".*" ".*" ; \
# enabling plugins for mqtt and management
rabbitmq-plugins enable rabbitmq_management ; \
rabbitmq-plugins enable rabbitmq_web_mqtt  ; \
# Creating new exchange
rabbitmqadmin declare exchange name=notification type=topic
# List all the exchanges
echo "*** Show all the the available Exchanges.***"
rabbitmqctl list_exchanges

echo "*** User '$RABBITMQ_USER' with password '$RABBITMQ_PASSWORD' completed. ***" ; \
echo "*** User '$RABBITMQ_USER_1' with password '$RABBITMQ_PASSWORD_1' completed. ***" ; \
echo "*** Log in the WebUI at port 15672 (example: http:/localhost:15672) ***") &

# $@ is used to pass arguments to the rabbitmq-server command.
# For example if you use it like this: docker run -d rabbitmq arg1 arg2,
# it will be as you run in the container rabbitmq-server arg1 arg2
rabbitmq-server $@
