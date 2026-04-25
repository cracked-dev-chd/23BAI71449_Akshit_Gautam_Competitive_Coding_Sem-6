import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    events = []
    
    idx = 1
    for _ in range(n):
        l = int(data[idx])
        r = int(data[idx+1])
        events.append((l, 1))
        events.append((r + 1, -1))
        idx += 2
    
    events.sort()
    
    ans = [0] * (n + 1)
    current_coverage = 0
    
    for i in range(len(events) - 1):
        current_coverage += events[i][1]
        length = events[i+1][0] - events[i][0]
        if current_coverage > 0:
            ans[current_coverage] += length
            
    print(*(ans[1:]))

if __name__ == "__main__":
    solve()