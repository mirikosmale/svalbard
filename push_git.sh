#!/bin/bash 

git add .
git add bash_code
git add python_code
git add settings

git commit -a -m "$1"
git push svalbard_ssh master
