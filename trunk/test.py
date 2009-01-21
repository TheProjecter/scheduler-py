import scheduler
import datetime
import time

timeout=5

def printMe(msg={'msg':'I am running once.'}):
    print msg['msg']
    return True

# Create a scheduler - this can now occur before a task is scheduled
my_scheduler = scheduler.Scheduler()

# Create a task called "foo", that runs a function named "printMe" with 
# optional arguments in a dict
foo_task = scheduler.Task("foo",
                          datetime.datetime.now(),
                          scheduler.every_x_secs(2), 
                          scheduler.RunOnce(printMe, {'msg':'this is a sound from way out'}))
# Once started, the scheduler will identify the next task to run and execute it.
# if there are no tasks it silently does nothing
my_scheduler.start()
# Add the foo task, a receipt is returned that can be used to drop the task from the scheduler
foo_receipt = my_scheduler.schedule_task(foo_task)
print foo_receipt
# Stop the scheduler
print 'sleeping for %s sec...' % (timeout)
time.sleep(timeout)
print 'waking up and killing scheduler'
my_scheduler.halt()
