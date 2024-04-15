# StudyBuddy

A platform to optimize your productivity by allowing you to seamlessly reserve a spot at a conducive study area, purchase any study material you need from our specially curated product store, or seek help from our 24/7 AI Buddy on your work!

# Accessing our Platform

View our live platform at this URL ```https://studybuddyswe.vercel.app```

# Running Locally

1. Clone the repository ```git clone https://github.com/jaredpek/StudyBuddy```
2. Install front-end dependencies
    - Navigate to the front-end directory ```cd application/frontend```
    - Install all dependencies ```npm install```
    - Create a new .env file with the following variables ```nano .env``` <br/>
    ```
    VITE_BACKEND_URL="http://127.0.0.1:8000"
    ```
    - Build the application ```npm run build```
3. Install back-end dependencies
    - Navigate to the back-end directory ```cd application/backend/project```
    - Initialise python virtual environment ```python -m venv venv```
    - Activate python virtual environment ```venv/Scripts/activate```
    - Install all dependencies ```pip install -r requirements.txt```
    - Create a new .env file with the following variables ```nano .env``` <br />
    ```
    ENVIRONMENT="DEVELOPMENT"
    DJANGO_SECRET_KEY="<alphanumeric string of length 64>"
    DJANGO_JWT_SIGNING_KEY="<alphanumeric string of length 64>"
    DJANGO_JWT_ALGORITHM="HS512"
    DJANGO_JWT_LIFETIME="14"
    DJANGO_BACKEND_URL="http://127.0.0.1:8000"
    DJANGO_DEBUG="True"
    GMAP_SECRET="<google maps API key>"
    GEMINI_API="<gemini API key>"
    ```
4. Run the application
    - Run the front-end ```npm run preview```
    - Run the back-end ```python manage.py runserver```
    - Access the front-end via ```http://localhost:4173```
    - Access the back-end via ```http://127.0.0.1:8000```

# Accessing Documentation
1. Front-End
    - Navigate to the documentation folder ```cd application/frontend/documentation```
    - Open the ```index.html``` file in the browser
    - View the documentation for all available JSX in the ```global``` pane on the right
2. Back-End
    - Run the django back-end ```python manage.py runserver```
    - Navigate to ```http://127.0.0.1:8000/documentation```
        - Username and Password will be provided seperately
