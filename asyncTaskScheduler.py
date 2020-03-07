# in memory asynchronous task scheduler + executer
# submit tasks, specify delay
# max number of processes
from __future__ import print_function
import time
import heapq
import threading

class AsyncTaskScheduler:
    def __init__(self, maxThreads):
        self.maxThreads = maxThreads
        # self.availableThreads = maxThreads
        self.threadIsAvailable = True
        self.queue = []
        poller = threading.Thread(name = "poller", target = self.pollQueue)
        poller.start()

    def enqueueTask(self, task, args, delay):
        currentTime = time.time()
        timeToExecuteAt = currentTime + delay
        heapq.heappush(self.queue, (timeToExecuteAt, task, args))
        return True

    def dequeTask(self):
        # if self.availableThreads > 0:
        if not self.threadIsAvailable:
            return
        else:
            self.threadIsAvailable = False
            _, task, args = heapq.heappop(self.queue)
            curr = threading.Thread(name = "curr", target = task, args = args)
            curr.start()
            curr.join()
            self.threadIsAvailable = True

    def pollQueue(self):
        while True:
            if len(self.queue) > 0:
                requiredEpoch, _, _ = self.queue[0]
                currentTime = time.time()
                if requiredEpoch >= currentTime:
                    self.dequeTask()
            time.sleep(1)

scheduler = AsyncTaskScheduler(1)
scheduler.enqueueTask(print, "SECOND", 10)
scheduler.enqueueTask(print, "FIRST", 2)
