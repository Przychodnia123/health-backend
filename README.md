# Health-backend project
> A Django-based backend application designed to manage and operate a medical clinic. 
> It among others allows user registration, patient management, appointment scheduling, prescription issuing, and test result handling.


## General Information
The project is built on the Django framework and Django REST Framework. The application enables among others the management of patient data, appointment scheduling, prescription issuing, and the addition of test results.

### Available Endpoints

#### List of All Users
- **URL**: `localhost/api/users`
- **Method**: `GET`
- **Headers Required**:
  - Key: `Authorization`
  - Value: `token 'your_token_here'`

#### User Registration
- **URL**: `http://localhost:8000/api/healthapp/register/`
- **Method**: `POST`
- **Body Required**:
  ```json
  {
    "username": "username",
    "password": "userpassword",
    "password2": "userpassword",
    "email": "useremail"
  }

#### User Login
- **URL**: `http://localhost:8000/api/healthapp/login/`
- **Method**: `POST`
- **Body Required**:
  ```json
  {
    "username": "username",
    "password": "userpassword",
    "password2": "userpassword"
  }


#### User Logout
- **URL**: `http://localhost:8000/api/healthapp/logout/`
- **Method**: `POST`
- **Headers Required**:
  - Key: `Authorization`
  - Value: `token 'your_token_here'`


## Setup
1. Clone the Repository `git clone https://github.com/Przychodnia123/health-backend.git`

2. Create and Activate Virtual Environment
`python -m venv myenv`
source myenv/bin/activate  # On Windows, use: myenv\Scripts\activate

3. Environment Configuration
Create a `.env` file in the root directory and add the following configurations:  ```
    DEBUG=True
    ```
    For local development, you also add the `SECRET_KEY`:
    ```
    SECRET_KEY='your_secret_key_here'
    ```

4. Install Dependencies
`pip install -r requirements.txt`


5. Database Migration```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

**Run the Project**:
    ```bash
    python manage.py runserver
    ```

## Notes
Ensure you have configured the appropriate local settings and updated the `.env` file with keys and configuration settings. **Important**: Always keep your `SECRET_KEY` confidential and do not expose it on GitHub or any public repositories.
