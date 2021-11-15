"""A dummy application using heartbeats."""
import random
import sys
from apphb import Heartbeat

def kernel():
    """Dummy application kernel"""
    return 0

def run():
    """Main application loop"""
    total_iters = 10
    window_size = 2
    if len(sys.argv) > 1:
        total_iters = int(sys.argv[1])
    if len(sys.argv) > 2:
        window_size = int(sys.argv[2])

    # by default, provide heartbeat with only the elapsed time for each iteration
    hbt = Heartbeat(window_size)

    for tag in range(total_iters):
        # with these dummy times, average performances should be ~0.2 heartbeats/sec
        start_time = (tag * 10) + random.randint(0, 4)
        kernel()
        end_time = (tag * 10) + random.randint(5, 9)
        hbt.heartbeat(tag, (end_time - start_time,))
        print(str(tag) + ': Instant performance: ' + str(hbt.get_instant_rate()))
        print(str(tag) + ': Window performance: ' + str(hbt.get_window_rate()))
    print('Global performance: ' + str(hbt.get_global_rate()))


if __name__ == '__main__':
    run()
