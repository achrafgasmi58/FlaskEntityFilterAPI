###FlaskEntityFilterAPI

A Flask-based API for filtering and managing individual and corporate entities with support for fuzzy name matching and date filtering.

Features

Filter individual and corporate (moral) entities based on name similarity and date of birth/creation.
Supports fuzzy name matching to find similar entity names.
Dynamically query different database tables based on the type of entity.
CRUD operations for entity data management.
Configurable through environment variables for easy deployment.
Installation

Prerequisites
Python 3.6+
pip
Setup
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/FlaskEntityFilterAPI.git
cd FlaskEntityFilterAPI
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Set up your environment variables:
Create a .env file in the project root directory and configure your database URI and other settings:
env
Copy code
DATABASE_URI=mysql+pymysql://username:password@localhost:3306/database_name
Initialize the database:
Ensure your database server is running, then execute:
bash
Copy code
flask db upgrade
Run the Flask application:
bash
Copy code
flask run
Usage

Adding Data
POST /data
Adds a new entity to the database.
Filtering Data
POST /data/filter
Filters entities based on name similarity and date. Specify "Type_de_personne" in the request body to differentiate between individual and corporate entities.
Updating Data
PUT /data/<int:data_id>
Updates an existing entity by ID.
Deleting Data
DELETE /data/<int:data_id>
Deletes an entity by ID.
Development

To contribute to this project, please fork the repository and submit a pull request with your proposed changes.

License

This project is licensed under the MIT License - see the LICENSE file for details.
