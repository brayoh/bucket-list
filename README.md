# My BucketList App
 a bucket list is a list of things a person wants to achieve or experience, as before reaching a certain age or dying,
 this web app allows to add, edit, delete or update your bucketlist(s) over time.

[![Travis Badge](https://travis-ci.org/brayoh/bucket-list.svg?branch=master)]()
[![Code Climate](https://img.shields.io/codeclimate/github/kabisaict/flow.svg)]()
[![Coverage Status](https://coveralls.io/repos/github/brayoh/bucket-list/badge.svg?branch=master)](https://coveralls.io/github/brayoh/bucket-list?branch=master)

## How to setup

* ### clone the repo to desired directory
    git clone https://github.com/brayoh/bucket-list.git

*  ### install pip
    sudo apt-get install python3-pip

 * ### create virtual environment to work on    
    mkvirtualenv my-venv

 * ### switch to the virtual env you created
    workon my-venv

 * ### navigate to the repo directory
    cd /my_project_directory/

*  ### install project dependencies
     pip install -r requirements.txt

*  ### make script executable
    chmod +x ./scripts/server_run.sh

*  ### run
    ./scripts/server_run.sh

*  ### open browser and navigate to
    http://127.0.0.1:5000

  ## How to run test
    after installing project dependencies run:     
     * nosetests
