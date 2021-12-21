#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main file of Eratosthenes."""

# Import modules
import argparse
import time
import functions as fn
import classes

# Define version string
version_num = '0.27'
version_dat = '2021-12-20'
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
    parser.add_argument('-k', '--keep',
                        choices=('always', 'never', 'interrupt'),
                        default='interrupt', help='keep mode for temporary '
                        'file (storage mode only)')
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

    # Define file extension for temporary file
    temp_ext = '.temp'
    # Translate progress option
    # hide_progress = not(args.progress)

    # Create divisor-method object
    divisor_method = classes.DivisorMethod(args.divisormethod)
    # Create sieve-method object
    sieve_method = classes.SieveMethod(args.sievemethod)
    # divisorfunc = fn.select_divisormethod(args)
    # Generate automatic filename
    outfile = fn.auto_filename(args, verbosity)
    # Make limit integer
    limit_specified = int(args.limit)
    # Define settings object
    settings = classes.Settings(divisor_method.name,
                                sieve_method.name,
                                version_str,
                                limit_specified,
                                sieve_method.get_iterations(limit_specified),
                                args.progress,
                                args.mode,
                                args.keep,
                                outfile,
                                temp_ext)
    # algorithm = classes.Algorithm(args.divisormethod, args.sievemethod)
    # Set interrupt switch to default
    interrupt = False

    # if verbosity >= 1:
    #     print()
    # Start timer
    start = time.process_time()
    # Check writing mode
    if settings.mode == 'storage':
        # Write to temporary file
        interrupt, last_iter, limit_actual = fn.select_algorithm_storage_mode(divisor_method,
                                                                              sieve_method,
                                                                              settings,
                                                                              verbosity)
    else:
        # Determine prime numbers
        primes, interrupt, last_iter, limit_actual = fn.select_algorithm_memory_mode(divisor_method,
                                                                                     sieve_method,
                                                                                     settings,
                                                                                     verbosity)
    # Stop timer
    elapsed_time = (time.process_time() - start)
    if settings.mode == 'storage':
        # Read temporary file
        with open(settings.tempfile, 'r') as f:
            primes = f.read().splitlines()
    # Define Result object
    result = classes.Result(last_iter, limit_actual, elapsed_time,
                            interrupt, primes)
    # Print result if -vv or -vvv
    if verbosity >= 2:
        print(primes)

    # Generate output
    fn.output(divisor_method, sieve_method, settings, result, verbosity)


if __name__ == '__main__':
    main()
