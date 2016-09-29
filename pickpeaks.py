def pick_peaks(arr):
    output = {'pos' : [], 'peaks' : []}
    if len(arr) > 2:
        ind = None
        for i in range(len(arr)):
            if arr[i] > arr[i-1]:
                ind = i
            elif arr[i] < arr[i-1] and ind:
                output['pos'].append(ind)
                output['peaks'].append(arr[ind])
                ind = None
    return output
