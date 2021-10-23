def is_palindrome(string: str) -> bool:
  stringStriped = string.strip().upper();
  return stringStriped[::-1] == stringStriped;


def main():
  palindromeInput = input("Please enter your text: ");
  print(is_palindrome(palindromeInput));


if __name__ == "__main__":
  main();

