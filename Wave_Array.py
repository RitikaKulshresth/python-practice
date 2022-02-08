def wave_array(arr):
    for i in range(0,len(arr)-1):
        if i%2!=0:
            if arr[i]>arr[i+1] :
                arr[i],arr[i+1]=arr[i+1],arr[i]   
        else:
            if arr[i+1]>arr[i]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

arr=[2,4,7,8,9,10]
print(wave_array(arr))