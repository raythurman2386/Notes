"""
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

To find  all the prime numbers less than or equal to a given integer `n` by Eratosthenes method:
  1. Create a list of consecutive integers from 2 through n
  2. Initially let p equal 2, the smallest prime number
  3. Enumerate the multiples of `p` by counting in increments of p from 2p to n, and mark them in the list
  4. Find the first number greater than p in the list that is not marked. If there is no number stop
    otherwise, let p now equal this new number (which is the next prime), repeat from step 3
  5. When the algorithm terminnates, the numbers remaining not marked in the list are all the primes below n
"""


def main():
    num = int(input("Find prime numbers up to number: "))
    # num = 30
    starting_num = 2
    list = [num for num in range(starting_num, num + 1)]

    while starting_num * starting_num <= num:
        for num in list:
            if num % starting_num == 0 and not num == 2:
                list.remove(num)

        starting_num += 1

    print(list)


if __name__ == '__main__':
    main()
