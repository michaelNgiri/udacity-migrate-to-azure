# TechConf Registration Website

## Project Overview
The TechConf website allows attendees to register for an upcoming conference. Administrators can also view the list of attendees and notify all attendees via a personalized email message.

The application is currently working but the following pain points have triggered the need for migration to Azure:
 - The web application is not scalable to handle user load at peak
 - When the admin sends out notifications, it's currently taking a long time because it's looping through all attendees, resulting in some HTTP timeout exceptions
 - The current architecture is not cost-effective 

In this project, you are tasked to do the following:
- Migrate and deploy the pre-existing web app to an Azure App Service
- Migrate a PostgreSQL database backup to an Azure Postgres database instance
- Refactor the notification logic to an Azure Function via a service bus queue message

## Dependencies

You will need to install the following locally:
- [Postgres](https://www.postgresql.org/download/)
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Azure Function tools V3](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash#install-the-azure-functions-core-tools)
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
- [Azure Tools for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack)

## Project Instructions

### Part 1: Create Azure Resources and Deploy Web App
1. Create a Resource group
2. Create an Azure Postgres Database single server
   - Add a new database `techconfdb`
   - Allow all IPs to connect to database server
   - Restore the database with the backup located in the data folder
3. Create a Service Bus resource with a `notificationqueue` that will be used to communicate between the web and the function
   - Open the web folder and update the following in the `config.py` file
      - `POSTGRES_URL`
      - `POSTGRES_USER`
      - `POSTGRES_PW`
      - `POSTGRES_DB`
      - `SERVICE_BUS_CONNECTION_STRING`
4. Create App Service plan
5. Create a storage account
6. Deploy the web app

### Part 2: Create and Publish Azure Function
1. Create an Azure Function in the `function` folder that is triggered by the service bus queue created in Part 1.

      **Note**: Skeleton code has been provided in the **README** file located in the `function` folder. You will need to copy/paste this code into the `__init.py__` file in the `function` folder.
      - The Azure Function should do the following:
         - Process the message which is the `notification_id`
         - Query the database using `psycopg2` library for the given notification to retrieve the subject and message
         - Query the database to retrieve a list of attendees (**email** and **first name**)
         - Loop through each attendee and send a personalized subject message
         - After the notification, update the notification status with the total number of attendees notified
2. Publish the Azure Function

### Part 3: Refactor `routes.py`
1. Refactor the post logic in `web/app/routes.py -> notification()` using servicebus `queue_client`:
   - The notification method on POST should save the notification object and queue the notification id for the function to pick it up
2. Re-deploy the web app to publish changes

## Monthly Cost Analysis
Complete a month cost analysis of each Azure resource to give an estimate total cost using the table below:

| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
| *Azure Postgres Database* |   basic compute gen5 & basic storage  |       $1.45       |
| *Azure Service Bus*   |      --  |     < $0.01         |
| *Azure App Service Plan* | Basic Tier | < $0.0.1 |
| *Azure App Service*                   |      Free Tier   |       $0       |
| *Azure Storage Account* | bandwidth & tables & tiered block blob | < $0.01 |

## Architecture Explanation
_ _This is a placeholder section where you can provide an explanation and reasoning for your architecture selection for both the Azure Web App and Azure Function._

The archicture selected for this app, is basead on following key points:
- Decoupling app behavior to improve code quality, enable separates teams and releases
- Better scale for each component of the app
- Better pay out of the app, because instead of paying for the total app we'll pay for each component

For this app, which is not so big we choose to deploy it in Azure because the SaaS service for Web Apps and Serveless Apps. In Azure, for Web and Function Apps we can use the free tier and also scale up or down basead on the trafic of our app. Given that we have decoupled the app into frontend and functions also we enable the ability to do separate releases and scales which is better for the cost-effectiveness.

---
## Project Rubric

App URI: https://nd081-c3-web-dev.azurewebsites.net

## Architecture Explanation

The archicture selected for this app, is basead on following key points:
- Decoupling app behavior to improve code quality, enable separates teams and releases
- Better scale for each component of the app
- Better pay out of the app, because instead of paying for the total app we'll pay for each component

For this app, which is not so big we choose to deploy it in Azure because the SaaS service for Web Apps and Serveless Apps. In Azure, for Web and Function Apps we can use the free tier and also scale up or down basead on the trafic of our app. Given that we have decoupled the app into frontend and functions also we enable the ability to do separate releases and scales which is better for the cost-effectiveness. 

## Monthly Cost Analysis

| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
| *Azure Postgres Database* |   basic compute gen5 & basic storage  |       $1.45       |
| *Azure Service Bus*   |      --  |     < $0.01         |
| *Azure App Service Plan* | Basic Tier | < $0.0.1 |
| *Azure App Service*                   |      Free Tier   |       $0       |
| *Azure Storage Account* | bandwidth & tables & tiered block blob | < $0.01 |
| *Azure Cache for Redis* | Basic tier | $0.22 |
| *SendGrid for Azure* | Free Tier | $0 |

## Screenshots
Please take a look at the folder `screenshots`, there we have all available screenshots of the app and environment.

#### About the requirements,

1. Migrate Web Applications - 2 Screenshots

   11. Screenshot of Azure Resource showing the App Service Plan.
   
         File: `screenshots/az_web_app_view_.png`

   12. Screenshot of the deployed Web App running. The screenshot should be fullscreen showing the URL and application running.

         File: `screenshots/app_running_.png`

2. Migrate Database - 2 Screenshots

   21. Screenshot of the Azure Resource showing the Azure Database for PostgreSQL server.

         File: `screenshots/az_database_view_.png`

   22. Screenshot of the Web App successfully loading the list of attendees and notifications from the deployed website.

         Files:
         - `screenshots/app_attendees_list_view_.png`
         - `screenshots/app_notification_status_list_view_.png`

3. Migrate Background Process - 4 Screenshots

   31. Screenshot of the Azure Function App running in Azure, showing the function name and the function app plan.

         File: `screenshots/az_function_view.png`

   32. Screenshots of the following showing functionality of the deployed site:

         321. Submitting a new notification.
         
               File: `screenshots/app_before_sending_notification_empty_full_view.png`

         322. Screenshot of filled out Send Notification form.

               File: `screenshots/app_before_sending_notification_full_view.png`


4. Notification processed after executing the Azure function.

   41. Screenshot of the Email Notifications List showing the notification status as Notifications submitted.

         File: `screenshots/app_after_sending_notification_submitted_view.png`

   42. Screenshot of the Email Notifications List showing the notification status as Notified X attendees.

         File: `screenshots/app_after_sending_notification_full_view.png`

#### And more,

