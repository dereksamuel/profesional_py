def made_repeator_of(n: int):
  def repeater(string: str) -> str:
    assert type(string) == str, "You can only strings";
    return string * n;
  return repeater;


def make_division_by(n: int):
  return lambda numberMayor: int(numberMayor / n);


def main():
  x = make_division_by(18);
  repeat_by_5 = made_repeator_of(5);
  print(repeat_by_5("Derek Hola, "));

  repeat_by_10 = made_repeator_of(10);
  print(repeat_by_10("Derek 10, "));
  print(x(54));


if __name__ == "__main__":
  main();

