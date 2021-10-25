import time;


def fibonacci(max = None):
  n1 = 0;
  n2 = 1;
  counter = 0;

  while True:
    aux = n1 + n2;
    if not max or aux <= max:
      if counter == 0:
        counter += 1;
        yield n1;
      elif counter == 1:
        counter += 1;
        yield n2;
      else:
        counter += 1;
        n1, n2 = n2, aux;
        yield aux;
    else:
      break;


def main():
  userInput: int = int(input("Enter your maximum number: "));
  fibo = fibonacci(userInput);
  for element in fibo:
    print(element);
    time.sleep(1);


if __name__ == "__main__":
  main();

