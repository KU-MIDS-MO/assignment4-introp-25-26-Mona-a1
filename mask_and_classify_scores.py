import numpy as np

arr = np.array([
    [-10,  20,  50, 110],
    [ 40,  69,  70, 101],
    [  0,  39,  -41,  80],
    [ -55,  60,  95, -200]
])

def mask_and_classify_scores(arr):

    
    if isinstance(arr, np.ndarray) == False:
        return None
    
    n = len(arr[0])   

    if arr.shape != (n,n):
        return None

    if n < 4:
        return None


# Part B; A Cleaning scores

    cleaned = arr.copy()
    
    
    for m in range(0,n):
        
        for i in range(0,n):
            if cleaned[m,i] < 0:
                cleaned[m,i] = 0
            
            if cleaned[m,i] > 100:
                cleaned[m,i] = 100
    
# Part B; classifying scores

    levels = np.ones((n,n), dtype=int) 
    
    for m in range(0,n):
            
        for i in range(0,n):
            if cleaned[m,i] < 40:
                levels[m,i] = 0
    
            if 40 <= cleaned[m,i] < 70:
                levels[m,i] = 1

            if cleaned[m,i] >= 70:
                levels[m,i] = 2





# Part C; counting passing scores per row

    row_pass_counts = np.zeros((n), dtype=int) 

    p = 0    

    for m in range(0,n):
        for i in range(0,n):
            if cleaned[m,i] >= 50:
                row_pass_counts[p] = row_pass_counts[p] + 1
                        
        p = p + 1






    return cleaned, levels, row_pass_counts

    pass
    ### Replace with your own code (end)   ###
print(mask_and_classify_scores(arr))