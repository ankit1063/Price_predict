FOR FLASK 
Flask supports Python 3.7 and newer.


For creating an Environment 
> mkdir myproject
> cd myproject
> py -3 -m venv venv


For Activating the Environment
> venv\Scripts\activate



Installing Flask
> $ pip install Flask


To run the flask server 
> FLASK_APP=”app”
> Python -m flask run 



FOR HEROKU 
Install Heroku from DOWNLOAD 


Create a file named procfile, 
→ web: gunicorn app:app --preload


Create a file named requirements.txt using command freeze > requirements.txt
category-encoders==2.4.0
click==8.0.4
colorama==0.4.4
cycler==0.11.0
Flask==2.0.3
fonttools==4.31.2
gunicorn==20.1.0
imbalanced-learn==0.9.0
itsdangerous==2.1.0
Jinja2==3.0.3
joblib==1.1.0
MarkupSafe==2.1.0
numpy==1.22.2
packaging==21.3
pandas==1.4.1
patsy==0.5.2
pyparsing==3.0.7
python-dateutil==2.8.2
pytz==2021.3
scikit-learn==1.0.2
scipy==1.8.0
six==1.16.0
sklearn==0.0
statsmodels==0.13.2
threadpoolctl==3.1.0
Werkzeug==2.0.3
xgboost==1.5.2


In order to deploy, it should be in the form of a github repo. Follow this commands:
> git init
> git add .
> git commit -m “Message”


To push the code into Heroku 
> heroku login (Fill the login details)
> heroku create (Click on the link)
eg - https://still-stream-97789.herokuapp.com/
> git push heroku main 


To check the logs 
> heroku logs --tail