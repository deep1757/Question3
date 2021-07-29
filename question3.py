for i in range(int(input())):
    n = int(input())
    a = list(map(int , input().split()))
    chk = n//2 +1
    flag =1
    if(n%2==1) and (a[0]==1):
        flag =0
        for i in range(chk-1):
            if(a[i] +1 != a[i+1]):
                    flag =1
                    break
            for i in range(chk-1,n-1):
                if(a[i] != a[i+1]+1):
                    flag =1
                    break
    print("yes" if flag ==0 else "no")