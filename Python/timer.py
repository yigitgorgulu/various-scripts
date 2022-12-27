import os
import random
import time

def avg(ls: list[int]) -> int:
    sum = 0
    for i in ls:
        sum += i
    return sum / len(ls)


if __name__ == '__main__':
    # create mock data
    partitions = [
        'P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08',
        'P09', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16',
        'P17', 'P18', 'P19', 'P20', 'P21', 'P22', 'P23', 'P24'
    ]
    execution_times = []

    print('Starting execution...')

    start = time.time()
    for idx, partition in enumerate(partitions):
        exec_start = time.time()
        
        time.sleep((random.random() * 5) + 1) # do work here

        execution_times.append(time.time() - exec_start)
        elapsed_time = time.time() - start
        expected_remaining = avg(execution_times) * (len(partitions) - (idx + 1))
        
        os.system('cls')
        print(f'''
        
         ____________________________________
        |                                    |
        |        Start time: {time.strftime('%H:%M:%S', time.gmtime(start - time.timezone))}        |
        |     Last processed: {partition}({(idx + 1):>2d}/{len(partitions)})     |
        |       Elapsed time: {(elapsed_time // 60):>3.0f}m {(elapsed_time % 60):>2.0f}s       |
        | Estimated time remaining: {(expected_remaining // 60):>3.0f}m {(expected_remaining % 60):>2.0f}s |
        |   Estimated completion: {time.strftime('%H:%M:%S', time.gmtime(time.time() - time.timezone + expected_remaining))}   |
        |                                    |
         ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        ''')
    
    print(f'Execution completed in {time.time() - start} seconds.')