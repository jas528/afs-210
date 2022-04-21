nlist=[55,31,26,20,63,7,51,74,81,40]
def mergeSort(nlist):
    mid = len(nlist)//2
    lefthalf = nlist[:mid]
    righthalf = nlist[mid:]
    if len(nlist)>1:
        print("Splitting",nlist)
        mergeSort(lefthalf)
        mergeSort(righthalf)
    merge(nlist,lefthalf,righthalf)

    print("Merging ",nlist)

def merge(nlist,lefthalf,righthalf):
    i=j=k=0
    while i <len (lefthalf) and j < len (righthalf):
        if lefthalf[i]< righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i <len (lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while  j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1   
        k=k+1
            
    return nlist

mergeSort(nlist)