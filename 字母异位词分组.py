class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        hash={}
        for s in strs:
            key = self.hash_key(s)
            try:
                hash[key].append(s)
            except KeyError:
                hash[key]=[s]
        return list(hash.values()) 

    def hash_key(self,s):
        table =[0]* 26
        for ch in s:
            index=ord(ch)-ord('a')
            table[index]+=1
        return str(table)
