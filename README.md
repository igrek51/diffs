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
`diffs ifconfig wlp2s0`  
![diffs demo ifconfig](https://github.com/igrek51/diffs/blob/master/docs/img/demo-ifconfig.gif?raw=true)

Find new applications opening network ports (shows only changes between the initial state):  
`diffs sudo netstat -tulpn`  
![diffs demo netstat](https://github.com/igrek51/diffs/blob/master/docs/img/demo-netstat.gif?raw=true)

Monitor changes in a file:
```bash
$ diffs cat /etc/resolv.conf
```

Difference between starting date and the current date:   
`diffs date`  
![diffs demo date](https://github.com/igrek51/diffs/blob/master/docs/img/demo-date.gif?raw=true)

Finding newly spawned processes:  
`diffs ps a -o pid,cmd`  
![diffs demo ps](https://github.com/igrek51/diffs/blob/master/docs/img/demo-ps.gif?raw=true)

