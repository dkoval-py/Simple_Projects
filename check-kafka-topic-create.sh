#!/bin/bash

wget -O "topics.json" "https://raw.githubusercontent.com/dkoval-py/Simple_Projects/master/topics.json"
ls -la
hostname
ip a
pwd
KAFKAZKHOSTS=$1
TOPICS_NAMES=(`jq -c '.[]' topics.json | jq -r '[.name]|join(" ")'`)
PARTITIONS=(`jq -c '.[]' topics.json | jq -r '[.partitions]|join(" ")'`)
REPLICATIONS=(`jq -c '.[]' topics.json | jq -r '[.replication]|join(" ")'`)
echo "Start"
echo $KAFKAZKHOSTS
echo $2
echo $TOPICS_NAMES
echo $PARTITIONS
echo $REPLICATIONS
echo "Stop"


for i in $(seq 1 ${#TOPICS_NAMES[@]}); do
    let "i=i-1"
    if /usr/hdp/current/kafka-broker/bin/kafka-topics.sh --create --replication-factor ${REPLICATIONS[$i]} --partitions ${PARTITIONS[$i]} --topic ${TOPICS_NAMES[$i]} --zookeeper $KAFKAZKHOSTS; then
        echo "Topic created sucessfully"
    else
        echo "Topic already exist"
    fi
done

exit 0