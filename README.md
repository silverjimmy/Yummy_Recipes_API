#Yummy_Recipes_Api

## Introduction
Flask API


## Installation

* Navigate to the application directory:

```
cd Yummy_Recipes_Api
```

* Create a virtual environment to install the
application in. You could install virtualenv and virtualenvwrapper.
Within your virtual environment, install the application package dependencies with:

```
pip install -r requirements.txt
```

* Run the application with:

```
python run.py
```

#### URL endpoints

| URL Endpoint | HTTP Methods | Summary |
| -------- | ------------- | --------- |
| `/auth/register/` | `POST`  | Register a new user|
| `/auth/login/` | `POST` | Login and retrieve token|
| `/recipes/` | `POST` | Create a new Recipe |
| `/recipes/` | `GET` | Retrieve all recipes for user |
| `/recipes/<id>/` | `GET` |  Retrieve recipe list details |
| `/recipes/<id>/` | `PUT` | Update recipe list details |
| `/recipes/<id>/` | `DELETE` | Delete a recipe list |
| `/recipes/<id>/categories/` | `POST` |  Create categories in a recipe list |
| `/recipes/<id>/categories/<catergory_id>/` | `DELETE`| Delete a category in a recipe list|
| `/recipes/<id>/categories/<catergory_id>/` | `PUT`| update a recipe list category details|
