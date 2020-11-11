# https://www.youtube.com/watch?v=fKl2JW_qrso
# Python Multiprocessing Tutorial: Run Code in Parallel Using the Multiprocessing Module
import multiprocessing as mp
import time

# start = time.perf_counter()

def do_something():
    print('sleeping for 1 sec')
    time.sleep(1)
    print('done sleeping')

p1 = mp.Process(target=do_something)
p2 = mp.Process(target=do_something)

p1.start()
p1.join()

p2.start()
p2.join()

finish = time.perf_counter()

# counter = []
# for i in range(10):
#     print(f'started {i}th process!')
#     p = mp.Process(target=do_something)
#     counter.append(time.perf_counter())
#     p.start()
#     p.join()
#     counter.append(time.perf_counter())
#     print(counter[-1] - counter[-2])


print(f'finished in {finish-start} second(s)')
