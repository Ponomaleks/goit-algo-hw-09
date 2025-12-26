## Conclusions

The experimental results confirm the theoretical differences between the greedy algorithm and the dynamic programming (DP) approach for the coin change problem.


*Testing coin change algorithms where greedy gives optimal result:*
```
{50: 2, 10: 1, 2: 1, 1: 1}
{50: 2, 10: 1, 2: 1, 1: 1}
```
*Testing coin change algorithms where greedy fails:*
```
{4: 1, 1: 2}
{3: 2}
```
*Benchmarking Greedy vs Dynamic Programming:*

| Change | Greedy Time (s) | DP Time (s) |
| ------ | --------------- | ----------- |
| 10     | 0.00000180      | 0.00001704  |
| 50     | 0.00000050      | 0.00003428  |
| 100    | 0.00000062      | 0.00010020  |
| 500    | 0.00000214      | 0.00045228  |
| 1000   | 0.00000438      | 0.00286628  |
| 5000   | 0.00004660      | 0.00571104  |
| 10000  | 0.00003908      | 0.00738322  |

1. **Correctness**
   - For canonical coin systems (e.g. `[50, 25, 10, 5, 2, 1]`), the greedy algorithm produces the same optimal result as the dynamic programming solution.
   - For non-canonical coin systems (e.g. `[4, 3, 1]`), the greedy algorithm may fail to find the optimal solution, while the dynamic programming algorithm always returns the minimum number of coins.

2. **Performance**
   - The greedy algorithm is significantly faster and scales very well with increasing change values.
   - The dynamic programming algorithm becomes noticeably slower as the change amount grows due to its `O(n × S)` time complexity, where `S` is the target sum.

3. **Practical Implications**
   - The greedy algorithm is preferable when working with canonical coin systems and large sums due to its superior performance and low memory usage.
   - Dynamic programming should be used when correctness is critical and the coin system is not guaranteed to be canonical, despite its higher computational cost.

Overall, the results demonstrate that the greedy algorithm offers excellent performance but limited applicability, while dynamic programming provides guaranteed optimality at the cost of higher time and memory consumption.
