Platform Overview
Petstagram: WorkPal serves as a versatile platform connecting pet owners with potential pet sitters or caretakers.

Pet Sitting Listings and Application Functionality
Users can explore diverse pet sitting listings and seamlessly apply for various opportunities. Pet owners can post detailed listings, outlining their pet's needs and preferences to attract suitable sitters, while pet sitters can effortlessly browse and submit applications through the platform's interface.

Pet Care Projects
An additional feature offered by Petstagram: WorkPal is the ability to create pet care projects. Users can outline specific tasks they need to be completed, providing a flexible avenue for hiring pet care professionals on a project basis without the commitment of a long-term arrangement.

Conclusion
Petstagram: WorkPal's multifaceted approach provides a dynamic environment for both pet owners and pet sitters. With its diverse range of features, the platform facilitates seamless connections and collaborations in the pet care market.


Installation
To utilise this Django project, follow the steps below to set it up on your system.

Install Python
Confirm Python Installation
Install PostgreSQL
Confirm PostgreSQL installation
Clone the project
Create a virtual environment in the project directory
Activate the virtual environment
Install required packages to run the project
Configure database
Run makemigrations
Run migrate
Run the application
Open the application
Guide

Install Python: To run the project, ensure Python is installed on your machine. Although Python comes pre-installed on many Linux distributions, the version may vary depending on the distribution and operating system version. If Python is not installed, you can download it from here.

Confirm Python installation: To confirm the successful installation of Python, run the following command in your command line interface (CMD/Terminal...).

python3 --version
Please note the potential variations in the command based on how Python was installed on your system: some commands may begin with python, others with python3, and yet others with py. Despite the differences in reference, they all refer to the same command.

Install postgres: Download the installer from the PostgreSQL website and follow the installation instructions

Confirm PostgreSQL installation: To validate the successful installation of PostgreSQL, execute the subsequent command within your command line interface (CLI), whether it's CMD or Terminal.

postgres --version
Clone the project: Navigate to your preferred installation directory using your command-line interface, and proceed to clone the project. If you encounter any difficulties, you can find more information about cloning your project here.
Using HTTPS
git clone https://github.com/username/repository.git
Replace https://github.com/username/repository.git with the HTTPS URL you copied from GitHub.

Using SSH```
git clone ssh://git@github.com/username/repository.git
Substitute ssh://git@github.com/username/repository.git with the SSH URL you copied from GitHub. For instance:

Create a Virtual Environment: To effectively manage dependencies, versions, and ensure encapsulation, it's essential to create a virtual environment in the directory of your project using:
python3 -m venv ./venv
Activate the virtual Environment: Activating the virtual environment ensures that Python commands use the environment's interpreter and packages, avoiding conflicts with system-wide installations and maintaining consistency across projects.
source venv/bin/activate
Install required packages: After you have activated the venv, install the required packages to be able to run the project
pip install -r requirements.txt
Configure database: To ensure database access, configure it within the settings.py file of your project. The user
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
Run makemigrations: To check any changes in the defined models, execute the following command:
python manage.py makemigrations
Run migrate:To apply the pending database schema changes defined in migration files.
python manage.py migrate
Run the application: To execute the application, navigate to its directory in the command-line interface and run the appropriate command specified in the project's documentation. This command starts the app
python manage.py runserver 8080
Open the app: Congratulations! You can now access the app on your local machine by visiting http://127.0.0.1:8080/ in your web browser.
