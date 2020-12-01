f = open('input','r')
lines = f.readlines()
striped_lines = [int(l.strip()) for l in lines]
number_of_lines = len(striped_lines)
for i in range(0,number_of_lines):
    for j in range(i,number_of_lines):
        if striped_lines[i] + striped_lines[j]  == 2020:
            print(striped_lines[i] * striped_lines[j])
            quit()
