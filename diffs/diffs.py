#!/usr/bin/env python3
import difflib
import time

from colorama import Fore
from nuclear.sublog import error_handler
from nuclear.shell import shell


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
    with error_handler():
        output_0 = shell(cmd)

        while True:
            if clear:
                shell('tput reset', raw_output=True)
            else:
                shell('clear -x', raw_output=True)  # do not clear terminal's scrollback

            output_now = shell(cmd)

            diff = difflib.ndiff(output_0.splitlines(keepends=True), output_now.splitlines(keepends=True))
            diff_list: list[str] = [d for d in diff if d[0] != ' ']
            diff_list = color_diff(diff_list)
            print(''.join(diff_list))

            time.sleep(interval)
