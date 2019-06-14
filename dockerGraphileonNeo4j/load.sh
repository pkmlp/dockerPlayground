#!/usr/bin/env bash
set -e
cd $(dirname $0)
docker load -i graphileon-2.2.0-pe-docker.tar.gz
