#!/bin/bash

KAFKAZKHOSTS=$1
TOPICS_LIST=(test1 test2)
PARTITIONS_COUNT=$2
REPLICATION_FACTOR=$3
echo "Start"
echo $KAFKAZKHOSTS
echo "Stop"

for i in ${TOPICS_LIST[@]}; do
    echo $i
    if /usr/hdp/current/kafka-broker/bin/kafka-topics.sh --create --replication-factor $REPLICATION_FACTOR --partitions $PARTITIONS_COUNT --topic $i --zookeeper $KAFKAZKHOSTS; then
        echo "Topic created sucessfully"
    else
        echo "Topic already exist"
    fi
done

exit 0