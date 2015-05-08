# Problem 83 -- Path sum: four ways

Find mimimal path sum of a matrix when moving to from the top left to
bottom write.

## Instructions

1. Clone git repository onto local machine
2. 'cd' into 'prob83' directory
3. Find the minimal path sum of matrix in text file with command using UCS (empirically verified as faster):

    '''
    python min_cost_path.py path_to_matrix_file
    '''

    or

    Test the code against simple test matrices with the command:
    '''
    python min_cost_path.py --test
    '''
    
## Performance of UCS vs. A*

###A*

404650 function calls in 0.278 seconds

Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.278    0.278 <string>:1(<module>)
    12641    0.026    0.000    0.076    0.000 Queue.py:107(put)
    12639    0.028    0.000    0.092    0.000 Queue.py:150(get)
        1    0.000    0.000    0.000    0.000 Queue.py:218(_init)
    25278    0.009    0.000    0.012    0.000 Queue.py:221(_qsize)
    12641    0.007    0.000    0.013    0.000 Queue.py:224(_put)
    12639    0.004    0.000    0.023    0.000 Queue.py:227(_get)
        1    0.000    0.000    0.000    0.000 Queue.py:26(__init__)
    12639    0.015    0.000    0.028    0.000 Queue.py:93(empty)
    12641    0.010    0.000    0.013    0.000 min_cost_path.py:25(manhattan_distance)
    12641    0.006    0.000    0.019    0.000 min_cost_path.py:29(get_min_possible_cost)
    6399    0.015    0.000    0.019    0.000 min_cost_path.py:32(get_neighbor_points)
        1    0.043    0.043    0.277    0.277 min_cost_path.py:44(A_star)
        3    0.000    0.000    0.000    0.000 threading.py:241(Condition)
        3    0.000    0.000    0.000    0.000 threading.py:259(__init__)
    25280    0.013    0.000    0.023    0.000 threading.py:299(_is_owned)
    25280    0.028    0.000    0.057    0.000 threading.py:372(notify)
        3    0.000    0.000    0.000    0.000 threading.py:58(__init__)
    25280    0.006    0.000    0.006    0.000 threading.py:63(_note)
    12639    0.019    0.000    0.019    0.000 {_heapq.heappop}
    12641    0.007    0.000    0.007    0.000 {_heapq.heappush}
    25282    0.003    0.000    0.003    0.000 {abs}
    25280    0.003    0.000    0.003    0.000 {len}
    63199    0.023    0.000    0.023    0.000 {method 'acquire' of 'thread.lock' objects}
    6399    0.002    0.000    0.002    0.000 {method 'add' of 'set' objects}
    25278    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    37919    0.011    0.000    0.011    0.000 {method 'release' of 'thread.lock' objects}
        1    0.000    0.000    0.000    0.000 {thread.allocate_lock}

### UCS

354086 function calls in 0.246 seconds

Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.246    0.246 <string>:1(<module>)
    12641    0.025    0.000    0.074    0.000 Queue.py:107(put)
    12639    0.027    0.000    0.088    0.000 Queue.py:150(get)
        1    0.000    0.000    0.000    0.000 Queue.py:218(_init)
    25278    0.008    0.000    0.011    0.000 Queue.py:221(_qsize)
    12641    0.006    0.000    0.013    0.000 Queue.py:224(_put)
    12639    0.004    0.000    0.023    0.000 Queue.py:227(_get)
        1    0.000    0.000    0.000    0.000 Queue.py:26(__init__)
    12639    0.015    0.000    0.028    0.000 Queue.py:93(empty)
    6399    0.015    0.000    0.018    0.000 min_cost_path.py:32(get_neighbor_points)
        1    0.037    0.037    0.246    0.246 min_cost_path.py:67(uniform_cost_search)
        3    0.000    0.000    0.000    0.000 threading.py:241(Condition)
        3    0.000    0.000    0.000    0.000 threading.py:259(__init__)
    25280    0.013    0.000    0.022    0.000 threading.py:299(_is_owned)
    25280    0.026    0.000    0.054    0.000 threading.py:372(notify)
        3    0.000    0.000    0.000    0.000 threading.py:58(__init__)
    25280    0.005    0.000    0.005    0.000 threading.py:63(_note)
    12639    0.019    0.000    0.019    0.000 {_heapq.heappop}
    12641    0.007    0.000    0.007    0.000 {_heapq.heappush}
    25280    0.003    0.000    0.003    0.000 {len}
    63199    0.021    0.000    0.021    0.000 {method 'acquire' of 'thread.lock' objects}
    6399    0.002    0.000    0.002    0.000 {method 'add' of 'set' objects}
    25278    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    37919    0.010    0.000    0.010    0.000 {method 'release' of 'thread.lock' objects}
        1    0.000    0.000    0.000    0.000 {thread.allocate_lock}


