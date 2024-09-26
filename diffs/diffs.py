#!/usr/bin/env python3
import difflib
import time
from typing import Iterable

from colorama import Fore
from nuclear.sublog import error_handler, logger
from nuclear.shell import shell


def color_diff(diff) -> Iterable[str]:
    for line in diff:
        if line.startswith('+'):
            yield Fore.GREEN + line + Fore.RESET
        elif line.startswith('-'):
            yield Fore.RED + line + Fore.RESET
        elif line.startswith('^'):
            yield Fore.BLUE + line + Fore.RESET
        else:
            yield line


def show_diff(cmd: str, interval: int, clear: bool, continuous: bool):
    with error_handler():
        output_0 = shell(cmd)

        while True:
            if clear:
                shell('tput reset', raw_output=True)
            elif not continuous:
                shell('clear -x', raw_output=True)  # do not clear terminal's scrollback

            output_now = shell(cmd)

            diff = difflib.ndiff(output_0.splitlines(keepends=True), output_now.splitlines(keepends=True))
            diff_list: list[str] = [d for d in diff if d[0] != ' ']
            diff_lines = list(color_diff(diff_list))
            
            if continuous:
                output_0 = output_now
                if diff_lines:
                    logger.info('Changes found')
                    print('\n'.join(diff_lines))
            else:
                if diff_lines:
                    print('\n'.join(diff_lines))

            time.sleep(interval)
