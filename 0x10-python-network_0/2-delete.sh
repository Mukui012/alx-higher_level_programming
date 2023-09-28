#!/bin/bash
#script that sends a DELETE request to the URL passed as the first argument and displays body of the response
curl -sX "$1" DELETE
