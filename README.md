<div>
  <h1 align="center">cdvpp</h1>
  <h4 align="center">
    Chilean Digital Vaccination Pass Parser (CDVPP) parses digital vaccination
    passes from PDF files
  </h4>
</div>

Reads a Digital Vaccination Pass PDF file as input and retrieves its details
as an instance of `VaccinationPass`.

## Development

This project was developed using `pyenv` and `pipenv`.

First install the Python version for this project specified in the
`.python-version` file.

```bash
pyenv install 3.10.0
```

Then move to the project directory and run `pipenv install` to install Pipfile
specified dependencies.

Finally run the virtual environment using `pipenv shell`.

Execute `python src/main.py` through Pipenv's shell to run the project.

## Caveats

Currently only the version of the PDF issued as of November 16, 2021 is admited.
Other versions are not yet compatible. This application relies on a specific
order of lines to retrieve each field from the PDF file.

## Pyright Support

Create a `pyrightconfig.json` file in the root directory and append the
following contents:

```json
{
  "venvPath": "<Absolute Path to your virtualenvs directory>",
  "venv": "<Virtualenv directory name>",
}
```

Where `venvPath` belongs to your `virtualenvs` directory path, and `venv` to
this project virtual environment.
