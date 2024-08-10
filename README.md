# Number Guessing Game

This projects is to run the number guessing app. It allows you to choose the range and then select the number

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies. Also it can be deployed on docker/podman to run the image

```bash
pip install -r requirments.txt
```

## Usage

```bash
# Install virtual environment
python -m venv venv

# Activate the virtual environment
. venv/bin/activate

# Install the dependencies
pip install --no-cache-dir -r requirements.txt

# Run the gunicorn or flask app (windows does not support gunicorn) For Gunicorn you need to pass the ssl certificates
gunicorn --config gunicorn_config.py main:app
or 
python main.py
```

## Contributing

You cna pull the code and do customization as per your requirements.

## License

[MIT](https://choosealicense.com/licenses/mit/)