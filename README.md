# Dreamers: instructions for running:

Make sure you're in the same directory as the Dockerfile, then copy the following commands into terminal to build a docker container with the necessary requirements and run the executable.

i.     `$ docker build -t solver .`

ii.    `$ docker run -it \
            --volume "$(pwd)":/code/ \
            solver`
            
The permutation-iteration graph will be generated each time the docker program is run and will produce a graph saved as `graph.png` in the `/dreamers` directory.
