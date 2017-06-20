# andela-bootcamp
Pre Bootcamp Technical Assesment Test

[![Travis Badge](https://travis-ci.org/brayoh/bucket-list.svg?branch=master)]()
[![Code Climate](https://img.shields.io/codeclimate/github/kabisaict/flow.svg)]()

## How to setup - for Debian users

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
    chmod +x server.sh

*  ### run
    ./server.sh

*  ### open browser and navigate to
    http://127.0.0.1:5000

  ## How to run test
    after installing project dependencies run:     
     * nosetests
