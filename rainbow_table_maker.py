import itertools

chrs = 'ABCDEFG'
cnt = 0

while cnt <= len(chrs):

    for xs in itertools.product(chrs, repeat=cnt):
        print(''.join(xs)) 
    
    cnt = cnt+1
