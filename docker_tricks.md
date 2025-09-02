# Docker Tricks and Commands

## Container Logs and Debugging
Capture logs from crashing container
Start Docker Container Locally

docker exec -it `docker ps -aq | head -1` tail -f /app/logs/USER-user-service.txt
* don't quote command

Look at dead container's filesystems
docker inspect <id>  | grep volume
Locally on Mac, you won't be able to access /var/lib/docker.  You need to use screens command:

screen ~/Library/Containers/com.docker.docker/Data/vms/0/tty
cd /var/lib/docker/volumes
ls -ltr | tail
Use ctrl-a d to detach, 'screen -S <sessionname> -X quit' to stop screen process

## Container Management

### Running BusyBox Containers
BusyBox containers exit immediately because they don't have a long-running process by default.

**Problem**: Container exits even with `-d` flag
```bash
docker run -p 8080:8080 -d --name box-1 busybox  # This exits immediately
```

**Solutions**:
```bash
# Keep container running with sleep
docker run -p 8080:8080 -d --name box-1 busybox sleep infinity

# Interactive mode with pseudo-TTY
docker run -p 8080:8080 -d -it --name box-2 busybox

# Keep running with tail command
docker run -p 8080:8080 -d --name box-3 busybox tail -f /dev/null
```

### Docker Exec Commands
Execute commands inside running containers:

```bash
# Interactive shell session
docker exec -it container_name /bin/sh

# For containers with bash
docker exec -it container_name /bin/bash

# Run single command
docker exec container_name ls -la

# Run command and see output
docker exec container_name ps aux
```

**Flags explained**:
- `-i` (interactive): Keep STDIN open
- `-t` (tty): Allocate a pseudo-TTY
- `-it` together: Interactive terminal session

### Container Cleanup
TO delete the exited containers
docker rm $(docker ps -aq --filter "name=box-1" --filter "status=exited")

