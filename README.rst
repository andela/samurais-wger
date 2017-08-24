.. image:: https://travis-ci.org/andela/samurais-wger.svg?branch=ch-circleci-coveralls-149839245
    :target: https://travis-ci.org/andela/samurais-wger
.. image:: https://coveralls.io/repos/github/andela/samurais-wger/badge.svg?branch=ch-circleci-coveralls-149839245
    :target: https://coveralls.io/github/andela/samurais-wger?branch=ch-circleci-coveralls-149839245
.. image:: https://codeclimate.com/github/andela/samurais-wger/badges/gpa.svg
    :target: https://codeclimate.com/github/andela/samurais-wger
    :alt: Code Climate
.. image:: https://codeclimate.com/github/andela/samurais-wger/badges/issue_count.svg
    :target: https://codeclimate.com/github/andela/samurais-wger
    :alt: Issue Count

Thank you for downloading wger Workout Manager. wger (ˈvɛɡɐ) is a free, open source web
application that manages your exercises and personal workouts, weight and diet
plans. It can also be used as a simple gym management utility, providing different
administrative roles (trainer, manager, etc.). It offers a REST API as well, for
easy integration with other projects and tools.

It is written with python/django and uses jQuery and some D3js for charts.

For more details and a live system, refer to the project's site: https://samurais-wger.herokuapp.com/


Installation
============

These are the basic steps to install and run the application locally on a linux
system. There are more detailed instructions, other deployment options as well
as an administration guide available locally in your code repository in the docs
folder (``make html`` to compile, then open_build/index.html).

Please consult the commands' help for further information and available
parameters.


Development version (from git)
------------------------------

**Note:** You can safely install from master, it is almost always in a usable
and stable state.


1) Install the necessary packages

::

 $ sudo apt-get install python3-dev python-virtualenv nodejs nodejs-legacy npm libjpeg8-dev zlib1g-dev git


On fedora 23

::

 $ sudo dnf install python3-devel python-virtualenv nodejs npm libjpeg-turbo-devel zlib-devel git

Then install the python packages from pypi in the virtualenv::

 $ virtualenv --python python3 venv-django
 $ source venv-django/bin/activate


2) Start the application. This will download the required JS and CSS libraries
   and create a SQlite database and populate it with data on the first run.

::

 $ git clone https://github.com/wger-project/wger.git
 $ cd wger
 $ pip install -r requirements.txt  # or requirements_devel.txt to develop
 $ invoke create-settings \
          --settings-path ./settings.py \
          --database-path ./database.sqlite
 $ invoke bootstrap-wger \
          --settings-path ./settings.py \
          --no-start-server
 $ python manage.py runserver

3) Log in as: **admin**, password **admin**

After the first run you can just use django's development server. You will
probably want to move the settings and sqlite files to your git folder, see
the comments in the documentation (development chapter) about this::

 $ python manage.py runserver


Command line options
--------------------

The available options for ``invoke`` are the following ::


  bootstrap-wger          Performs all steps necessary to bootstrap the application
  config-location         Returns the default location for the settings file and the data folder
  create-or-reset_admin   Creates an admin user or resets the password for an existing one
  create-settings         Creates a local settings file
  load-fixtures           Loads all fixtures
  migrate-db              Run all database migrations
  start-wger              Start the application using django's built in webserver

Contact
=======

Feel free to contact us if you found this useful or if there was something that
didn't behave as you expected. We can't fix what we don't know about, so please
report liberally. If you're not sure if something is a bug or not, feel free to
file a bug anyway.

* **issue tracker:** https://github.com/andela/samurais-wger/issues


Sources
=======

All the code and the content is freely available:

* **Main repository:** https://github.com/andela/samurais-wger


Licence
=======

The application is licenced under the Affero GNU General Public License 3 or
later (AGPL 3+).

The initial exercise and ingredient data is licensed additionally under one of
the Creative Commons licenses, see the individual exercises for more details.

The documentation is released under a CC-BY-SA either version 4 of the License,
or (at your option) any later version.

Some images where taken from Wikipedia, see the SOURCES file in their respective
folders for more details.
