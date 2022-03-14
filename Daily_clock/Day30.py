# 2022-3-14 599 两个列表的最小索引总和
"""
假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。
"""


class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        findex = {list1[i]: i for i in range(len(list1))}
        sindex = {list2[i]: i for i in range(len(list2))}
        common = set(list2) & set(list1)
        sumofindex = {j: findex[j] + sindex[j] for j in common}
        return [k for k in common if sumofindex[k] == min(sumofindex.values())]
