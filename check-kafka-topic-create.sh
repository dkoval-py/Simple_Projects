#!/bin/bash

wget -O "/topics.json" "https://raw.githubusercontent.com/dkoval-py/Simple_Projects/master/topics.json"
KAFKAZKHOSTS=$1
TOPICS_NAMES=(`jq -c '.[]' /topics.json | jq -r '[.name]|join(" ")'`)
PARTITIONS=(`jq -c '.[]' /topics.json | jq -r '[.partitions]|join(" ")'`)
REPLICATIONS=(`jq -c '.[]' /topics.json | jq -r '[.replication]|join(" ")'`)

for i in $(seq 1 ${#TOPICS_NAMES[@]}); do
    let "i=i-1"
    if /usr/hdp/current/kafka-broker/bin/kafka-topics.sh --create --replication-factor ${REPLICATIONS[$i]} --partitions ${PARTITIONS[$i]} --topic ${TOPICS_NAMES[$i]} --zookeeper $KAFKAZKHOSTS; then
        echo "##[section]Topic ${TOPICS_NAMES[$i]} created sucessfully"
    else
        echo "##vso[task.logissue type=warning]Topic ${TOPICS_NAMES[$i]} already exists"
    fi
done

exit 0