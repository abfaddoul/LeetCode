class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s = ""
        for i in range(len(strs[0]), -1, -1):
            s = [strs[0][j] for j in range(i)]
            s = "".join(s)
            c = 1
            for st in strs:
                if not st.startswith(s):
                    c = 0
                    continue
            if c == 1:
                return s
        return s
