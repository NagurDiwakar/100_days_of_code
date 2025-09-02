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

