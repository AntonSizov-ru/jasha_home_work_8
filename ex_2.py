random_list = [19, 2, 31, 45, 6, 11, 121, 27]


def bubble_sort(nums):
    # по умолчанию от меньшего к большему
    swapped = True  # чтобы цикл запустился хотя один раз
    while swapped:
        swapped = False
        for i in range(len(random_list) - 1):
            if nums[i] < nums[i+1]:  
                nums[i], nums[i+1] = nums[i+1], nums[i]
                print(nums)
                swapped = True

print(random_list)

bubble_sort(random_list)



