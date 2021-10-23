def is_palindrome(string):
  return string[::-1] == string;


def main():
  palindromeInput = input("Please enter your text: ");
  print(is_palindrome(palindromeInput));


if __name__ == "__main__":
  main();

