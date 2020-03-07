def isColorful(nums):
    products = {}
    for subset in powerset(nums):
        currentProduct = reduce((lambda x, y: s * y), subset)
        if currentProduct in products:
            return False
        else:
            products[currentProduct] = True
    return True

def powerset(nums):
    all = [[]]
    for num in nums:
        all += [subset + [num] for subset in all]
    return all
