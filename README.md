Platform Overview
Petstagram: WorkPal serves as a versatile platform connecting pet owners with potential pet sitters or caretakers.

Pet Sitting Listings and Application Functionality
Users can explore diverse pet sitting listings and seamlessly apply for various opportunities. Pet owners can post detailed listings, outlining their pet's needs and preferences to attract suitable sitters, while pet sitters can effortlessly browse and submit applications through the platform's interface.

Pet Care Projects
An additional feature offered by Petstagram: WorkPal is the ability to create pet care projects. Users can outline specific tasks they need to be completed, providing a flexible avenue for hiring pet care professionals on a project basis without the commitment of a long-term arrangement.

Conclusion
Petstagram: WorkPal's multifaceted approach provides a dynamic environment for both pet owners and pet sitters. With its diverse range of features, the platform facilitates seamless connections and collaborations in the pet care market.


<h2 id="section-id">Technologies</h2>

<br />
<br />

<p align="center">
    <a href="https://www.python.org"><img src="https://skillicons.dev/icons?i=python" alt="Python"></a>&nbsp;&nbsp;&nbsp;
    <a href="https://git-scm.com"><img src="https://skillicons.dev/icons?i=git" alt="Git"></a>&nbsp;&nbsp;&nbsp;
    <a href="https://www.djangoproject.com"><img src="https://skillicons.dev/icons?i=django" alt="Django"></a>&nbsp;&nbsp;&nbsp;
    <a href="https://www.docker.com"><img src="https://skillicons.dev/icons?i=docker" alt="Docker"></a>&nbsp;&nbsp;&nbsp;
    <a href="https://www.postgresql.org"><img src="https://skillicons.dev/icons?i=postgres" alt="PostgreSQL"></a>&nbsp;&nbsp;&nbsp;
    <a href="https://en.wikipedia.org/wiki/HTML"><img src="https://skillicons.dev/icons?i=html" alt="HTML"></a>&nbsp;&nbsp;&nbsp;
    <a href="https://bg.wikipedia.org/wiki/CSSj"><img src="https://skillicons.dev/icons?i=css" alt="CSS"></a>&nbsp;&nbsp;&nbsp;
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"><img src="https://skillicons.dev/icons?i=js" alt="JavaScript"></a>
</p>

<br />
<br />

