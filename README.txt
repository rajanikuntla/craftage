# Introduction 

APIs for contact interaction 

# Getting Started

The APIs are developed in Python using the FastAPI library:

1. Install Python 3.8 and create a virtual environment

    - On the terminal window, check the Python version by typing

    `python -V`

    - Create a new virtual environment named `craftage_venv`

    `python -m venv craftage_venv`
    
    - Activate this new virtual environment (you would see `(craftage_venv)` appearing at beginning of your prompt)

    `source craftage_venv/bin/activate`

    NOTE:: 

    if venv doesn't work follow the conda steps to activate 

    a. To create env in conda

    CMD: conda create -n craftage_venv python==3.8

    proceed with y in prompt

    b. To activate env

    CMD: conda activate craftage_venv    

2.  Install the python packages, all contained in the `requirements.txt` file

    `pip install -r requirements.txt`
 
 

# Build and Test

The code can be run on a terminal with the above `craftage_venv` python environment activated, by moving to the base directory of the repository and typing:

**Debug**

```

uvicorn api:app --reload

```
 

Then, the API can be tested by opening the Swagger doc for the API at: http://127.0.0.1:8000/docs or else the ReDoc doc at http://127.0.0.1:8000/redoc

 

## Tests and coverage report

Test can be run using `pytest` simply by running:

    `pytest`

 

 