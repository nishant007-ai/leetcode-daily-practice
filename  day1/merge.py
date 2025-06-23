

def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1

# Example usage
scores1 = [65, 70, 85, 0, 0, 0]
scores2 = [60, 80, 90]
merged_scores = merge(scores1, 3, scores2, 3)
print("Merged scores:", merged_scores)