![Python](https://skillicons.dev/icons?i=python)

### Python

Python is a high-level, interpreted programming language known for its simplicity and readability, making it ideal for beginners and experienced developers alike. It supports multiple programming paradigms and has a vast ecosystem of libraries and frameworks for various applications, including web development, data analysis, machine learning, and automation.

<br />

![Git](https://skillicons.dev/icons?i=git)

### Git

Git is a distributed version control system designed for tracking changes in source code during software development. It allows multiple developers to collaborate on projects efficiently by providing tools for branching, merging, and versioning code.

<br />

![Git](https://skillicons.dev/icons?i=django)

### Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It provides built-in features for authentication, URL routing, template engine, and database management, making it ideal for building web applications quickly and efficiently.

<br />

![Postgres](https://skillicons.dev/icons?i=postgres)

### Postgres

PostgreSQL, often referred to simply as "Postgres," is a free and open-source relational database management system known for its reliability, extensibility, and powerful features. It supports a wide range of advanced functionalities, including ACID compliance, data integrity, and concurrency control, making it a popular choice for both small-scale projects and large-scale enterprise applications.

<br />

![HTML](https://skillicons.dev/icons?i=html)

### HTML

HTML is the foundation of web development, allowing developers to structure content and create interactive web pages using tags and attributes. It provides a standardized way to format text, images, links, and other elements on the internet.

<br />

![CSS](https://skillicons.dev/icons?i=css)

### CSS

CSS, or Cascading Style Sheets, is a styling language used to control the presentation and layout of HTML documents. It enables developers to customize the appearance of web pages, including aspects such as fonts, colors, spacing, and positioning, enhancing the visual appeal and user experience of websites.

<br />

---

<h2 id="installation">Installation</h2>

To utilise this Django project, follow the steps below to set it up on your system.

1. [Install Python](#installation-install-python)
2. [Confirm Python Installation](#installation-confirm-installation-python)
3. [Install PostgreSQL](#installation-confirm-installation-postgres)
4. [Confirm PostgreSQL installation](#installation-confirm-installation-postgres)
5. [Clone the project](#installation-clone-project)
6. [Create a virtual environment in the project directory](#installation-create-virtual-environment)
7. [Activate the virtual environment](#installation-activate-virtual-environment)
8. [Install required packages to run the project](#installation-required-packages)
9. [Configure database](#installation-configure-database)
10. [Run makemigrations](#installation-run-makemigrations)
11. [Run migrate](#installation-run-migrate)
12. [Run the application](#installation-run-application)
13. [Open the application](#installation-open-app)

Guide

1. <b id="installation-install-python">Install Python: </b> To run the project, ensure Python is installed on your machine. Although Python comes pre-installed on many Linux distributions, the version may vary depending on the distribution and operating system version. If Python is not installed, you can download it from [here](https://www.python.org/downloads/).

2. <b id="installation-confirm-installation-python"> Confirm Python installation: </b> To confirm the successful installation of Python, run the following command in your command line interface (CMD/Terminal...). 

```
python3 --version
```

Please note the potential variations in the command based on how Python was installed on your system: some commands may begin with `python`, others with `python3`, and yet others with `py`. Despite the differences in reference, they all refer to the same command.

3. <b id="installation-install-postgres"> Install postgres: </b> Download the installer from the [PostgreSQL website](https://www.postgresql.org) and follow the installation instructions

4. <b id="installation-confirm-installation-postgres"> Confirm PostgreSQL installation: </b> To validate the successful installation of PostgreSQL, execute the subsequent command within your command line interface (CLI), whether it's CMD or Terminal.

```
postgres --version
```

5. <b id="installation-clone-project">Clone the project:</b> Navigate to your preferred installation directory using your command-line interface, and proceed to clone the project. If you encounter any difficulties, you can find more information about cloning your project [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

* Using HTTPS

```
git clone https://github.com/username/repository.git
```

Replace `https://github.com/username/repository.git` with the HTTPS URL you copied from GitHub.

* Using SSH```

```
git clone ssh://git@github.com/username/repository.git
```

Substitute `ssh://git@github.com/username/repository.git` with the SSH URL you copied from GitHub. For instance:

6. <b id="installation-create-virtual-environment">Create a Virtual Environment:</b> To effectively manage dependencies, versions, and ensure encapsulation, it's essential to create a virtual environment in the directory of your project using:

```
python3 -m venv ./venv
```

7. <b id="installation-activate-virtual-environment">Activate the virtual Environment:</b> Activating the virtual environment ensures that Python commands use the environment's interpreter and packages, avoiding conflicts with system-wide installations and maintaining consistency across projects.

```
source venv/bin/activate
```

8. <b id="installation-required-packages">Install required packages:</b> After you have activated the venv, install the required packages to be able to run the project

```
pip install -r requirements.txt
```

9. <b id="installation-configure-database">Configure database:</b> To ensure database access, configure it within the settings.py file of your project. The user

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myprojectdb', # The name of your database
        'USER': 'myprojectuser', # The name of your user or the default 'postgres' user
        'PASSWORD': 'password', # The password associated with your account, which was set up during the PostgreSQL installation.
        'HOST': 'localhost',  # Or the IP address of your PostgreSQL server
        'PORT': '5432',       # Default PostgreSQL port
    }
}
```

10. <b id="installation-run-makemigrations">Run makemigrations:</b> To check any changes in the defined models, execute the following command:
```
python manage.py makemigrations
```

11. <b id="installation-run-migrate">Run migrate:</b>To apply the pending database schema changes defined in migration files.
```
python manage.py migrate
```

12. <b id="installation-run-application">Run the application:</b> To execute the application, navigate to its directory in the command-line interface and run the appropriate command specified in the project's documentation. This command starts the app

```
python manage.py runserver 8080
```

13. <b id="installation-open-app">Open the app: </b>Congratulations! You can now access the app on your local machine by visiting [http://127.0.0.1:8080/](http://127.0.0.1:8080/) in your web browser.
---
