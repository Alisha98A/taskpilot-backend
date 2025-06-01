
## Testing

### Manual testing

<details>
<summary> User Stories and Epics</summary>  
<br>

---

### **EPIC – Task Management**

| Goals | How are they achieved? | Comment |
| --- | --- | --- |
| As an authenticated user, I want to create a new task so I can manage my responsibilities | API endpoint `/api/tasks/` with POST method, using TaskSerializer | |
| As an authenticated user, I want to view a list of my tasks | API endpoint `/api/tasks/` with GET method filtered by user | |
| As an authenticated user, I want to view task details including attached notes | Detail view at `/api/tasks/<id>/` returns nested notes via TaskWithNotesSerializer | |
| As an authenticated user, I want to update a task | API endpoint `/api/tasks/<id>/` with PUT method, protected by IsOwnerOnly permission | |
| As an authenticated user, I want to delete a task I no longer need | DELETE request to `/api/tasks/<id>/` | |
| As an authenticated user, I want tasks to automatically be marked as overdue | Overridden `save()` method on Task model checks due date | |

---

### **EPIC – Notes System**

| Goals | How are they achieved? | Comment |
| --- | --- | --- |
| As an authenticated user, I want to create a note attached to a task | API POST to `/api/notes/`, task is required and must belong to the user | |
| As an authenticated user, I want to view all my notes | GET request to `/api/notes/` only returns notes by the current user | |
| As an authenticated user, I want to edit a note | PUT/PATCH request to `/api/notes/<id>/` | |
| As an authenticated user, I want to delete a note I no longer need | DELETE request to `/api/notes/<id>/` | |

---

### **EPIC – Authentication & Session Management**

| Goals | How are they achieved? | Comment |
| --- | --- | --- |
| As a new user, I want to register for an account | Endpoint `/api/dj-rest-auth/registration/` using dj-rest-auth | |
| As a returning user, I want to log in and receive a JWT | Endpoint `/api/dj-rest-auth/login/`, returns access and refresh tokens | |
| As a logged-in user, I want to log out securely | Endpoint `/api/dj-rest-auth/logout/`, using `logout_route` view | |
| As a user, I want to refresh my JWT to stay logged in | Endpoint `/api/token/refresh/` | |

---

### **EPIC – Contact & Feedback**

| Goals | How are they achieved? | Comment |
| --- | --- | --- |
| As a user, I want to submit a message for support | POST request to `/api/contact/` | |
| As an admin, I want to view all submitted messages | GET request to `/api/contact/messages/`, protected with `IsAdminUser` | |

---

### **EPIC – Permissions and Security**

| Goals | How are they achieved? | Comment |
| --- | --- | --- |
| As an authenticated user, I want to only access my own data | All task/note queries filter by request.user; permissions enforced | |
| As an unauthorized user, I should be blocked from others’ content | Custom permission class `IsOwnerOnly` applied to detail views | |
| As an admin, I want to access all contact messages | Contact list view uses `IsAdminUser` permission | |

</details>

_<span style="color: blue;">[Back to Content](#table-of-contents)</span>_


## Validator Testing

### JSX

I have used jsx-Prettier and ESLint throughout the development to check that my JSX and JavaScript meet the standards for clean code.

### HTML

I validated my HTML pages using the W3 Nu HTML Checker. They came back with no errors, only pointers about redundant trailing slashes left by React. Please check the results for each page below.

<details>
<summary>HTML validation results</summary>

[Homepage](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftaskpilot-backend-6ee557f05c5b.herokuapp.com%2F)
[Sign in Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftaskpilot-backend-6ee557f05c5b.herokuapp.com%2Fsignin)
[Sign up Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftaskpilot-backend-6ee557f05c5b.herokuapp.com%2Fsignup)
[Dashboard](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftaskpilot-backend-6ee557f05c5b.herokuapp.com%2Fdashboard)
[Task list page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftaskpilot-backend-6ee557f05c5b.herokuapp.com%2Ftasks)
[Create task page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftaskpilot-backend-6ee557f05c5b.herokuapp.com%2Ftasks%2Fcreate)
[Edit task](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftaskpilot-backend-6ee557f05c5b.herokuapp.com%2Ftasks%2F24%2Fedit)
[Task detail](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftaskpilot-backend-6ee557f05c5b.herokuapp.com%2Ftasks%2F6)
[Notes list page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftaskpilot-backend-6ee557f05c5b.herokuapp.com%2Fnotes)
[Note detail](https://taskpilot-backend-6ee557f05c5b.herokuapp.com/notes/79)
[Note edit](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftaskpilot-backend-6ee557f05c5b.herokuapp.com%2Fnotes%2Fid%2Fedit)
[Note delete](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftaskpilot-backend-6ee557f05c5b.herokuapp.com%2Fnotes%2Fid%2Fdelete)
[Contact page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftaskpilot-backend-6ee557f05c5b.herokuapp.com%2Fcontact)

</details>

_<span style="color: blue;">[Back to Content](#table-of-contents)</span>_


### CSS

This script uses the [W3C CSS Validator](http://jigsaw.w3.org/css-validator/validator) 

### Automated testing


#### Backend API Automated Testing

I implemented comprehensive automated tests for the API endpoints related to the core app functionalities: Tasks, Notes, and Contact messages.

- The tests cover **CRUD operations** (Create, Read, Update, Delete) for tasks and notes, verifying that authenticated users can manage their own data securely.
- Contact API tests ensure that users can submit messages, and only admin users can list all contact messages, enforcing proper permissions.
- Authentication is simulated using Django REST Framework’s `APIClient` with forced user authentication to test endpoints in a secure context.
- Each test verifies both the HTTP response status codes and the changes in the database, confirming that the API behaves as expected.
- All 11 tests passed successfully, demonstrating that the API endpoints are stable and meet the specified user stories and requirements.

This testing ensures robustness of the API and helps prevent regressions during further development.


![Backend testing](documentation/testing/testbackend.png)


### Validator testing


![Test for validators.py](documentation/testing/test_test_validators_py.png)
![Test for models.py](documentation/testing/test_test_models_py.png)



# Bug: Favicon and Static File Path Errors on Deployment

## Problem

After deployment, the application displayed **404 Not Found** errors for the following favicon-related files:

- `/favicon_io/logo.png`
- `/favicon_io/site.webmanifest`

Additionally, there were issues with Django not properly collecting or serving some static files from the React build.

## Cause

- The favicon files were located in `staticfiles/favicon_io/`, but the React app expected them at `/static/favicon_io/`.
- `collectstatic` was not moving or recognizing some assets because of incorrect folder structure or `STATICFILES_DIRS` misconfiguration.

## Solution

1. **Moved Favicon Files**  
   Moved the favicon assets into the React build path:  
   `staticfiles/build/favicon_io/`

2. **Updated Django Settings**  
   In `settings.py`, configured static settings to serve React and Django assets correctly.


3. **Committed React Build**  
   The built React files inside `staticfiles/build/` were committed to Git to ensure they are available on Heroku during deployment.

4. **Collected Static Files**  
   Ran:

```bash
   python manage.py collectstatic --noinput
```

```bash
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles' / 'build' / 'static',  # React static files
]

This gathered Django admin static files and merged them with the React build in the staticfiles directory.

STATIC_ROOT = BASE_DIR / 'staticfiles'
WHITENOISE_ROOT = BASE_DIR / 'staticfiles' / 'build'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```