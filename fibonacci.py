import time;


class Fibonnacci():
  def __init__(self, max = None): # si quiero parametros en constructor
    self.max = max;

  def __iter__(self):
    self.n1 = 0;
    self.n2 = 1;
    self.counter = 0;
    return self;

  def __next__(self):
    aux = self.n1 + self.n2;
    if not self.max or aux <= self.max:
      if self.counter == 0:
        self.counter += 1;
        return self.n1;
      elif self.counter == 1:
        self.counter += 1;
        return self.n2;
      else:
        # self.n1 = self.n2;
        # self.n2 = self.n1 + self.n2;
        self.counter += 1;
        self.n1, self.n2 = self.n2, aux;
        return aux;
    else:
      raise StopIteration;


def main():
  fibonnacci = Fibonnacci(1000);
  for element in fibonnacci:
    print(element);
    time.sleep(0.05); # pausar 0.05 antes de seguir a la siguiente vuelta


if __name__ == "__main__":
  main();

