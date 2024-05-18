# https://leetcode.com/problems/goal-parser-interpretation/
class Solution:
    def interpret(self, command: str) -> str:
        out = ""
        i = 0
        while i <  len(command):
            if  command[i] == "(" and command[i + 1] == ")":
                out += "o"

            elif command[i] != "(" and command[i] != ")":
                out += command[i]
            i += 1
        return out