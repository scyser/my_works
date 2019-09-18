filename = "input.txt"
import copy
def swap(array, index):
    temp = copy.deepcopy(array[index])
    array[index] = array[index+1]
    array[index+1] = temp

# using insertion sorting to find the poorest, the richest and the middle rich habitants

with open(filename, "r") as file_in:
    n = int(file_in.readline().strip())
    a = file_in.readline().strip().split()
    array = [[float(a[i]), i + 1] for i in range(n)]
    with open("output.txt", "w") as file_out:
        for j in range(1, n):
            i = j - 1
            while i >= 0 and array[i] > array[i+1]:
                swap(array, i)
                i -= 1
        file_out.write(
            str(array[0][1]) + " " +
            str(array[n // 2][1]) + " " +
            str(array[n - 1][1]))


