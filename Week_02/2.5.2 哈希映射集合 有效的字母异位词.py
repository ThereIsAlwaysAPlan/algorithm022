
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 暴力 O(nlogn)
        # return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)

        # hashtable
        if len(s) != len(t) : return False
        l = [0] * 26
        for i in range(len(s)):
            l[ord(s[i])-ord('a')] += 1
            l[ord(t[i])-ord('a')] -= 1
        for i in l:
            if i != 0:
                return False
        return True

if __name__ == "__main__":
    s = 'anagram'
    t = 'nagaram'
    print(Solution().isAnagram(s,t))