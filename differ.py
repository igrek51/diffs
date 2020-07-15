#!/usr/bin/env python3
import difflib
import time

from colorama import Fore
from nuclear import CliBuilder, arguments, parameter
from nuclear.sublog import log_error
from nuclear.utils.shell import shell_output, shell


def main():
    CliBuilder('differ', run=show_diff, help_on_empty=True, help='Show changes in any command output').has(
        parameter('interval', type=int, default=1, help='interval in seconds between consecutive executions'),
        arguments('cmd', joined_with=' ', help='commmand to be invoked and compare its results'),
    ).run()


def color_diff(diff):
    for line in diff:
        if line.startswith('+'):
            yield Fore.GREEN + line + Fore.RESET
        elif line.startswith('-'):
            yield Fore.RED + line + Fore.RESET
        elif line.startswith('^'):
            yield Fore.BLUE + line + Fore.RESET
        else:
            yield line


def show_diff(cmd: str, interval: int):
    with log_error():
        output_0 = shell_output(cmd)

        while True:
            shell('tput reset')

            output_now = shell_output(cmd)

            diff = difflib.ndiff(output_0.splitlines(keepends=True), output_now.splitlines(keepends=True))
            diff = [d for d in diff if d[0] != ' ']
            diff = color_diff(diff)
            print(''.join(diff))

            time.sleep(interval)


if __name__ == '__main__':
    main()
