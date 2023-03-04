# hackathon
Vefa ASR Lab Hackathon

## Dependencies
- Ubuntu 22.04

## Installation
You must use the installation script as a normal user (with sudo privileges, the script will ask sudo password).

To install on a new server with default configs and without domain (for this, project must be on directory "~/hackathon"):
```bash
$ chmod +x install.sh
$ ./install.sh
```

You can specify project name with -n argument (server directory needs to be at ~/<PROJECT_NAME>):
```bash
$ ./install.sh -n <PROJECT_NAME>
```

You can specify domain with -d argument (This will get an SSL certificate for your domain):
```bash
$ ./install.sh -d <DOMAIN>
```
