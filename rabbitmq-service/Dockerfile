FROM rabbitmq:3.9.5-management

# Define environment variables.
ENV RABBITMQ_PID_FILE /var/lib/rabbitmq/mnesia/rabbitmq

# First User
ENV RABBITMQ_USER admin

ENV RABBITMQ_PASSWORD password

# Second User
ENV RABBITMQ_USER_1 mqtt

ENV RABBITMQ_PASSWORD_1 mqtt

# copy the certs
COPY ./certs/ /etc/rabbitmq/cert 

VOLUME [ "/etc/letsencrypt/live/service.talentfind.io" ]

ADD init.sh /init.sh

ADD rabbitmq.conf /etc/rabbitmq/

RUN chmod +x /init.sh 

RUN chown rabbitmq:rabbitmq /etc/rabbitmq/rabbitmq.conf

EXPOSE 15672 5671 5672 8883 1883 15675 15676 

# Define default command
CMD ["/init.sh", "rabbitmq-server"]

