# StudyBuddy

StudyBuddy is a Django-based web application designed to help users find study partners, join study rooms, and collaborate on academic topics. The platform provides features such as user authentication, topic browsing, room creation, and activity tracking.

## Features

- **User Authentication**: Register, log in, and manage user profiles.
- **Study Rooms**: Create, join, and participate in study rooms.
- **Topics**: Browse and filter topics to find relevant study groups.
- **Activity Feed**: View recent activities and interactions.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Screenshots

## Project Structure

```
studyBud/
├── db.sqlite3
├── manage.py
├── studyBud/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── base/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── base/
│   │   │   ├── main.html
│   │   │   ├── room.html
│   ├── static/
│       ├── images/...
│       ├── css/
│       │   ├── styles.css
│       ├── js/
│       │   ├── scripts.js
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/studybuddy.git
   cd studybuddy
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/Scripts/activate  # On Windows
   source env/bin/activate      # On macOS/Linux
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Open the application in your browser at
   ```url
    [Domain](http://127.0.0.1:8000.)
   ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

This project was created while learning backend development in a YT channel named "Traversy Media". Checout the course to learn more. Also, you are welcome to use it or contribute in it.
