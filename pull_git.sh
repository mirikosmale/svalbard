#!/bin/bash 

# git pull svalbard_ssh master
git stash
git pull svalbard_ssh master
chmod -R 755 .
