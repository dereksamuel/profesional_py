def main():
  set1 = set([1, 2, 3, 4, 5]);
  set2 = set([5, 6, 7, 8, 9]);

  union = set1 | set2;
  intersection = set1 & set2;
  difference = set1 - set2;
  difference2 = set2 - set1;
  symmetric_difference = set1 ^ set2;

  print(union, intersection, difference, symmetric_difference, difference2);


if __name__ == "__main__":
  main();
  print(f"Name: {__name__}");

