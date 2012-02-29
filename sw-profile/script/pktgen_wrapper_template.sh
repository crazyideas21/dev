#!/bin/sh

# Not to be used directly. See ../src/pktgen.py::send()

modprobe pktgen


pgset() {
    local result

    echo $1 > $PGDEV

    result=`cat $PGDEV | fgrep "Result: OK:"`
    if [ "$result" = "" ]; then
         cat $PGDEV | fgrep Result:
    fi
}

pg() {
    echo inject > $PGDEV
    cat $PGDEV
}

# Config Start Here -----------------------------------------------------------


# thread config
# Each CPU has own thread. Two CPU exammple. We add eth1, eth1 respectivly.

PGDEV=[PKTGEN_PROC]kpktgend_0
  echo "Removing all devices"
 pgset "rem_device_all" 
  echo "Adding [PKTGEN_IFACE]"
 pgset "add_device [PKTGEN_IFACE]" 


# device config
# delay 0
# We need to do alloc for every skb since we cannot clone here.

CLONE_SKB="clone_skb 0"
# NIC adds 4 bytes CRC
PKT_SIZE="pkt_size [PKT_SIZE]"

# COUNT 0 means forever
#COUNT="count 0"
COUNT="count [PKT_COUNT]"
DELAY="delay [DELAY]"

PGDEV=[PKTGEN_PROC][PKTGEN_IFACE]
  echo "Configuring $PGDEV"
 pgset "$COUNT"
 pgset "$CLONE_SKB"
 pgset "$PKT_SIZE"
 pgset "$DELAY"

 pgset "src_min [SRC_IP]"
 pgset "dst     [DST_IP]"
 pgset "dst_mac [DST_MAC]"

 pgset "udp_src_min 10000"
 pgset "udp_src_max [MAX_PORT]"



# Time to run
PGDEV=[PKTGEN_PROC]pgctrl

 echo "Running... ctrl^C to stop"
 pgset "start" 
 echo "Done"

# Result can be vieved in /proc/net/pktgen/eth1
