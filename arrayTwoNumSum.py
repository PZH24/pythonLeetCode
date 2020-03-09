"""
处理数组中的两个和
例子：
    array = [2,3,4,5],target=5
    print [2,3]
    求输出坐标
"""


def twoSum(array_num, target_sum):
    """使用暴力解决办法，循环
        时间复杂度：两层 for 循环，O（n²）
        空间复杂度：O（1）
    """
    max_len = len(array_num)
    result = []
    for i in range(max_len):
        start = array_num[i]
        j = i + 1
        if j < max_len:
            for j in range(j, max_len):
                end = array_num[j]
                if (start + end) == target_sum:
                    dic = [i, j]
                    result.append(dic)
                    break
    print("结果是:" + str(result))


def twoSumByDict(array_num, target_sum):
    """通过字典 key的唯一性进行处理
    时间复杂度 o(n)
    网上答案
    """
    dic = {}
    max_len = len(array_num)
    for i in range(max_len):
        sub = target_sum - array_num[i]
        if sub in dic:
            print([i, dic.get(sub)])
        dic[array_num[i]] = i
    print(dic)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 9, 6, 7, 8, 11]
    target = 15
    # twoSum(array, target)
    twoSumByDict(array, target)
