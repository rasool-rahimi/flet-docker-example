**NOTE:** Throughout this whole process, the Docker Desktop program should be open.  
**NOTE:** For linking to the "assets" directory, don't use "/assets" and use "/" instead.

1. Create a local Docker image with the following command:

    ```bash
    docker build -t {project-name} .
    
    docker run -p 80:8000 {project-name}
    ```

2. Create a repository on [Docker Hub](https://hub.docker.com/) and name it whatever you want.

3. Log in to your Docker account in the terminal using the following command:

    ```bash
    docker login -u {your-username}
    ```

4. Enter your password:

    ```
    {your-password}
    ```

5. Use this command to create a tag for your repository:

    ```bash
    docker tag {project-name}:{project-tag} {your-username}/{repository-name}:{repository-tag}
    ```

6. Finally, push your local image to the Docker Hub repository:

    ```bash
    docker push {your-username}/{repository-name}:{repository-tag}
    ```

[Docker Hub Link](https://hub.docker.com/)

**ENJOY!!!**
