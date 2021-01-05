# ---------- I/O setup ----------
import sys, os

# get input file paths
current_directory = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(current_directory, "Hammer_input.txt")

# redirect stdin file handlers to txt file
sys.stdin=open(input_path, 'r')

# ---------- Solution ----------

# first use time = distance / horizontal speed
# then use SUVAT eqn for vertical motion v = u + at
# eliminate t and rearrange for theta (use sine double angle formula)

import math

# get number of test cases
T = int(input())

for t in range(1, T+1):
    # get launch speed and distance travelled for each test
    V_D = input().split()
    V, D = V_D[0], V_D[1]

    # print desired output
    print("Case #{}: V = {}, D = {}".format(t, V, D))
