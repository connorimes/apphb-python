"""A dummy application using heartbeats with logging that formats floating point output."""
import csv
import random
import sys
from apphb import logging, Heartbeat

def kernel():
    """Dummy application kernel"""
    return 0

def format_record(record):
    """Format float values to high precision, not in exponential form."""
    return [f'{r:.15f}' if isinstance(r, float) else r for r in record]

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

    # by default, provide heartbeat with only the elapsed time for each iteration
    # provide heartbeat with start and end values for "energy" field
    hbt = Heartbeat(window_size)
    # Let's report time in nanoseconds. which makes heart rates very small
    with open(hbt_log, 'w', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(logging.get_log_header(hbt, time_name='Time (ns)',
                                               heartrate_name='Heartrate (Heartbeats/ns)'))

    for tag in range(total_iters):
        # with these dummy times, average performances should be ~0.25 heartbeats/sec
        start_time_ns = (tag * 10000000000) + random.randint(0, 5000000000)
        kernel()
        end_time_ns = (tag * 10000000000) + random.randint(5000000001, 9999999999)
        hbt.heartbeat(tag, (end_time_ns - start_time_ns,))
        with open(hbt_log, 'a', encoding="utf8") as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            rec = logging.get_log_records(hbt, count=1)[0]
            writer.writerow(format_record(rec))


if __name__ == '__main__':
    run()
