"""A dummy application using heartbeats with logging."""
import csv
import random
import sys
from apphb import logging, Heartbeat

def kernel():
    """Dummy application kernel"""
    return 0

def run():
    """Main application loop"""
    total_iters = 10
    window_size = 2
    hbt_log = 'heartbeat.csv'
    if len(sys.argv) > 1:
        total_iters = int(sys.argv[1])
    if len(sys.argv) > 2:
        window_size = int(sys.argv[2])
    if len(sys.argv) > 3:
        hbt_log = sys.argv[3]

    # provide heartbeat with both start and end times for each iteration
    hbt = Heartbeat(window_size, time_shape=2)
    with open(hbt_log, 'w', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(logging.get_log_header(hbt))

    for tag in range(total_iters):
        # with these dummy times, average performances should be ~0.2 heartbeats/sec
        start_time = (tag * 10) + random.randint(0, 4)
        kernel()
        end_time = (tag * 10) + random.randint(5, 9)
        hbt.heartbeat(tag, (start_time, end_time))
        with open(hbt_log, 'a', encoding="utf8") as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            rec = logging.get_log_records(hbt, count=1)[0]
            writer.writerow(rec)


if __name__ == '__main__':
    run()
