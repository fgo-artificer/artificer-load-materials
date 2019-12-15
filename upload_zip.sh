#!/bin/bash
proj=artificer-load-materials
aws lambda update-function-code --function-name $proj --zip-file fileb://$proj.zip
