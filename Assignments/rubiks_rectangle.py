import sys
import queue

first_state = input('Input final configuration: ')
final_state = str(12345678)
if first_state == final_state:
    print ('0 step is needed to reach the final configuration.')
    sys.exit()
try:
    fin = []
    for i in first_state:
        if i == ' ':
            continue
        fin.append(i)
    if len(fin) != 8:
        raise ValueError

    for j in range(8):
        if int(fin[j]) < 1:
            raise ValueError
        if fin[j] in fin[j +1:]:
            raise ValueError       
except ValueError:
    print('Incorrect configuration, giving up...')
    sys.exit()
first_state = fin[0]+fin[1]+fin[2]+fin[3]+fin[4]+fin[5]+fin[6]+fin[7]
steps = 0
progress = set() 
q = queue.Queue()   

def bingo(e):
    if e == first_state:
        print(str(steps) + ' steps are needed to reach the final configuration.')
        sys.exit()
    
    if e not in progress:
        progress.add(e)
        q.put(e)

def find():
    Ind = bingo(final_state)
    return Ind

find()

while not q.empty():
    
    steps = steps + 1
    size = q.qsize()
    for i in range(0, size):
        current = q.get()       
        bingo(current[7] + current[6] + current[5] + current[4] + current[3] + current[2] + current[1] + current[0])
        bingo(current[3] + current[0] + current[1] + current[2] + current[5] + current[6] + current[7] + current[4])
        bingo(current[0] + current[6] + current[1] + current[3] + current[4] + current[2] + current[5] + current[7])
        
        
    

