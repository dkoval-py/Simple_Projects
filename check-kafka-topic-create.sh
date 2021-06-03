#!/bin/bash

if /usr/hdp/current/kafka-broker/bin/kafka-topics.sh --create --replication-factor 1 --partitions 1 --topic test-topic --zookeeper zk1-intrac.gvua5lvbodjevd1tlu31gxlc2a.ax.internal.cloudapp.net:2181,zk2-intrac.gvua5lvbodjevd1tlu31gxlc2a.ax.internal.cloudapp.net:2181 > /dev/null 2>&1; then
        exit 0
else
        exit 100
fi

