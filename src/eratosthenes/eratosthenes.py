#!/usr/bin/env python3
"""Main file of Eratosthenes."""

# Import modules
import argparse
import time
import os
import sieves

# Define version string
version_num = '0.18'
version_dat = '2021-08-21'
version_str = '{} ({})'.format(version_num, version_dat)


def main():
    """Define argument parses, process arguments and call functions."""
    # Define argument parsers and subparsers
    parser = argparse.ArgumentParser(description='A program for testing implementations of the sieve of Eratosthenes. (https://github.com/flozo/Eratosthenes)')
    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s '+ version_str)
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='verbosity level (-v, -vv, -vvv): '
                        'default = single-line output, v = multi-line, vv = detailed')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help=('disable terminal output (terminates all verbosity)'))
    parser.add_argument('-p', '--progress', action='store_true',
                        help=('show progress bar'))
    parser.add_argument('-s', '--sievemethod', dest='sievemethod',
                        choices=('all', 'odd', '3k', '4k', '6k', 'list', 'list-np', 'divisors'),
                        default='6k', help='sieve method')
    parser.add_argument('-d', '--divisormethod', choices=('all', 'sqrt'),
                        default='sqrt', help='divisor method')
    parser.add_argument('-a', '--auto-name', dest='autoname',
                        action='store_true',
                        help='generate name for output file automatically as \'Eratosthenes_<limit>_<sievemethod>_<divisormethod>.dat\' with path from [outfile]')
    parser.add_argument('limit', type=int, default=100,
                        help='upper limit of test range (a non-negative integer)')
    parser.add_argument('outfile', nargs='?', help='write to file \'outfile\'')

    args = parser.parse_args()

    # Check verbosity level
    verbosity = args.verbose
    if args.quiet is True:
        verbosity = -1
    if verbosity >= 1:
        print(args)

    # Check progress option
    hide_progress = not(args.progress)

    # Process arguments
    limit = int(args.limit)
    algorithm = sieves.Algorithm(args.divisormethod, args.sievemethod)
    if args.divisormethod == 'all':
        divisorfunc = sieves.isprime_all_break
    elif args.divisormethod == 'sqrt':
        divisorfunc = sieves.isprime_sqrt_break
    # elif args.divisormethod == 'sqrt-break':
    #     divisorfunc = sieves.divisors_sqrt_break

    # If autoname option is not used, take outfile argument, else generate auto filename
    if args.autoname is False:
        outfile = args.outfile
    else:
        filename = 'Eratosthenes_{}_{}_{}.dat'.format(limit,
                                                      args.sievemethod,
                                                      args.divisormethod)
        path = os.path.dirname(args.outfile)
        outfile = os.path.join(path, filename)
        if verbosity >= 1:
            print('[auto-name] Using option --auto-name')
            print('[auto-name] Composing output filename from limit ({}), sieve method ({}), and divisor method ({}).'.format(limit, args.sievemethod, args.divisormethod))
            print('[auto-name] Generated auto filename: {}'.format(filename))
            print('[auto-name] Using path from positional argument outfile: {}'.format(path))
    if verbosity >= 1:
        if args.outfile is None:
            print('[output] No output file specified. No file output.')
        else:
            print('[output] Writing output to: {}'.format(outfile))
    start = time.process_time()

    # Use specified algorithms
    if algorithm.sievemethod == 'all':
        primes = sieves.alg_all(divisorfunc, limit, hide_progress)
    elif algorithm.sievemethod == 'odd':
        primes = sieves.alg_odd(divisorfunc, limit, hide_progress)
    elif algorithm.sievemethod == '6k':
        primes = sieves.alg_6k(divisorfunc, limit, hide_progress)
    elif algorithm.sievemethod == '4k':
        primes = sieves.alg_4k(divisorfunc, limit, hide_progress)
    elif algorithm.sievemethod == '3k':
        primes = sieves.alg_3k(divisorfunc, limit, hide_progress)
    elif algorithm.sievemethod == 'list':
        primes = sieves.alg_multiples_all(limit, hide_progress)
    elif algorithm.sievemethod == 'list-np':
        primes = sieves.alg_multiples_all_np(limit, hide_progress)
    elif algorithm.sievemethod == 'divisors':
        primes = sieves.numdivisors(limit, hide_progress)
    if verbosity >= 2:
        print(primes)
    elapsed = (time.process_time() - start)

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
            print('[result] Detected {} prime numbers in {:.9f} seconds.'.format(len(primes), elapsed))
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
            print('Created divisor list in the rage [1, {}] in {:.9f} seconds'.format(limit, elapsed))
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
