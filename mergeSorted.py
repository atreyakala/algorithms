def merge(nums1, m, num2, n):
    pos1 = m + n - 1
    pos2 = n - 1
    writeIdx = m - 1
    while pos1 >= 0 and pos2 >= 0:
        num1 = nums1[pos1]
        num2 = nums2[pos2]
        if num1 > num2:
            nums1[writeIdx] = num1
            pos1 -= 1
        else:
            nums1[writeIdx] = num2
            pos2 -= 1
        writeIdx -= 1
    while pos2 >= 0:
        nums1[writeIdx] = nums2[pos2]
        pos2 -= 1
        writeIdx -= 1
