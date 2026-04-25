import sys
 
def solve():
  
    input = sys.stdin.read().split()
    if not input:
        return
    
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    
    results = []
    
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = [int(x) for x in input[ptr : ptr + n]]
        ptr += n
        
      
        counts = [0] * (n + 1)
        for x in a:
            counts[x] += 1
            
        special_count = 0
        is_special = [False] * (n + 1)
        
       
        for i in range(n):
            current_sum = a[i]
            for j in range(i + 1, n):
                current_sum += a[j]
                
                
                if current_sum > n:
                    break
                
              
                is_special[current_sum] = True
        
        
        total_special = 0
        for val in range(1, n + 1):
            if is_special[val]:
                total_special += counts[val]
                
        results.append(str(total_special))
    
    sys.stdout.write("\n".join(results) + "\n")
 
if __name__ == "__main__":
    solve()