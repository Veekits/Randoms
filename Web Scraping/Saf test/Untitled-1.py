def solution(A):
  """
  Finds the smallest positive integer not occurring in the array A.

  Args:
    A: An array of integers.

  Returns:
    The smallest positive integer not occurring in A.
  """

  # Use a set to efficiently track seen numbers.
  seen = set()

  # Iterate through the array and mark seen numbers.
  for num in A:
    if num > 0:
      seen.add(num)

  # Check for missing numbers from 1 to the length of the array + 1.
  for i in range(1, len(A) + 2):
    if i not in seen:
      return i

  # If no missing numbers are found, return 1.
  return 1

# Example usage
A = [1, 3, 6, 4, 1, 2]
missing_number = solution(A)
print(f"The smallest positive integer not occurring in A is: {missing_number}")
