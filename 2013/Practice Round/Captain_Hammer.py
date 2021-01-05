# ---------- I/O setup ----------
import sys, os

# get input file paths
current_directory = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(current_directory, "Hammer_input.txt")

# redirect stdin file handlers to txt file
sys.stdin=open(input_path, 'r')

# ---------- Solution ----------

# get number of test cases
T = int(input())

for t in range(1, T+1):
    # get number of names in the test case
    N = int(input())
    N_out = N**3

    # print desired output
    print("Case #{}: {}".format(t, N_out))
