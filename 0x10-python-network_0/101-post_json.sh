#!/bin/bash
# This script sends json files
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
