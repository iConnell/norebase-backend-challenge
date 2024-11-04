# norebase-backend-challenge

## Features

- **Retrieve Like Count**: Get the current number of likes on an article.
- **Like an Article**: Increment the like count of an article.
- **Concurrency Safety**: Uses atomic increments to handle high traffic without race conditions.

## Tech Stack

- **Backend**: Django Rest Framework
- **Database**: Sqlite

## Installation

### Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/iConnell/norebase-backend-challenge.git
   cd norbase-backend-challenge
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows, use

   ```
   venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL** (or other preferred relational database) and configure the `DATABASES` setting in `settings.py`.

5. **Run migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### `GET /api/articles/<article_id>/likes/`

**Description**: Retrieve the current like count of a specific article.

- **URL Parameters**: `article_id` - ID of the article.
- **Sample Response**:
  ```json
  {
    "status": "success",
    "data": {
      "like_count": 1
    }
  }
  ```

### `POST /api/articles/<article_id>/like/`

**Description**: Like a specific article, incrementing its like count.

- **URL Parameters**: `article_id` - ID of the article.
- **Sample Response**:
  ```json
  {
    "status": "success",
    "data": {
      "like_count": 1
    }
  }
  ```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Open a pull request to the main branch.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
