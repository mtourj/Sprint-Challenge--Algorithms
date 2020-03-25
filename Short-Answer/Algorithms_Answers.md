#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
After analyzing this bit, it is clear the second line is the worst line,
where the while loop is defined, and it has a runtime complexity of n^3
because it loops n^3 times. That is the worst bit of that snippet so
that is the time complexity of that snippet


b)
This snippet contains a loop within a loop, where the outside loop has a
runtime complexity of O(n) because it loops n times, and the inner loop
has a runtime complexity of log(n) because the cursor is multiplied by 2
on each iteration and counts up to n. Therefore the runtime complexity of
this snippet would be classified O(n log n)


c)
This is a recursive function with one base case and calls itself no more
than once. This function would have a runtime complexity of O(n) because
the recursion depth of this function has a linear, direct relationship
with the input size

## Exercise II

Since I have got plenty of eggs, I will sacrifice of few to experiment
and find out what floor floor f is exactly. I would do this with a
binary search to minimize the number of eggs I drop. My pseudocode:

mid = floors // 2
start = 0
end = floors

'''The lowest floor that an egg last broke at'''
breaksAt = 0

while end > start:
  didBreak = throwEggFromFloor(mid)

  if didBreak:
      if mid < breaksAt:
          breaksAt = mid
      end = mid
  else:
      if mid - 1 == breaksAt
          return mid
      else:
          start = mid
  mid = (end - start) // 2