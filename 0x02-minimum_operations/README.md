# MinOperations project

## Flowchart of Solution
```bash
                    +------------------+
                    |  Start function  |
                    +------------------+
                             |
                             v
                    +--------------------+
                    | Set min_operations |
                    |      to zero       |
                    +--------------------+
                            |
                            v
                    +------------------+
                    | Check if n <= 1  |
                    +------------------+
                            |
                            v
            +--+<---+ If true, return 0
            |  |
            |  v
+-------------+-------------+
|   For i in range(2, n+1)  |
+---------------------------+
            |  |
            |  v
     +------+----------+
     | Check if n is   |
     | divisible by i  |
     +------+----------+
            |  |
            v  |
     +------+-----------+
     | Divide n by i    |
     | and add i to the |
     | total            |
     +------+-----------+
            |  |
            v  |
     +------+-----------+
     | Continue to      |
     | divide n by i    |
     | until n is no    |
     | longer divisible |
     | by i             |
     +------+-----------+
            |  |
            v  |
+-----------+--+-----------+
| Return min_operations    |
+--------------------------+
```
- ok bye
