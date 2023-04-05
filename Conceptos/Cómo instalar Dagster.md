### Step 1: Create a Virtual Environment

First, create a new virtual environment for your Dagster project using `virtualenv`. You can use any directory you like, but for this example, we'll create a new directory named `dagster-tutorial` in your home directory.

```bash
cd ~ # moves to root folder
mkdir dagster-tutorial 
cd dagster-tutorial 
python -m venv .venv # creates a virtual environment for the project
```

### Step 2: Activate the Virtual Environment

Activate the virtual environment using the activate script.

```bash
.venv/Scripts/activate
```

### Step 3: Install Dagster

With the virtual environment activated, install Dagster and the required dependencies via pip.

```
pip install dagster dagit
```

> *Dagster* es el módulo completo y *dagit* es la interfaz de usuario.

### Step 4: Initialize a New Dagster Project

Next, create a new Dagster project running the following command in your `dagster-tutorial` directory:

```bash
dagster project scaffold --name dagster-project-name
```

The newly generated `dagster-project-name` directory is a fully functioning [Python package](https://docs.python.org/3/tutorial/modules.html#packages) and can be installed with `pip`.

To install it as a package and its Python dependencies, run:

```bash
pip install -e ".[dev]"
```

> Using the `--editable` (`-e`) flag instructs `pip` to install your code location as a Python package in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes are automatically applied.

Run the following to start the Dagit web server:

```bash
dagster dev
```

> **Note**: This command also starts the [Dagster daemon](https://docs.dagster.io/deployment/dagster-daemon). Refer to the [Running Dagster locally guide](https://docs.dagster.io/guides/running-dagster-locally) for more info.

Use the browser to open [http://localhost:3000](http://localhost:3000/) to view the project.

### Recursos externos
- [Dagster tutorial](https://docs.dagster.io/tutorial)
- [[Cómo utilizar Dagster]]
