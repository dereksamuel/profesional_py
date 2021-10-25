def deleteRepeats(some_list):
  without_duplicates = [];

  for element in some_list:
    if element not in without_duplicates:
      without_duplicates.append(element);

  return without_duplicates;


def to_set(func):
  def wrapper(*args, **kwargs):
    result = set(func(*args, **kwargs));
    print(result);
    return result;
  return wrapper;


@to_set
def setter_example(any_list):
  return any_list;


def main():
  print(deleteRepeats([1, 1, 1, 1, 1, 55, 55, 2, 2, 3, 8, 9]));
  setter_example([1, 1, 1, 1, 1, 55, 55, 2, 2, 3, 8, 9]);


if __name__ == "__main__":
  main();

