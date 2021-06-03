#!/bin/bash

KAFKAZKHOSTS=$1
TOPICS_LIST=(test1 test2)
echo "Start"
echo $KAFKAZKHOSTS
echo "Stop"

for i in ${TOPICS_LIST[@]}; do
  if /usr/hdp/current/kafka-broker/bin/kafka-topics.sh --create --replication-factor 1 --partitions 1 --topic $i --zookeeper $KAFKAZKHOSTS; then
        echo "Topic created sucessfully"
  else
        echo "Topic already exist"
  fi
done

exit 0