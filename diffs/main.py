from nuclear import CliBuilder, arguments, parameter, flag

from .diffs import show_diff
from .version import __version__


def main():
    CliBuilder('diffs', run=show_diff, help_on_empty=True, version=__version__,
               help='Command output changes monitor').has(
        parameter('interval', type=float, default=1, help='interval in seconds between consecutive executions'),
        flag('clear', help='clear terminal scrollback'),
        arguments('cmd', joined_with=' ', help='commmand to be invoked and compare its results'),
    ).run()
