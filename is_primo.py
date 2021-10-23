def is_prime(number: int) -> bool:
  primes = [2, 3, 4, 5, 7, 11];
  is_prime_list = [prime for prime in primes if number % prime == 0 and number != prime];
  return len(is_prime_list) == 0;


def main():
  your_number: int = int(input("Enter your number: "));
  print(is_prime(your_number));


if __name__ == "__main__":
  main();

