"""A dummy application using heartbeats with logging and field normalization."""
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

    # by default, provide heartbeat with only the elapsed time for each iteration
    # provide heartbeat with start and end values for "energy" field
    hbt = Heartbeat(window_size, fields_shape=(2,))
    # Let's report time in nanoseconds and energy in microJoules, but normalize logging to present
    # time in ms, heartrate in hb/s, energy in mJ, and Power in W (i.e., J/s), thus:
    # time normalization factor (ns * x = ms): x = 1/1000000
    # time rate normalization factor (hb/ns * x = hb/s): x = 1000000000
    # energy normalization factor (uJ * x = mJ): x = 1/1000
    # power normalization factor (uJ / ns * x = J / ms * x = J/s: x = 1000
    with open(hbt_log, 'w', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(logging.get_log_header(hbt, time_name='Time (ms)',
                                               heartrate_name='Heartrate (Heartbeats/sec)',
                                               field_names=["Energy (mJ)"],
                                               field_rate_names=["Power (W)"]))

    for tag in range(total_iters):
        # with these dummy times, average performances should be ~0.25 heartbeats/sec
        # with these dummy energy values, average power should be ~1 Watts
        start_time_ns = (tag * 10000000000) + random.randint(0, 5000000000)
        start_uj = (tag * 10000000) + random.randint(0, 5000000)
        kernel()
        end_time_ns = (tag * 10000000000) + random.randint(5000000001, 9999999999)
        end_uj = (tag * 10000000) + random.randint(5000001, 9999999)
        hbt.heartbeat(tag, (end_time_ns - start_time_ns,), fields=((start_uj, end_uj),))
        with open(hbt_log, 'a', encoding="utf8") as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            rec = logging.get_log_records(hbt, count=1, time_norm=1/1000000,
                                          heartrate_norm=1000000000, field_norms=[1/1000],
                                          field_rate_norms=[1000])[0]
            writer.writerow(rec)


if __name__ == '__main__':
    run()
