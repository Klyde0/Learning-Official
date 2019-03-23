def square_numbers(nums):
    result= []
    for i in nums:
        yield(i*i)
# yield word = generator

my_nums = square_numbers([1, 2, 3, 4, 5])

print(next(my_nums))
