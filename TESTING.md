
## Testing

### Manual testing

### Automated testing

### Validator testing


![Test for validators.py](documentation/testing/test_test_validators_py.png)
![Test for models.py](documentation/testing/test_test_models_py.png)




🐞 Bug: Favicon and Static File Path Errors on Deployment

❗️Problem

After deployment, the application displayed 404 Not Found errors for the following favicon-related files:
	•	/favicon_io/logo.png
	•	/favicon_io/site.webmanifest

Additionally, there were issues with Django not properly collecting or serving some static files from the React build.

🔍 Cause
	•	The favicon files were located in staticfiles/favicon_io/, but the React app expected them at /static/favicon_io/.
	•	collectstatic was not moving or recognizing some assets because of incorrect folder structure or STATICFILES_DIRS misconfiguration.

✅ Solution
	1.	Moved Favicon Files
Moved the favicon assets into the React build path:
staticfiles/build/favicon_io/
	2.	Updated Django Settings
In settings.py, configured static settings to serve React and Django assets correctly:




STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles' / 'build' / 'static',  # React static files
]

STATIC_ROOT = BASE_DIR / 'staticfiles'
WHITENOISE_ROOT = BASE_DIR / 'staticfiles' / 'build'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


	3.	Committed React Build
The built React files inside staticfiles/build/ were committed to Git to ensure they are available on Heroku during deployment.
	4.	Collected Static Files
Ran:

python manage.py collectstatic --noinput

This gathered Django admin static files and merged them with the React build in the staticfiles directory.