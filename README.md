
# FlaskEntityFilterAPI

A Flask-based API for filtering and managing individual and corporate entities with support for fuzzy name matching and date filtering.

## Features

- Filter individual and corporate (moral) entities based on name similarity and date of birth/creation.
- Supports fuzzy name matching to find similar entity names.
- Dynamically query different database tables based on the type of entity.
- CRUD operations for entity data management.
- Configurable through environment variables for easy deployment.

## Installation

### Prerequisites

- Python 3.6+
- pip

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FlaskEntityFilterAPI.git
   cd FlaskEntityFilterAPI
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the application, configure the environment variables as per your database and application setup. Create a `.env` file in the project root directory with the following variables:

- `DATABASE_URL`: The database connection URL, e.g., `sqlite:///yourdatabase.db`.
- `FLASK_ENV`: The environment for Flask to run in, e.g., `development` or `production`.
- `SECRET_KEY`: A secret key for securing sessions and cookies.

## Running the Application

1. Initialize the database (if using models that require a database):
   ```bash
   flask db upgrade
   ```

2. Start the Flask application:
   ```bash
   flask run
   ```

## Usage

### Filtering Entities

- To filter entities by name and date, send a `GET` request to `/entities` with the following query parameters:
  - `name`: The name of the entity to search for.
  - `date`: The date of birth or creation of the entity (format: `YYYY-MM-DD`).
  - `type`: The type of entity (`individual` or `corporate`).

Example:
```bash
curl -X GET "http://localhost:5000/entities?name=John Doe&date=1980-01-01&type=individual"
```

### Adding a New Entity

- To add a new entity, send a `POST` request to `/entities` with a JSON body containing the entity details.

Example:
```bash
curl -X POST "http://localhost:5000/entities" -H "Content-Type: application/json" -d '{"name": "New Entity", "date": "2000-01-01", "type": "individual"}'
```

## Development

### Adding New Features or Fixing Bugs

1. Create a new branch for your feature or bug fix.
2. Implement your changes.
3. Write or update tests as necessary.
4. Submit a pull request to the main branch.

### Running Tests

To run the test suite, use the following command:

```bash
pytest
```

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
