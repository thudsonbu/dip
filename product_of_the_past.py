def products(nums):
    # variables
    product = 1
    current = 1
    new_array = []
    # Calculate total product
    for position in range(0, len(nums)):
        product = 1
        for i in range(0, len(nums)):
            if i != position:
                product = product * nums[i]
        new_array.append(product)
    return new_array

print(products([1,2,3,4,5]))

