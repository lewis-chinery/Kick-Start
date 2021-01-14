# ---------- I/O setup ----------
import sys, os

# get input file paths
current_directory = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(current_directory, "Bad_Horse_input.txt")

# redirect stdin file handlers to txt file
sys.stdin=open(input_path, 'r')

# ---------- Solution ----------

# get number of test cases
T = int(input())

for t in range(1, T+1):

    # get number of pairs of names in each test case
    M = int(input())
    names = []

    for m in range(1, M+1):
        # get each 'troublesome pairing'
        name1, name2 = [name for name in input().split()]
        names.append([name1, name2])

    # print desired output
    print("Case #{}: {}".format(t, names))
