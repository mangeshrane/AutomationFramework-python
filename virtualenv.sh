#!/bin/bash

if [ -d ../env ] 
then
	echo "activate" 
else 
	python -m venv ../env
	echo "activate" 
fi