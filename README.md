## Description

It is a simple project which has to process texts to do emotional analysis.

To see the previous version of the project (Python, FastApi, Postgres),
welcome to this branch: https://github.com/iriskin77/api_lstm_model/tree/copy/save-monolith-python

## Todo

Now I am goingo to refactor the project according to the schema below:

![Рис. 2](/images/new_scema.png)

1) Api-gateway на Go

2) Auth-service на Go + Mongo

3) File-service на Python, gRPC

4) File-process-service на Python