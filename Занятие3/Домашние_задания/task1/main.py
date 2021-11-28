input_file_1 = 'n1'
input_file_2 = 'n2'

def task_1():
    with open(input_file_1, 'r') as f:
        list_z = f.readline()
        # for l_1 in f:
        #        z = f.readline()
        print(list_z)
    return list_z
def task_2():
    with open(input_file_2, 'r') as g:
        list_v = g.readline()
        # for l_2 in g:
        #        v = g.readline()
        print(list_v)
    return list_v

if __name__ == "__main__":
    # Write your solution here
    z = task_1()
    v = task_2()
    n = ''.join(z) + ''.join(v)
    val = filter(str.isdigit, n)
    print(list("".join(val)))


