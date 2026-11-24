#!/bin/sh
destino=$1
for i in 1 2 3 4 5; do
  python subscriber.py "$destino" --nome "sub$i" $SUB_OPTS &
done
sleep 3
python publisher.py "$destino" $PUB_OPTS
wait
