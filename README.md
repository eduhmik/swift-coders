# swift-coders
Agile group project that allows normal users to create and edit their own comments, moderators to create and delete comments and admins have the ability to edit or delete any comment.

# Installation and Setup
Clone the repository.
```bash
git clone https://github.com/eduhmik/swift-coders.git
```
## Navigate to the app folder
```bash
cd swift-coders
```

## Create a virtual environment

```bash
$ python3 -m venv venv;
$ source venv/bin/activate
```
On Windows
```bash
py -3 -m venv venv
```
If you need to install virtualenv because you are on an older version of Python:
```bash
virtualenv venv
```
On Windows
```bash
\Python27\Scripts\virtualenv.exe venv
```

## Activate the virtual environment
Before you begin you will need to activate the corresponding environment
```bash
source venv/bin/activate
```
On Windows
```bash
venv\Scripts\activate
```

## Install requirements
```bash
$ pip install -r requirements.txt
```

## Running the application
After the configuration, you will run the app 
```bash
$ export FLASK_APP=run.py
$ flask run
```





