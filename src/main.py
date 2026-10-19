import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="[IP_ADDRESS]", port=8000, reload=True)

print(merge_sort([3,4,1,2,5]))
def merge_sort(list):
    if len(list) == 0:
        return list
    else:
        mid = len(list) // 2
        left = merge_sort(list[:mid])
        right = merge_sort(list[mid:])
        return merge(left, right)

def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])