if __name__ == '__main__':
    python_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name,score]) 

unique_result_set=set([])
for result in(i[1] for i in python_students):
    unique_result_set.add(result)
    

sorted_unique_result_list=sorted(unique_result_set)

res=[inner for inner in python_students if inner[1]==sorted_unique_result_list[1]]
res.sort()
for row in res:
    del row[1]

for s in res:
    print(*s)