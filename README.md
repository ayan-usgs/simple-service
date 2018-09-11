# Simple Service

This is a simple Python Falcon web application for testing in a Docker container
and loading environment variables from a mounted volume. This is intended test the
efficacy of *.var files with AWS ECS which is missing support of env files as of
September 2018.

The path where the file or directory are mounted in the container must also be passed 
in as the `MOUNT_DIRECTORY` environment variable when running the container for the
environment variables to be picked up. The container will still work if not volume
and environment variables are provided.