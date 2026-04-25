import sys

def solve():
    tokens = sys.stdin.read().split()
    if len(tokens) <= 1:
        return
    
    n = int(tokens[0])
    tokens = tokens[1:]
    
    res = []
    stack = []
    
    for token in tokens:
        if res and not stack:
            print("Error occurred")
            return
            
        if stack:
            if stack[-1] == 1:
                res.append(",")
            stack[-1] -= 1
            
        if token == "pair":
            res.append("pair<")
            stack.append(2)
        else:
            res.append("int")
            while stack and stack[-1] == 0:
                stack.pop()
                res.append(">")
                
    if stack or not res:
        print("Error occurred")
    else:
        sys.stdout.write("".join(res) + "\n")

if __name__ == "__main__":
    solve()