import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = []
    b = []
    idx = 1
    for _ in range(n):
        a.append(int(input_data[idx]))
        b.append(int(input_data[idx+1]))
        idx += 2
    
    sum_b = sum(b)
    max_a = sum(a)
    
    dp = [[-1] * (max_a + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    current_max_s = 0
    for i in range(n):
        ca = a[i]
        cb = b[i]
        for k in range(i, -1, -1):
            row_k = dp[k]
            row_k1 = dp[k+1]
            for s in range(current_max_s, -1, -1):
                if row_k[s] != -1:
                    if row_k[s] + cb > row_k1[s + ca]:
                        row_k1[s + ca] = row_k[s] + cb
        current_max_s += ca
    
    results = []
    for k in range(1, n + 1):
        best = 0.0
        row_k = dp[k]
        for s in range(max_a + 1):
            if row_k[s] != -1:
                val = min(float(s), (row_k[s] + sum_b) / 2.0)
                if val > best:
                    best = val
        results.append(f"{best:.10f}")
        
    sys.stdout.write(" ".join(results) + "\n")

if __name__ == "__main__":
    solve()