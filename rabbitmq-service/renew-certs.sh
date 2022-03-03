#!/bin/sh
# Path: scripts/cert-new.sh
# print all the values in /etc/letsencrypt/live/service.talentfind.io/fullchain.pem
echo "Renewing the certs"
sudo certbot renew --dry-run

echo "Removing the old certs"
rm /root/rabbitmq-service/certs/*

echo "Copying the values from letencrypt to the certs folder."
cat /etc/letsencrypt/live/service.talentfind.io/cert.pem > /root/rabbitmq-service/certs/cert.pem
cat /etc/letsencrypt/live/service.talentfind.io/chain.pem > /root/rabbitmq-service/certs/chain.pem
cat /etc/letsencrypt/live/service.talentfind.io/fullchain.pem > /root/rabbitmq-service/certs/fullchain.pem
cat /etc/letsencrypt/live/service.talentfind.io/privkey.pem > /root/rabbitmq-service/certs/privkey.pem

echo "List the files."
ls -la 

echo "Renew Complete."

