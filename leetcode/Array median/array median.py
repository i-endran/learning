"""
Finding median of two sorted arrays in O(m+n) time complexity.
"""

def find_median(arr: list[int], size: int):
    median: float = 0.0
    if size % 2 == 0:
        i = int(size / 2)
        median = (arr[i-1] + arr[i]) / 2
    else:
        i = int(size / 2)
        median = arr[i]

    return str(median)

nums1 = [-5]
nums2 = [5, 10, 15, 20]

m = len(nums1)
n = len(nums2)

# if m == 0:
#     print('Median: ' + find_median(nums2, n))
# if n == 0:
#     print('Median: ' + find_median(nums1, m))

no_of_loop: int = int((m+n)/2 + 1)

pointer_a, pointer_b = 0, 0
mem_1, mem_2 = 0, 0


for i in range(0, no_of_loop):
    val_a = nums1[pointer_a] if pointer_a < m else 10000000
    val_b = nums2[pointer_b] if pointer_b < n else 10000000

    if val_a <= val_b:
        mem_1 = mem_2
        mem_2 = nums1[pointer_a]

        pointer_a += 1
    else:
        mem_1 = mem_2
        mem_2 = nums2[pointer_b]

        pointer_b += 1

if (m+n) % 2 == 0:
    print('Median: ' + str((mem_1 + mem_2) / 2))
else:
    print('Median: ' + str(mem_2))

print('Test Median: ' + find_median(sorted(nums1 + nums2), m+n))