## Screenshots

The following screenshots should be taken and uploaded to this **screenshots** folder:

1. **Migrate Web Applications - 2 Screenshots**
 - Screenshot of Azure Resource showing the **App Service Plan**.
 - Screenshot of the deployed Web App running. The screenshot should be fullscreen showing the URL and application running.
2. **Migrate Database - 2 Screenshots**
 - Screenshot of the Azure Resource showing the **Azure Database for PostgreSQL server**.
 - Screenshot of the Web App successfully loading the list of **attendees** and **notifications** from the deployed website.
3. **Migrate Background Process - 4 Screenshots**
 - Screenshot of the Azure Function App running in Azure, showing the **function name** and the **function app plan**.
 - Screenshots of the following showing functionality of the deployed site:
    1. Submitting a new notification.
      - Screenshot of filled out **Send Notification** form.
    2. Notification processed after executing the Azure function.
      - Screenshot of the **Email Notifications List** showing the notification status as **Notifications submitted**.
      - Screenshot of the **Email Notifications List** showing the notification status as **Notified X attendees**.



# 1. How to set Up giveateach
# 2. Clone the project or fork the project 
# 3. create a Postgres DB. The details are in the flask.cfg file in the instance folder
# 4. Create a virtual environment on your local repository named "flask_env" and activate it 
# 5. Run these command from the main repository: 
#    set FLASK_APP=giveateach.py
#    pip install -r requirements.txt
#    flask db init
#    flask db migrate
#    flask db upgrade
#    create_admin.py

# 4. finally, run "app.py" to get the app running on your local server.


#  How to set Up giveateach
# 1. Installed python 3.7 and added python to "PATH" during the installation process. Check for other   version of python installed on your system and remove or update to python 3.7 before installing
# 2. Clone the project or fork the project 
# 3. create a Postgres DB. The details are in the "flask.cfg" file in the instance folder
# 4. On your CMD terminal, navigate to the project main directory and do the following:
# 4.1 Create a virtual environment with this command "python -m venv flask_env" and enter
# 4.2 Navigate to the newly created "flask_env" folder and move to the "bin" folder or "scripts" folder (depending on your OS) and type "activate" and enter
# Your directory listing on your CMD terminal should look like this 
# "(flask_env) C:\Users\DELL\giveateach>" when you successfully activate the virtual environment
# 5. on CMD terminal, run these commands one after another from the main project repository repository: 
#    pip install -r requirements.txt
#    set FLASK_APP=giveateach.py
#    flask db init
#    flask db migrate
#    flask db upgrade
#    create_admin.py
#6. finally, run "app.py" to get the app running on your local server.
