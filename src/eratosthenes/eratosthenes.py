#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main file of Eratosthenes."""

# Import modules
import argparse
import time
import functions as fn
import classes

# Define version string
version_num = '0.24'
version_dat = '2021-12-16'
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
                        '\'Eratosthenes_<limit>_<sievemethod>_<divisormethod>'
                        '_<mode>.dat\' with path from [outfile]')
    parser.add_argument('-m', '--mode', choices=('memory', 'storage'),
                        default='memory', help='on-the-fly writing mode '
                        '(memory=keep result in array before writing to file, '
                        'storage=write to disk on the fly)')
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
    algorithm = classes.Algorithm(args.divisormethod, args.sievemethod)
    # Make limit integer
    limit = int(args.limit)

    # Start timer
    start = time.process_time()
    # Check writing mode
    if args.mode == 'storage':
        # Write to temporary file
        fn.select_algorithm_storage(algorithm, divisorfunc, limit,
                                    outfile + '.temp', hide_progress,
                                    verbosity)
        # sv.alg_6k_file(divisorfunc, limit, outfile + '.temp')
        # Stop timer
        elapsed_time = (time.process_time() - start)
        # Read temporary file
        with open(outfile + '.temp', 'r') as f:
            primes = f.read().splitlines()
    else:
        # Determine prime numbers
        primes = fn.select_algorithm(algorithm, divisorfunc, limit,
                                     hide_progress, verbosity)
        # Stop timer
        elapsed_time = (time.process_time() - start)
    # Define Result object
    result = classes.Result(args.divisormethod, args.sievemethod,
                            version_str, limit, elapsed_time,
                            str(args.progress), args.mode, primes)
    # Print result if -vv or -vvv
    if verbosity >= 2:
        print(primes)

    # Generate output
    fn.output(result, outfile, verbosity)


if __name__ == '__main__':
    main()
