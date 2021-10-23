from datetime import datetime;

def execution_time(my_funct):
  def wrapper(*args, **kwargs):
    initial_time = datetime.now();
    my_funct(*args, **kwargs);
    final_time = datetime.now();
    time_elapsed = final_time - initial_time;
    print("Pasaron", str(time_elapsed.total_seconds()), "seconds");
  return wrapper;


@execution_time
def random_func():
  for _ in range(1, 10000000):
    pass;


@execution_time
def suma(a: int, b: int) -> int:
  return a + b;


def main():
  suma(1, 2);
  random_func();


if __name__ == "__main__":
  main();

