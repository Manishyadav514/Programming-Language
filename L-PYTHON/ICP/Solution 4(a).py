def swap(arr,x,y):
    arr[x],arr[y]=arr[y],arr[x]
arr=[30,10,3,5,100,1,25,29,90,26]

def partition(arr,left,right):
    if arr[0] > arr[1]:
        swap(arr, 1, 0)
    p1=arr[left]
    p2=arr[right]
    wall=0
    for i in range(wall,len(arr)):
        if arr[i]<p1:
            swap(arr,wall,i)
            wall=wall+1

    for i in range(wall,len(arr)):
        if arr[i]<p2:
            swap(arr,wall,i)
            wall=wall+1
    print(arr)


#TO PRINT THE NUMBER IN ORDER OF X<P1,P1<X,P2,P2<X
partition(arr,0,1)