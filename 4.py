if __name__ == '__main__':
    n = int(input())
    while not 2<=n<=10:
        print('please make sure that there are between 2 and 10 inputs')
        n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        newList= [x for x in scores if 0<=x<=100]
        student_marks[name] = newList
    query_name = input()
    div = len(student_marks[query_name])
    print ("{0:.2f}".format(sum(student_marks[query_name])/div))