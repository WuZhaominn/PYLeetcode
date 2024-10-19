class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0
        max_len = 0
        hashSet = set()
        for right in range(len(s)):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left+=1
            hashSet.add(s[right])
            max_len = max(max_len,right-left+1)
        return max_len

在 Python 中，哈希集合（set）和哈希表（通常指 dict 字典）都是基于哈希函数实现的数据结构，但它们的功能和用法有所不同。
1. 哈希集合（set）
定义：集合是一个无序的、元素不重复的容器。
存储机制：集合使用哈希函数对元素进行哈希映射来快速查找、添加和删除元素。
特点：
只包含唯一的元素，无法存储重复的值。
元素无序，不能通过索引访问。
常用于检查某个元素是否存在（时间复杂度为 O(1)）。
主要操作：添加、删除、查找。

2. 哈希表（dict）
定义：字典是一种键值对（key-value pair）结构的映射数据类型。
存储机制：字典使用哈希函数来快速查找键，并且每个键对应一个值。
特点：
每个键必须是唯一的，值可以重复。
键值对是无序的（Python 3.7+ 后，字典保留了插入顺序，但这不影响其哈希表的本质）。
常用于根据键快速查找对应的值（时间复杂度为 O(1)）。
主要操作：插入、删除、查找键值对。



区别：
数据存储形式：

set 只存储元素，不存储额外信息（如键和值的对应关系）。
dict 存储的是键值对，每个键关联一个值。
用途：

set：主要用于元素的去重或快速判断元素是否存在。
dict：主要用于根据键快速查找、插入和删除对应的值。
存储限制：

set：只能存储元素，不能存储映射关系。
dict：既存储键，也存储值，每个键对应一个值。
内部实现：

set：基于哈希函数，实现类似一个只存储键的哈希表。
dict：基于哈希函数，实现一个完整的键值对映射。
