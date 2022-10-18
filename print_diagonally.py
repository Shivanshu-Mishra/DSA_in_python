#User function Template for python3

def downwardDigonal(N, A):
    elements=[]
    for i in range(0,N):
        row=0
        col=i
        while(row<=i):
            elements.append(A[row][col])
            row+=1
            col-=1
    for i in range(1,N):
        row=i
        col=N-1
        while(row<N):
            elements.append(A[row][col])
            row+=1
            col-=1
    return elements


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends