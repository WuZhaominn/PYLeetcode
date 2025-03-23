class Node:
    __slots__ = 'son', 'end'

    def __init__(self):
        self.son = {}   # 子节点字典，键为字符，值为子节点
        self.end = False  # 标记当前节点是否为某个单词的结尾

class Trie:
    def __init__(self):
        self.root = Node()  # 初始化根节点

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()    # 如果字符不存在，创建新节点
            cur = cur.son[c]   # 移动到子节点
        cur.end = True   # 标记单词结尾

    def find(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.son:
                return 0   # 字符不存在，返回 0
            cur = cur.son[c]   # 移动到子节点
        return 2 if cur.end else 1   # 判断是否单词结尾，0：单词或前缀不存在1：前缀存在，但不是完整单词。2：完整单词存在
#判断单词是否存在于 Trie 树中。
    def search(self, word: str) -> bool:
        
        return self.find(word) == 2
#判断是否存在以给定前缀开头的单词。

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) != 0
