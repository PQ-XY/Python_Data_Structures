"""
File: fib.py
"""
"""
Yao Xu
6/13/2025

This program calculates fibonacci series up to n using three methods -- recursion, linear algorithm and memorization. 
In the main function, the three functions were tested and also evaluated by calls/iterations.

The time complexity of the recursiveFib function is O(2^n).
    Because if we draw the recursion tree of the function, you get below diagram:
                                    f(n)                              2^0
                                       
                               f(n-1)    f(n-2)                       2^1
                                           
                        f(n-2)  f(n-3)  f(n-3)  f(n-4)                2^2
                                     .......
                        f(1)  f(0)                                    2^(n-1)
                        
    the total time complexity is O(2^0 + 2^1 + ... + 2^(n-1)) = O(2^n)
    
The time complexity of the memorizedFib function is O(n).
    Since we have the memorization so each distinct k in n is only calculated once. So for n, it will calculate n times.
    
The time complexity of the linearFib function is O(n).
    In the linearFib function, we have have a loop with n iterations. Although within each iteration, we have done 5 steps, 
    but time complexity wise, it will be O(5n) = O(n).
"""

from counter import Counter

def recursiveFib(n, counter):
    """The recursive fibonacci function."""
    counter.increment()
    if n < 3:
        return 1
    else:
        return recursiveFib(n - 1, counter) + recursiveFib(n - 2, counter)

def memoizedFib(n, counter, dict = {}):
    """
    The recursive fibonacci memoized function.
    In this function, we introduced a dictionary to help us keep track of the calculated result so in each call, we just
    need to check if the result is already in the dictionary. In this way, we don't do redundant calculations.
    Input:
        n: integer, counter: class instance, dict: dictionary
    Output:
        int: the nth Fibonacci number.
    """
    counter.increment()

    if n in dict:
        return dict[n]

    if n < 3:
        dict[n] = 1
    else:
       dict[n] = memoizedFib(n - 1, counter, dict) + memoizedFib(n - 2, counter, dict)

    return dict[n]
    
def linearFib(n, counter):
    """Linear fibonacci function."""
    sum = 1
    first = 1
    second = 1
    count = 3
    while count <= n:
        counter.increment()
        sum = first + second
        first = second
        second = sum
        count += 1
    return sum

def test(fib_function, flag=False):
    """
    Input:
        function to be tested
        flag: boolean (to control the extra argument just for memorizedFib())
    Output:
        result follow below template (you will have numbers of calls or iterations in
        place of the *s)

            name of the function:
            n         fib    calls/iterations
            2           1                   *
            4           3                   *
            8          21                   *
            16         987                  *
            32     2178309                  *
    """
    problemSize = 2
    callsCount = Counter()
    print(f"\n{fib_function.__name__}:")
    print("%4s%12s%20s" % ("n", "fib", "calls/iterations"))
    for count in range(5):
        if flag:
            result = fib_function(problemSize, callsCount, {})
        else:
            result = fib_function(problemSize, callsCount)
        print("%4d%12d%20s" % (problemSize,result, callsCount))
        problemSize *= 2
        callsCount.reset()

def main():
    """
    Tests the recursive fibonacci function with some powers of 2.

    Used a test() helper function to reduce the redundant codes.
    """
    test(recursiveFib)
    test(memoizedFib, flag=True)
    test(linearFib)

if __name__ == "__main__":
    main()
