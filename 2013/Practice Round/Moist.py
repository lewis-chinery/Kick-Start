# ---------- I/O setup ----------
import sys, os

# get input & output file paths (change as needed)
current_directory = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(current_directory, "Moist_input.txt")
output_path = os.path.join(current_directory, "Moist_output.txt")

# redirect stdin & stdout file handlers to txt files
sys.stdin=open(input_path, 'r')
# comment out below line to print to console instead
# sys.stdout=open(output_path, 'w')

# ---------- Solution ----------

# get number of test cases
T = int(input())

for t in range(1, T+1):
    # get number of names in the test case
    N = int(input())

    # initialise name list
    name_list = []
    for n in range(N):
        name_list.append(input())

    # get number of moves needed to sort list
    largest_name = name_list[0]
    num_moves = 0
    for name in name_list:
        if name < largest_name:
            num_moves += 1
        if name > largest_name:
            largest_name = name
            
    # print desired output
    print("Case #{}: {}".format(t, num_moves))