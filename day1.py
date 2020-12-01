with open('day1_input.txt','r') as f:
    data = f.read()

data = [int(i) for i in data.split()]
def first_problem(data):
    for i in data:
        for j in data:
            if i + j == 2020:
                print(i*j)
                break
  
def second_problem(data):
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    print(i*j*k)
                    break

if __name__ == '__main__':
    first_problem(data)
    second_problem(data)
