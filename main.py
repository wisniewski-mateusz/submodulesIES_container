from submodulesIES_submodule.is_it_prime import is_it_prime

def main():
    n = input('Number of prime numbers needed: ')
    error = 'You should provide an integer'
    assert n.isdigit(), error
    n = int(n)
    lower_bound = input('Number from which prime numbers should be searched for: ')
    assert lower_bound.isdigit(), error
    current_number = int(lower_bound)
    
    prime_numbers_displayed = 0
    while prime_numbers_displayed < n:
        if is_it_prime(current_number):
            print(current_number)
            prime_numbers_displayed += 1
        current_number += 1
    
if __name__ == '__main__':
    main()