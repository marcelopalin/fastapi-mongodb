Docker Cheat Sheet

I'm not going to explain how Docker works. For that there are a lot of in depth tutorials. But I'm going to leave here a list of useful commands, some of them that we're going to use. So you don't have to go hunting into the documentation.
Command 	Description
docker pull <image> 	Downloads an image without starting it
docker images 	List of downloaded images
docker image rm <id> 	Remove the image with id <id>. It's better to use the id instead of the name in case you have multiple version of the same service
docker run <image> 	Starts the image. This is creating a container
docker run -d <image> 	Starts the image in detached mode
docker run -p 1234:9876 <image> 	Runs an image binding the local port 1234 to the container port 9876
docker run --name <image> 	Run the image with a custom image
docker ps 	List of running images
docker ps -a 	List of running and stopped images
docker stop <id> 	Stops the container with the id <id>
docker start <id> 	Re-starts an already created container (crated with docker run)
docker log <id> 	Output of the image with id <id>
docker exec -it <id> <command> 	Run the command <command> (pe. /bin/bash) in the running container interactively
docker network ls 	List the available networks
docker network create <name> 	Create a new network
docker run --network <name> <image> 	Runs the image <image> on the network <network>