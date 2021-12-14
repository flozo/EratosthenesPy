#!/usr/bin/env python3
"""Main file of Eratosthenes."""

# Import modules
import argparse
import time
import functions as fn
import sieves

# Define version string
version_num = '0.19'
version_dat = '2021-12-14'
version_str = '{} ({})'.format(version_num, version_dat)


def main():
    """Define argument parses, process arguments and call functions."""
    # Define argument parsers and subparsers
    parser = argparse.ArgumentParser(description='A program for testing '
                                     'implementations of the sieve of '
                                     'Eratosthenes. '
                                     '(https://github.com/flozo/Eratosthenes)')
    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s ' + version_str)
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='verbosity level (-v, -vv, -vvv): '
                        'default = single-line output, v = multi-line, '
                        'vv = detailed')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help=('disable terminal output (terminates all '
                              'verbosity)'))
    parser.add_argument('-p', '--progress', action='store_true',
                        help=('show progress bar'))
    parser.add_argument('-s', '--sievemethod', dest='sievemethod',
                        choices=('all', 'odd', '3k', '4k', '6k', 'list',
                                 'list-np', 'divisors'),
                        default='6k', help='sieve method')
    parser.add_argument('-d', '--divisormethod', choices=('all', 'sqrt'),
                        default='sqrt', help='divisor method')
    parser.add_argument('-a', '--auto-name', dest='autoname',
                        action='store_true',
                        help='generate name for output file automatically as '
                        '\'Eratosthenes_<limit>_<sievemethod>_<divisormethod>.'
                        'dat\' with path from [outfile]')
    parser.add_argument('limit', type=int, default=100,
                        help='upper limit of test range (a non-negative '
                        'integer)')
    parser.add_argument('outfile', nargs='?', help='write to file \'outfile\'')

    args = parser.parse_args()

    # Translate verbosity level
    verbosity = fn.verbosity_level(args)

    # Print argument list if -v, -vv, or -vvv
    if verbosity >= 1:
        print(args)

    # Translate progress option
    hide_progress = not(args.progress)

    # Select divisor method
    divisorfunc = fn.select_divisormethod(args)
    # Generate automatic filename
    outfile = fn.auto_filename(args, verbosity)
    # Define algorithm
    algorithm = sieves.Algorithm(args.divisormethod, args.sievemethod)
    # Make limit integer
    limit = int(args.limit)
    # Start timer
    start = time.process_time()
    # Determine prime numbers
    primes = fn.select_algorithm(algorithm, divisorfunc, limit, hide_progress,
                                 verbosity)
    # Stop timer
    elapsed = (time.process_time() - start)
    # Print result if -vv or -vvv
    if verbosity >= 2:
        print(primes)

    # Generate output
    title = 'Eratosthenes v{}'.format(version_str)
    header_width = len(title) // 3 * 3
    header_top = '# {0} {1} {0}\n'.format('*' * int(header_width // 3), title)
    header_closing = '# {}\n'.format('*' * (len(header_top) - 3))

    if algorithm.sievemethod != 'divisors':
        header = [
            ['Tested integer range', '[0, {}]'.format(limit)],
            ['Detected prime numbers', len(primes)],
            ['Applied sieve method', algorithm.sievemethod],
            ['Applied divisors method', algorithm.divisormethod],
            ['Progress bar active', str(args.progress)],
            ['Sifting time', '{:.9f} seconds'.format(elapsed)],
            ]
        if verbosity >= 0:
            print('[result] Detected {} prime numbers in {:.9f} '
                  'seconds.'.format(len(primes), elapsed))
        if outfile is not None:
            with open(outfile, 'w', encoding='UTF-8') as f:
                f.write(header_top)
                for item in header:
                    f.write('# {:<25} {:<25}\n'.format(item[0], item[1]))
                f.write(header_closing)
                for i in range(len(primes)):
                    f.write('{}\n'.format(primes[i]))
    else:
        header = [
            ['Integer range', '[0, {}]'.format(limit)],
            ['Applied divisors method', algorithm.divisormethod],
            ['Progress bar active', str(args.progress)],
            ['Time', '{:.9f} seconds'.format(elapsed)],
            ]
        if verbosity >= 0:
            print('Created divisor list in the rage [1, {}] in {:.9f} '
                  'seconds'.format(limit, elapsed))
        if outfile is not None:
            with open(outfile, 'w', encoding='UTF-8') as f:
                f.write(header_top)
                for item in header:
                    f.write('# {:<25} {:<25}\n'.format(item[0], item[1]))
                f.write(header_closing)
                f.write('# Number\tDivisors\n')
                for i in range(len(primes)):
                    f.write('{}\t{}\n'.format(primes[i][0], primes[i][1]))


if __name__ == '__main__':
    main()
