"""def quartiles(arr):
    # Write your code here
    size=len(arr)
    arr1=sorted(arr)
    if size % 2 == 0:
        mid = int(size / 2)
        Q1 = arr1[0:mid]
        Q3 = arr1[mid:]

    else:
        mid = int(size / 2)
        Q1 = arr1[0:mid]
        Q3 = arr1[mid + 1:]


    def medi(arr):
        arr1 = sorted(arr)
        arr_len = len(arr1)

        if arr_len % 2 != 0:
            med = int(arr_len / 2)
            median = arr1[med]

        else:
            med1 = int(arr_len / 2)
            med2 = int(arr_len / 2) - 1
            median1 = arr1[med1]
            median2 = arr1[med2]
            median = (median1 + median2) / 2

        return int(median)

    median1 = (medi(Q1))
    median2 = (medi(arr1))
    median3 = (medi(Q3))
    output = [median1, median2, median3]
    return output



if __name__ == '__main__':
    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))
    res = quartiles(data)
    print(res)
"""


# #Q1,Q3 find
# size = 5
# arr = [9,5,7,1,3]
# arr1=sorted(arr)

# if size%2==0:
#     mid= int(size/2)
#     Q1=arr1[0:mid]
#     Q3=arr1[mid:]
# else:
#     mid = int(size / 2)
#     Q1=arr1[0:mid]
#     Q3=arr1[mid+1:]
# print(Q1)
# print(Q3)
    


"""
#standard deviation

import math

def stdDev(arr):
    sum_arr = sum(arr)
    len_arr = len(arr)
    mean = sum_arr / len_arr
    s_list = []

    for i in arr:
        square = (i - mean) ** 2
        s_list.append(square)

    sum_s = sum(s_list)
    std_deviation = math.sqrt(sum_s / len_arr)

    # Rounding the standard deviation to one decimal place
    rounded_std_dev = round(std_deviation, 1)

    print(rounded_std_dev)

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    stdDev(vals)
"""


# f=[5, 4, 3, 2, 1, 5]
# v=[6, 12, 8, 10, 20, 16]
# def make_list(vals, freqs):
#     # Print your answer to 1 decimal place within this function
#     dict1 = dict(zip(vals, freqs))
#     # print(dict1)
#     l1=[]
#     for key, values in dict1.items():
#         l1.extend([key]*values)
#     print(l1)
#     l2 =sorted(l1)   
#     return l2

# res = make_list(v, f)
# print(res)


# l2=[6, 6, 6, 6, 6, 8, 8, 8, 10, 10,  12, 12, 12, 12, 16, 16, 16, 16, 16, 20]
# size=len(l2)
# if size%2==0:
#     mid=int(size/2)
#     lh=l2[0:mid]
#     uh=l2[mid:]
# else:
#     mid=int(size/2)
#     lh=l2[0:mid]
#     uh=l2[mid+1:]

# def medi(arr):
#     arr1 = sorted(arr)
#     arr_len = len(arr1)

#     if arr_len % 2 != 0:
#         med = int(arr_len / 2)
#         median = arr1[med]

#     else:
#         med1 = int(arr_len / 2)
#         med2 = int(arr_len / 2) - 1
#         median1 = arr1[med1]
#         median2 = arr1[med2]
#         median = (median1 + median2) / 2

#     return median

# q1=medi(lh)
# print(q1)
# q3=medi(uh)
# print(q3)

# print(q3-q1)



def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    dict1=dict(zip(values,freqs))
    l1=[]
    for key,values in dict1.items():
        l1.extend([key]*values)
    l2=sorted(l1)
    size=len(l2)
    if size%2==0:
        mid=int(size/2)
        lh=l2[0:mid]
        uh=l2[mid:]
    else:
        mid=int(size/2)
        lh=l2[0:mid]
        uh=l2[mid+1:]

    def medi(arr):
        arr1 = sorted(arr)
        arr_len = len(arr1)

        if arr_len % 2 != 0:
            med = int(arr_len / 2)
            median = arr1[med]

        else:
            med1 = int(arr_len / 2)
            med2 = int(arr_len / 2) - 1
            median1 = arr1[med1]
            median2 = arr1[med2]
            median = (median1 + median2) / 2

        return median

    q1=medi(lh)
    q3=medi(uh)

    print(round(q3-q1,1))
    # print("{:.1f}".format(q3 - q1))


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
    
