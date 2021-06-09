
# Example of ssh between two docker containers

Do this to build & start the containers:

    bash ./build.sh
    docker compose up

Then find the local container using `docker ps` and do this:

    docker exec -it <local-container-id> bash
    bash test-user.sh remote admin

You should now be in the remote container via ssh.


This repo also contains files to test conda environment validation via the asyncssh module. Running `validate.py /home/admin/miniconda3/envs/test-env remote admin` from the local container at /srv will use asyncssh to ensure that conda environment exists in the remote container at that path.
