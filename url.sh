#!/bin/bash

url=$(curl -s 127.0.0.1:4040/api/tunnels | jq -r .tunnels[0].public_url)

echo $url
