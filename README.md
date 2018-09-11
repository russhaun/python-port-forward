# Python Port Forward
This script forwards a number of configured local ports to local or remote socket servers.
original script by vinodpandey modified to work on py3 for use with artillery from BinaryDefense
for use with Docker.this whole script will eventually work its way into said software.

## Usage:
```
On windows:
python port-forward.py

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
