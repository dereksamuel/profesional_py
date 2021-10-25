def printToUpper(my_func):
  def wrapper():
    print(my_func().upper());
  return wrapper


def welcome(func):
  def wrapper(*args, **kwargs):
    func_result: str = func(*args, **kwargs);
    if func_result:
      print("""

  👋👋👋   👋👋👋   👋👋👋👋👋
  👋👋👋   👋👋👋     👋👋👋
  👋👋👋|👋👋👋👋     👋👋👋
  👋👋👋|👋👋👋👋     👋👋👋
  👋👋👋   👋👋👋   👋👋👋👋👋

      """);
      print("welcome back 👋", func_result.upper());
  return wrapper;


@welcome
def byDerek(name = "Derek", lastname = "Paul"):
  return name + " " + lastname;


@welcome
def byJosh(name = "Joseph", lastname = "Bla"):
  print("will be a wellcome message to", name);
  return name + " " + lastname;


@printToUpper
def handleName():
  return "Hello";


def main():
  byDerek();
  byJosh("Other Name");
  handleName();


if __name__ == "__main__":
  main();

