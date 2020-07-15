# diffs

[![GitHub version](https://badge.fury.io/gh/igrek51%2Fdiffs.svg)](https://github.com/igrek51/diffs)
[![PyPI version](https://badge.fury.io/py/diffs.svg)](https://pypi.org/project/diffs)

**diffs** monitors for any changes in arbitrary shell command output between the initial state and the current output.

# Installation
```shell
pip3 install diffs
```

Python 3.6 (or newer) is required.

# Usage
```bash
diffs CMD
```
The initial `CMD` output is stored at the beginning.
Then the command is run again periodically and the output is compared against the initial output.
If there are differences, they are shown in the standard diff format. The unchaged lines are not shown.

## Examples
Show how many packets have been sent since the script has been started:
```bash
$ diffs ifconfig wlp2s0
-         RX packets 819320  bytes 171114372 (163.1 MiB)
?                     ---                ---      ^
+         RX packets 820098  bytes 171181884 (163.2 MiB)
?                       +++            + ++       ^
-         TX packets 2493955  bytes 3512746768 (3.2 GiB)
?                        ^^^           ^^^  ^^
+         TX packets 2496731  bytes 3516673094 (3.2 GiB)
?                       ++ ^           ^  ^^^^
```

Find new applications opening network ports (shows only changes between the initial state):
```bash
$ diffs netstat -tulpn
# after opening new port:
+ tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN      18655/python
```

Monitor a file for a changes:
```bash
$ diffs cat /etc/resolv.conf
```

Difference between starting date and the current date:
```bash
$ diffs date
- nie, 12 maj 2019, 13:41:51 CEST
?                       ^  ^
+ nie, 12 maj 2019, 13:42:52 CEST
?                       ^  ^
```

Finding lately spawned processes:
```bash
$ diffs ps a
-   806 tty7     Ssl+   1:46 /usr/lib/xorg/Xorg :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
?                          ^
+   806 tty7     Ssl+   1:47 /usr/lib/xorg/Xorg :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
?                          ^
- 12521 pts/1    S+     0:00 /bin/sh -c ps a
?    --
+ 12665 pts/1    S+     0:00 /bin/sh -c ps a
?   ++
- 12522 pts/1    R+     0:00 ps a
?   ^^^
+ 12666 pts/1    R+     0:00 ps a
?   ^^^
```
