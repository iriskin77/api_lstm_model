1) Как сделать миграции:

+ **aerich init -t settings.tortoise_conf.TORTOISE_ORM** - прописать путь до файла с конфигурацией TORTOISE_ORM 

+ **aerich init-db** - этой командой создаются миграции и применяются в БД

+ **aerich migrate**

+ **aerich upgrade**

+ **Важно: нужно зарегистрировать модели (tortoise_orm в main)**
