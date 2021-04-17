#!/bin/bash

python3 -m venv env
source env/bin/bash
make install_test

az webapp up -sku F1 -n pmu-udacity-webapp