class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        while len(tokens) != 1:
            for ind,tok in enumerate(tokens):
                if str(tok) in '+-*/':
                    if tok == '+':
                        tmp = int(tokens[ind-2]) + int(tokens[ind-1])
                    elif tok == '-':
                        tmp = int(tokens[ind-2]) - int(tokens[ind-1])
                    elif tok == '*':
                        tmp = int(tokens[ind-2]) * int(tokens[ind-1])
                    elif tok == '/':
                        if int(tokens[ind-1])*int(tokens[ind-2]) >= 0:
                            tmp = int(tokens[ind-2]) / int(tokens[ind-1])
                        else:
                            d = lambda n,d:(n+d//2)//d
                            tmp = int(float(tokens[ind-2]) / float(tokens[ind-1]))
                    tok_update = tokens[:ind-2] + [tmp] + tokens[ind+1:]
                    break
            tokens = tok_update[:]
        return int(tokens[0])

a = Solution()
print a.evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"])
