
def merge_sort(A:list, B:list):
    def is_sorted(lst):
        if lst == []: return True
        last_num = lst[0]
        for x in lst:
            if x < last_num: return False
            last_num = x
        return True
    i = 0
    j = 0
    C = []
    if not is_sorted(A):
        mid = len(A) // 2
        A = merge_sort(A[:mid], A[mid:])
    if not is_sorted(B):
        mid = len(B) // 2
        B = merge_sort(B[:mid], B[mid:])
    while (i < len(A) and j < len(B)):
        if A[i] < B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1
    if i==len(A):
        C.extend(B[j:])
    elif j==len(B):
        C.extend(A[i:])
    return C



