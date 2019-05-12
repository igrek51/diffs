# differ
**differ** monitors for a changes in any shell command output between initial state and the current output.

# Usage
```bash
./differ.py <cmd>
```
The initial *<cmd>* output is stored at the beginning.
Then the command is run again periodically and the output is compared with the initial output.
If there are differences, they are shown in the standard diff format.

## Examples
Find new applications opening network ports, show only changes between the initial state:
```bash
$ ./differ.py netstat -tulpn

# after opening new port:

+ tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN      18655/python
```

Monitor a file for a changes:
```bash
$ ./differ.py cat /etc/resolv.conf
```

```bash
$ ./differ.py date
- nie, 12 maj 2019, 13:41:51 CEST
?                       ^  ^
+ nie, 12 maj 2019, 13:42:52 CEST
?                       ^  ^
```
