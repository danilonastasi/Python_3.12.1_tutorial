
##### Python 3.12.1 tutorial from the link: https://www.python.org/ --> Docs #####
##### 01/11/2024 #####

##### tested on ________ -  Microsoft Windows - Python 3.12.0 (Oct  2 2023) #####


##### 12. Virtual Environments and Packages #####


##### 12.1. Introduction #####

# Python applications will often use packages and modules that don’t come as part 
# of the standard library. Applications will sometimes need a specific version of 
# a library, because the application may require that a particular bug has been 
# fixed or the application may be written using an obsolete version of the library’s 
# interface.

# This means it may not be possible for one Python installation to meet the 
# requirements of every application. If application A needs version 1.0 of a 
# particular module but application B needs version 2.0, then the requirements 
# are in conflict and installing either version 1.0 or 2.0 will leave one 
# application unable to run.

# The solution for this problem is to create a virtual environment, a self-contained 
# directory tree that contains a Python installation for a particular version of 
# Python, plus a number of additional packages.

# Different applications can then use different virtual environments. To resolve 
# the earlier example of conflicting requirements, application A can have its own 
# virtual environment with version 1.0 installed while application B has another 
# virtual environment with version 2.0. If application B requires a library be 
# upgraded to version 3.0, this will not affect application A’s environment.


##### 12.2. Creating Virtual Environments #####

# The module used to create and manage virtual environments is called venv. 
# venv will usually install the most recent version of Python that you have available. 
# If you have multiple versions of Python on your system, you can select a specific 
# Python version by running python3 or whichever version you want.

# To create a virtual environment, decide upon a directory where you want to place 
# it, and run the venv module as a script with the directory path:

python -m venv tutorial-env  # creates the tutorial-env directory in the path where
                             # I run th code in the windows prompt

# This will create the tutorial-env directory if it doesn’t exist, and also create 
# directories inside it containing a copy of the Python interpreter and various 
# supporting files.

# A common directory location for a virtual environment is .venv. This name keeps 
# the directory typically hidden in your shell and thus out of the way while 
# giving it a name that explains why the directory exists. It also prevents 
# clashing with .env environment variable definition files that some tooling 
# supports.

# Once you’ve created a virtual environment, you may activate it.

# On Windows, run:

tutorial-env\Scripts\activate

# On Unix or MacOS, run:

source tutorial-env/bin/activate

# (This script is written for the bash shell. If you use the csh or fish shells, 
# there are alternate activate.csh and activate.fish scripts you should use instead.)

# Activating the virtual environment will change your shell’s prompt to show what 
# virtual environment you’re using, and modify the environment so that running python 
# will get you that particular version and installation of Python. For example:

# $ source ~/envs/tutorial-env/bin/activate
# (tutorial-env) $ python
# Python 3.5.1 (default, May  6 2016, 10:59:36)
#  ...

import sys
sys.path
# ['', '/usr/local/lib/python35.zip', ...,
# '~/envs/tutorial-env/lib/python3.5/site-packages']

# To deactivate a virtual environment, type:

deactivate

# into the terminal (windows prompt)  -->

quit()
deactivate


##### 12.3. Managing Packages with pip #####

# You can install, upgrade, and remove packages using a program called pip. By 
# default pip will install packages from the Python Package Index. You can browse 
# the Python Package Index by going to it in your web browser.

# pip has a number of subcommands: “install”, “uninstall”, “freeze”, etc. 
# (Consult the Installing Python Modules guide for complete 
# documentation for pip.)  -->

    ##### Installing Python Modules ####

    # Key terms

      # - pip is the preferred installer program. Starting with Python 3.4, it is 
      #   included by default with the Python binary installers.

      # - A virtual environment is a semi-isolated Python environment that allows 
      #   packages to be installed for use by a particular application, rather 
      #   than being installed system wide.

      # - venv is the standard tool for creating virtual environments, and has been 
      #   part of Python since Python 3.3. Starting with Python 3.4, it defaults 
      #   to installing pip into all created virtual environments.

      # - virtualenv is a third party alternative (and predecessor) to venv. It 
      #    allows virtual environments to be used on versions of Python prior to 3.4, 
      #    which either don’t provide venv at all, or aren’t able to automatically install pip into created environments.

      # - The Python Package Index is a public repository of open source licensed 
      #   packages made available for use by other Python users.

      # - the Python Packaging Authority is the group of developers and documentation 
      #   authors responsible for the maintenance and evolution of the standard 
      #   packaging tools and the associated metadata and file format standards. 
      #   They maintain a variety of tools, documentation, and issue trackers on 
      #   GitHub.

      # - distutils is the original build and distribution system first added to 
      #   the Python standard library in 1998. While direct use of distutils is 
      #   being phased out, it still laid the foundation for the current packaging 
      #   and distribution infrastructure, and it not only remains part of the 
      #   standard library, but its name lives on in other ways (such as the name of 
      #   the mailing list used to coordinate Python packaging standards development).

    # Changed in version 3.5: The use of venv is now recommended for creating 
    # virtual environments.

    ##### Basic usage #####

    # The standard packaging tools are all designed to be used from the command line.
    # (Maybe is the windows prompt???)

    # The following command will install the latest version of a module and its 
    # dependencies from the Python Package Index:

    python -m pip install SomePackage

    # I think is the same as:

    pip install SomePackage

    ## Note For POSIX users (including macOS and Linux users), the examples in this 
    #  guide assume the use of a virtual environment.
    # For Windows users, the examples in this guide assume that the option to 
    # adjust the system PATH environment variable was selected when installing Python.

    # It’s also possible to specify an exact or minimum version directly on the 
    # command line. When using comparator operators such as >, < or some other 
    # special character which get interpreted by shell, the package name and the 
    # version should be enclosed within double quotes:

    python -m pip install SomePackage==1.0.4    # specific version
    python -m pip install "SomePackage>=1.0.4"  # minimum version

    # Normally, if a suitable module is already installed, attempting to install it 
    # again will have no effect. Upgrading existing modules must be requested 
    # explicitly:

    python -m pip install --upgrade SomePackage

    # More information and resources regarding pip and its capabilities can be found 
    # in the Python Packaging User Guide.

    # Creation of virtual environments is done through the venv module. 
    # Installing packages into an active virtual environment uses the commands 
    # shown above.

