strs=["eat","tea","tan","ate","nat","bat"]

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        for word in strs:
            a=" ".join(sorted(word))
            for b in a:
                index_map=defaultdict(list)
                for index,b in enumerate(a):
                    index_map[b].append(index)
                dup={}
                for item, idxs in index_map.items():
                    
                    dup[item] = idxs
                for c in dup.values():
                    for d in c:
                        e==d.sorted("")
        return word[d]

            


            
        