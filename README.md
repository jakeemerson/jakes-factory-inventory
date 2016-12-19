# jakes-factory-inventory

A REST api that allows users to manage a simple inventory for a factory.

* Create, Read, Update, and Delete (CRUD) methods for product manufacturers
* Create, Read, Update, and Delete (CRUD) methods for products in the inventory

# Installation

## Install initial dependencies

Since you are reading this you already know about git. Just to be thorough, make sure that a git client is installed on your local environment.

Next is a virtual environment for isolating the code. `virtualenvwrapper` is a great way to make sure that code doesn't fall prey to bugs or issues of incompatibility when updating external packages. Check out the instructions [here](http://virtualenvwrapper.readthedocs.io/en/latest/install.html) for installing this great tool. Assuming you have already installed Python and pip you can run the following commands to get started:

    pip install virtualenvwrapper
    mkdir factory
    cd factory
    mkvirtualenv factory
    

## Download and install the code

Once your virtual environment is set up it's time to pull down the git project:

    git clone git@github.com:jakeemerson/jakes-factory-inventory.git
    
Now, install the dependencies with:

    cd jakes-factory-inventory
    pip install -r requirements.txt
    
Note: There is also an Ansible playbook included to show an example of how this code can be deployed in a production environment. However, this is not fully working as I am not certain of the target environment.

## Run tests

The included tests demonstrate the requirements for CRUD methods on both the manufacturer and inventory item objects. Run tests with:

    cd factory
    python manage.py test --settings=settings
    
The last part is important because this package uses a non-standard scheme for managing the projects settings. This is to make it easier to switch settings between development, testing, and production environments. 

## Run the development server

You can play with the code via the handy interface provided by the django REST framework. First, start the development server:
 
     python manage.py runserver --settings=settings
     
and go to [http://127.0.0.1:8000/inventory/](http://127.0.0.1:8000/inventory/)

That's all!
