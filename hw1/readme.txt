Names: Srimaan Sridharan, Adit Dasgupta
References: Lecture 1 and Lecture 2 slides
Notes: No abnormal errors or warnings
Answers:
    1.  The results strongly agree with the distinction. If we take the test case of 837062415, both 
    UCS and all three variants of A* found cost = 616 with length = 24. On 182043765, both found 
    cost = 511 with length = 22. This held true without exception across all puzzles tested. On 837062415,
    greedy-h1 found a cost of 1,525 (2.5x more expensive than optimal) with a length of 60. greedy-h2
    finds a cost of 1280 with a length of 44. greedy-h3 managed to find the optimal solution, but this
    is not always the case. On 482173605, the optimal solution found by UCS and all A* variants is
    length = 16 with cost = 488. greedy-h3 found length = 122 and cost = 2122, nearly 4x worse.
    BFS and Greedy show clear suboptimality. On 182043765, BFS found the same path length of 22 as UCS 
    and A*. However, BFS found a more expensive path cost of 613 compared to UCS's and A*'s cost of 511.
    This shows that BFS optimizes for shortest path, not lowest cost. The tradeoff between UCS and A* vs
    UCS and Greedy is efficiency. greedy-h3 only expands 43 states on 837062415 vs astar-h3's 562 but at
    the cost of optimality. UCS and all A* variants will always find the most optimal solution, but must
    explore more states to guarantee it.

    2. Based of the start state 837062415, UCS expands the most states at 156,595. This is because UCS
    has no heuristic to base its search. It explores outwards in all directions by cost. This expands
    an incredibly large number of states before finding the solution. Greedy-h3 processes the least
    states at 43. Greedy inherently ignores path cost and "charges" towards the state that looks closest
    to its goal. This makes it extremely fast but it completely shirks cost. On this game it got lucky
    but as mentioned previously, it finds suboptimal solutions for others.

    3. The choice of heuristic greatly affects the performance of A*. On the state 837062415:
    - astar-h1: length = 24, cost = 616, frontier = 182,642, expanded = 152,907
    - astar-h2: length = 24, cost = 616, frontier = 179,398, expanded = 149,201
    - astar-h3: length = 24, cost = 616, frontier = 901, expanded = 562
    h1 and h2 perform similarly and barely better than UCS (156,595 expanded). h3 expands only 562 states,
    which is over 272x fewer than h1. This is due to how informed each heuristic is. h1 only counts misplaced
    tiles and treating each move with equal cost. h2's Manhattan distance considers the distance of each tile
    from its current position to its goal position. h3 multiplies each tile's Manhattan distance by its tile^2.
    This accounts for the weighted transition cost of each tile. h3 is the most accurate estimate of remaining
    cost, so A* wastes the fewest moves.
