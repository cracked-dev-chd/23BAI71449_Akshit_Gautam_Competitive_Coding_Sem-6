import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    ptr = 0
    t_cases = int(data[ptr])
    ptr += 1
    results = []
    
    for _ in range(t_cases):
        n = int(data[ptr])
        ptr += 1
        h = [int(x) for x in data[ptr : ptr + n]]
        ptr += n
        
        max_h = max(h)
        ans = float('inf')
        
        for target in [max_h, max_h + 1]:
            low = 0
            high = 10**18
            current_best = high
            
            total_need_ones = 0
            total_need_twos = 0
            for x in h:
                diff = target - x
                total_need_twos += diff // 2
                total_need_ones += diff % 2
            
            while low <= high:
                mid = (low + high) // 2
                
                avail_ones = (mid + 1) // 2
                avail_twos = mid // 2
                
                if total_need_ones > avail_ones:
                    low = mid + 1
                else:
                    rem_ones = avail_ones - total_need_ones
                    needed_from_ones = max(0, total_need_twos - avail_twos)
                    
                    if needed_from_ones * 2 <= rem_ones:
                        current_best = mid
                        high = mid - 1
                    else:
                        low = mid + 1
            
            if current_best < ans:
                ans = current_best
                
        results.append(str(ans))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()