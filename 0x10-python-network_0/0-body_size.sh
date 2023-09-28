#!/bin/bash
#script that displays the size of the body of the URL
curl -s "$1" | wc -c
