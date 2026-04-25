import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    base1, mod1 = 5, 10**15 + 7
    base2, mod2 = 7, 10**15 + 9
    
    def get_hashes(s):
        h1, h2 = 0, 0
        for char in s:
            val = ord(char) - ord('a') + 1
            h1 = (h1 * base1 + val) % mod1
            h2 = (h2 * base2 + val) % mod2
        return (h1, h2)

    known_hashes = set()
    idx = 2
    for _ in range(n):
        known_hashes.add(get_hashes(input_data[idx]))
        idx += 1
        
    results = []
    for _ in range(m):
        s = input_data[idx]
        idx += 1
        h1, h2 = get_hashes(s)
        found = False
        
        p1, p2 = 1, 1
        for i in range(len(s) - 1, -1, -1):
            curr_val = ord(s[i]) - ord('a') + 1
            
            for v in [1, 2, 3]:
                if v == curr_val:
                    continue
                
                diff = v - curr_val
                nh1 = (h1 + diff * p1) % mod1
                nh2 = (h2 + diff * p2) % mod2
                
                if (nh1, nh2) in known_hashes:
                    found = True
                    break
            
            if found: break
            p1 = (p1 * base1) % mod1
            p2 = (p2 * base2) % mod2
            
        results.append("YES" if found else "NO")
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()