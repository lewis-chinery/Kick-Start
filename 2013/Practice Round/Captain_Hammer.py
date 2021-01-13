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
    V, D = [int(i) for i in input().split()]

    # calculate theta (degrees between 0 and 90)
    theta = 180/math.pi * abs(0.5 * math.asin(-9.8*D / (V**2)))

    # return to 7 decimal places
    theta = format(theta, '.7f')

    # print desired output
    print("Case #{}: {}".format(t, theta))
