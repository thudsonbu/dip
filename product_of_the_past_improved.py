
def product(nums):
    # Generate before products
    before_products = []
    product = 1
    for num in nums:
        if before_products:
            before_products.append(num * before_products[-1])
        else:
            before_products.append(num)
        product = num * product
    print(before_products)

    # Generate after products
    after_products = []
    for num in reversed(nums):
        if after_products:
            after_products.append(num * after_products[-1])
        else:
            after_products.append(num)
    after_products = list(reversed(after_products))
    print(after_products)
    
    # Generate final array
    products = []
    for i in range(0, len(nums)):
        if i == 0:
            products.append(after_products[i])
        elif i == len(nums) - 1:
            products.append(before_products[i-1])
        else:
            products.append(before_products[i-1] * after_products[i+1])
    return products

print(product([1,2,3,4,5]))