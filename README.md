##what is reverse shell?
A python script which allows an operator to control multiple client devices remotely.

##how to use?

1. Run the server.py script on your server and keep it active to listen or incoming connections.
2. Enter your server IP address in client file as 'host' variable
3. Run the client.py script on client's device.

##turtle shell commands

-   List connected devices

```
turtle> list

----------CLIENTS---------
[0]  216.239.32.0
[1]  66.249.80.0
```

-   Select from client list

```
turtle> select 0

You are now connected to target
path/to/client/file/on/client/device>
```

-   Run a command on client

```
path/to/client/file/on/client/device> ls

client.py
**Other files and folders**
```

-   Go back to turtle

```
path/to/client/file/on/client/device> quit

turtle>
```

-   Close the program and end all connections

```
turtle> exit
```

-   Close connection with a single client

```
path/to/client/file/on/client/device> exit

turtle>
```
