#!/bin/bash


TOPICS_LIST=(test1 test2)

echo $KAFKAZKHOSTS

for i in ${TOPICS_LIST[@]}; do
  if /usr/hdp/current/kafka-broker/bin/kafka-topics.sh --create --replication-factor 1 --partitions 1 --topic $i --zookeeper $KAFKAZKHOSTS; then
        echo "Topic created sucessfully"
        exit 0
  else
        echo "Topic already exist"
        exit 0
  fi
done
