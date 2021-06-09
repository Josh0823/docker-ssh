#!/bin/bash

echo Generating ssh creds...
rm -rf secrets
mkdir secrets
ssh-keygen -t rsa -N '' -C ca@localhost -f secrets/creds
ssh-keygen -s secrets/creds -h -I localhost secrets/creds.pub

echo Building local...
cd local
docker build -t local:latest .
cd ..

echo Building remote...
cd remote
docker build -t remote:latest .
cd ..
