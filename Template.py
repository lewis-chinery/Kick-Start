# ---------- I/O setup ----------
import sys, os

# get input & output file paths (change as needed)
current_directory = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(current_directory, "input.txt")
output_path = os.path.join(current_directory, "output.txt")

# redirect stdin & stdout file handlers to txt files
sys.stdin=open(input_path, 'r')
# comment out below line to print to console instead
sys.stdout=open(output_path, 'w')

# ---------- Solution ----------

# get number of test cases
T = int(input())

for t in range(1, T+1):
    # get number of names in the test case
    N = int(input())
    N_out = N**3

    # print desired output
    print("Case #{}: {}".format(t, N_out))
