#!/usr/bin/env python3
import difflib
import time

from colorama import Fore
from nuclear.sublog import log_error
from nuclear.utils.shell import shell_output, shell


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


def show_diff(cmd: str, interval: int, clear: bool):
    with log_error():
        output_0 = shell_output(cmd)

        while True:
            if clear:
                shell('tput reset')
            else:
                shell('clear -x')  # do not clear terminal's scrollback

            output_now = shell_output(cmd)

            diff = difflib.ndiff(output_0.splitlines(keepends=True), output_now.splitlines(keepends=True))
            diff = [d for d in diff if d[0] != ' ']
            diff = color_diff(diff)
            print(''.join(diff))

            time.sleep(interval)
