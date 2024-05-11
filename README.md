## Description

It is a simple project which has to process texts to do emotional analysis.

To see the previous version of the project (Python, FastApi, Postgres),
welcome to this branch: https://github.com/iriskin77/api_lstm_model/tree/copy/save-monolith-python

## Todo

New service that should have to be done:

![Рис. 2](/images/services.png)

1) Api-gateway

2) Auth-service Go + Mongo + Redis

3) File-service Go + gRPC + Postgres (to store texts extracted from files) + Minio (to store files)

4) Process-service Python + FastApi + Minio (service with LSTM model to implement emotion analusis)

5) Analytics service Go (service should analyze, count statistics)