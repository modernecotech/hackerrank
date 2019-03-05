#find the runner up

if __name__ == '__main__':
    n = int(input())
    while not 2<=n<=10:
        print('please make sure that there are between 2 and 10 inputs')
        n = int(input())
    arr = map(int, input().split())
    newList=[]
    newList= [x for x in arr if -100<=x<=100]

rank_set=set([])

for result in(i for i in newList):
    rank_set.add(result)

print(sorted(rank_set)[len(rank_set)-2])
