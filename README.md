# Account Service

This is a RESTful API which can store and retrieve account information using a Firestore database.

### Requirements

- A Firestore instance up and running in your Google Cloud account
- google service account to access the Firestore

#### Refer below link for more detail about setting up the environment to use google Firestore

- https://cloud.google.com/firestore/docs/quickstart-servers

### Environment variables

The service uses the below variables in its configuration. They all have default values as shown below if they are not otherwise specified:

```
ACCOUNT_NAMESPACE=accounts(default)
PORT=5001(default)
CUSTOMER_SERVICE_URL=http://localhost:5000(default)
```

To enable full functionality of the account service you must provide it with the endpoint of the customer service using the environment variable CUSTOMER_SERVICE_URL.

### To run linter

```bash
make lint
```

### To run tests

```bash
make test
```

### To run the service locally

Note:

The ability to create new accounts will only work when the service is provided with a working customer service endpoint.
Although you should be able to retrieve account information without it.

```bash
make run
```

### Deployment to Cloud Run

This repository contains a cloudbuild.yaml file to deploy this service on to Cloud Run.
In order for this service to be able to create new accounts you must specify the url of the running customer service in the deployment command like below:

```bash
gcloud builds submit --substitutions=_CUSTOMER_SERVICE_URL="[CUSTOMER_SERVICE_URL]",_ACCOUNT_NAMESPACE="[ACCOUNT_NAMESPACE]"
```

where [CUSTOMER_SERVICE_URL] is the url of the customer service and can be retrieved from the customer service in the Cloud Run console, and [ACCOUNT_NAMESPACE] is the name of the Firestore collection that stores the accounts information.
If you accidentally deploy this service before customer, you can update its deployment retrospectively by re-running the command above with the new customer url.

### API documentation

You can access the API documentation by launching the application and visiting [swagger ui](http://localhost:5001/docs/) locally.


