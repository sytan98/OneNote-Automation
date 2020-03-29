# OneNote-Automation

The goal of this program is to automate the process of creating notes in class. Every single time there is a new lecture. The process of downloading the slides from blackboard and attaching into OneNote can be minimised.

## Goal:
1. Utilise Microsoft Graph OneNote API to create a new notebook in the right section
2. Use Graph API to check OneDrive for new slides to include into notes
3. Maybe find a way to use blackboard API
4. Automate this process by using crontabing it on an EC2 instance

## Microsoft Graph API:
The Microsoft Graph API offers a single endpoint, https://graph.microsoft.com, to provide access to rich, people-centric data and insights exposed as resources of Microsoft 365 services. You can use REST APIs or SDKs to access the endpoint and build apps that support scenarios spanning across productivity, collaboration, education, security, identity, access, device management, and much more.

In this case, I will be mainly using the API to access OneNote and OneDrive.

### Authentication
This was such a pain in the ass to do:(
To call Microsoft Graph, your app must acquire an access token from the Microsoft identity platform. The access token contains information about your app and the permissions it has for the resources and APIs available through Microsoft Graph. Only with the access token then can you call Microsoft graph API successfully.

I used Microsoft Authentication Library (MSAL) module to help me with this process.

### Application
You need to create an application on the Azure AD platform. After that, you have to delegate permissions to the applications that you will be using with this application.
Use the Graph Explorer to test the API endpoints that you want.

###