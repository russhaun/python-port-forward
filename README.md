# Python Port Forward
This script forwards a number of configured local ports to local or remote socket servers.
original script by vinodpandey modified to work on py3 for use with artillery from BinaryDefense
to use with Docker package Doomsday .this is just a concept more will have to done
the basic idea is this: any port that you have artillery monitor can be forwded from true host
to docker contaner on seperate network  in this case port 80 isolating them from everyone so you can 
monitor and react accordingly with a "fake service" that looks local to machine being scanned from 
attacker point of veiw
## Concept:
'''

#Like This:  Att.->>artillery->>Doomsday->>svcname
#ex:        (remote net)->>(localnet)->>(docker net)->>(wherever you want)
        
'''
## Usage:
```
On windows:
python port-forward.py

# iis cannot be enabled on machine. port forward will fail
# and they will see real host. this is a honeypot (right?)
# port 80 must be allowed through windows firewall

On linux:
sudo python port-forward.py

# with default port-forward.config, access: http://localhost/ -> this should now show content from http://localhost:8080/
# you can run a test python http server using below command to check the default configuration
# python -m SimpleHTTPServer 8080
```

## Configuration:
```
Add to the config file port-forward.config lines with contents as follows:
can specify multiple lines

<local incoming port> <dest hostname> <dest port>
```

## Starting/stopping
```
Start the application at command line with 'sudo python port-forward.py' and stop the application by keying in <ctrl-c>.
```

## Errors
```
Error messages are stored in file 'error.log'.
```


## Tested on
'''

Win 10 pro 
py 3.6(local)

docker ver used
Version 18.06.1-ce-win73 (19507)
running linux containers
'''
