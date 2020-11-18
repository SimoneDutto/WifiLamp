#!/bin/bash

flask run &

./ngrok http 5000 & 

