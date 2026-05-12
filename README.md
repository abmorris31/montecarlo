# montecarlo

![PyPI version](https://img.shields.io/pypi/v/montecarlo.svg)

A package to perform Monte Carlo simulations.

* GitHub: https://github.com/abmorris31/montecarlo/
* PyPI package: https://pypi.org/project/montecarlo/
* Created by: **[Alex Morris](https://audrey.feldroy.com/)** | GitHub https://github.com/abmorris31 | PyPI https://pypi.org/user/abmorris31/
* Free software: MIT License

## Features

* Runs a monte carlo simulation using metropolis sampling to give accurate values of energy and magnetization when the number of an ising hamiltonian's configurations becomes too large for direct calculation. Assumes a boltzmann distribution.

## Documentation

Refer to the docs folder for more information about installation and usage.

Documentation is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

* **Live site:** https://abmorris31.github.io/montecarlo/
* **Preview locally:** `just docs-serve` (serves at http://localhost:8000)
* **Build:** `just docs-build`

API documentation is auto-generated from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

Docs deploy automatically on push to `main` via GitHub Actions. To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/montecarlo.git
cd montecarlo

# Install in editable mode with live updates
uv tool install --editable .
```

This installs the CLI globally but with live updates - any changes you make to the source code are immediately available when you run `montecarlo`.

Run tests:

```bash
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Author

montecarlo was created in 2026 by Alex Morris.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
