# StrongMind Jr. Full Stack Application

> This is a full-stack web application created for the coding exercise at StrongMind

## Technology Used

- Backend: Django 5.0.1 (Python 3.11.0)
- Frontend: HTML, CSS (Bootstrap 5)
- Database: SQLite (development), PostgreSQL (deployment)
- OS: Windows
- Development timeline: [TIMELINE.md](https://github.com/trashykoifish1/strongmind-pizza/blob/main/TIMELINE.md)

## Building Locally

The deployed website can be accessed at https://strongmindpizza.onrender.com/

> [!NOTE]
> Due to the free tier of Render, the host will shut down after periods of inactivity and has to be startup upon access. So, the first load should be fairly long. Please be patient `:)`

To build the project locally, follow these steps:

- Clone the project or download the [zip](https://github.com/trashykoifish1/strongmind-pizza/archive/refs/heads/main.zip)

```shell
$ git clone https://github.com/trashykoifish1/strongmind-pizza.git
```

- Ensure that [Python](https://www.python.org/) is installed

```shell
$ python --version
Python 3.11.0
```

> [!NOTE]
> Because the application uses `Django 5.0.1` so `Python >= 3.10` is reccommended

- Navigate to the project folder
- Create your own virtual environment or use the provided one

**Windows:**

Creating virtual environment

```shell
$ python -m venv env
```

Activating virtual environment

```shell
$ .\env\Scripts\activate
```

**Mac/Linux:**

Creating virtual environment

```bash
$ python -m venv env
```

Activating vritual environment

```bash
$ source env/bin/activate
```

- Ensure that `pip` is installed if not refer to [pip installation guide](https://pip.pypa.io/en/stable/installation/)

```shell
$ pip --version
pip 22.3 from FILEPATH (python 3.11)
```

- Install the required dependencies

```shell
$ pip install -r requirements.txt
```

- Run the project locally

```
$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
February 09, 2024 - 02:20:24
Django version 5.0.1, using settings 'pizza_app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

- Navigate to [localhost:8000](http://localhost:8000/) to access the application

> [!NOTE]
> The local application is configured to use `SQLite`, in order to switch to `PostgreSQL` (hosted on Render) follow the steps below

- Access the `settings.py` file with a text editor
- Find the `DEBUG` variable and switch between `True` or `False` accordingly

## Testing
