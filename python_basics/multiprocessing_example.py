import multiprocessing
from multiprocessing import Pool 

def spawned(num):
    print(f'Spawned {num}')

def run_process():
    for i in range(55):
        p = multiprocessing.Process(target=spawned, args=(i, ))
        p.start()
        #p.join()

def job(num):
    return num ** 2

def run_mult_proc():
    with Pool(processes=20) as p:
        data = p.map(job, range(5))
    print(data)

if __name__ == '__main__':
    run_mult_proc()