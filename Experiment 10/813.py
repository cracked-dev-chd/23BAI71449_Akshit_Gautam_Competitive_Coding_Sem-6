import sys
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    a = [int(x) for x in input_data[2:2+n]]
    
    q_ptr = 2 + n
    q_count = int(input_data[q_ptr])
    q_ptr += 1
    
    # If it doesn't exist, it defaults to 0.
    pos = {}
    prev_k = [0] * n
    for i in range(n):
        val = a[i]
        if val not in pos:
            pos[val] = []
        pos[val].append(i + 1)
        if len(pos[val]) > k:
            prev_k[i] = pos[val][-k-1]
    
 
    m_nodes = n * 45
    L = [0] * m_nodes
    R = [0] * m_nodes
    cnt = [0] * m_nodes
    roots = [0] * (n + 1)
    ptr = 1
 
    for i in range(n):
        val = prev_k[i]
        roots[i+1] = ptr
        curr = ptr
        prev = roots[i]
        ptr += 1
        
        low, high = 0, n
        while True:
            cnt[curr] = cnt[prev] + 1
            if low == high:
                break
            mid = (low + high) // 2
            if val <= mid:
                R[curr] = R[prev]
                L[curr] = ptr
                curr = L[curr]
                prev = L[prev]
                high = mid
            else:
                L[curr] = L[prev]
                R[curr] = ptr
                curr = R[curr]
                prev = R[prev]
                low = mid + 1
            ptr += 1
 
    
    last_ans = 0
    ans_list = []
    
    for _ in range(q_count):
        x = int(input_data[q_ptr])
        y = int(input_data[q_ptr+1])
        q_ptr += 2
        
        # Online decryption using the TRUE last_ans
        l = (x + last_ans) % n + 1
        r = (y + last_ans) % n + 1
        if l > r: 
            l, r = r, l
        
        
        res = 0
        node = roots[r]
        target = l - 1
        low, high = 0, n
        
        while node > 0:
            if high <= target:
                res += cnt[node]
                break
            mid = (low + high) // 2
            if target <= mid:
                node = L[node]
                high = mid
            else:
                res += cnt[L[node]]
                node = R[node]
                low = mid + 1
        
       
        last_ans = res - (l - 1)
        ans_list.append(str(last_ans))
        
    sys.stdout.write("\n".join(ans_list) + "\n")
 
if __name__ == "__main__":
    solve()