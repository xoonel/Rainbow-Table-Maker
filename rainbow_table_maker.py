import itertools

chrs = 'ABCDEF'

cnt = 0

# Creates the rainbow table text document; overwrites previous ones if program is run.
rnbwtbl_file = open("rainbow_table.txt", "w")

while cnt <= len(chrs):

    for i in itertools.product(chrs, repeat=cnt):
        # Prints all possible character permutations in the shell.
        print(''.join(i)) 
        # Concurrently writes all possible possible character permutations to text document () contiguously with no formatting.
        rnbwtbl_file.write(''.join(i))
    cnt = cnt+1
