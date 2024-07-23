# Test task - simple IoT device manager.

While implementing the task, a simple database management
program was created with asynchronous API.

## Database setup

Before running the app you need to configure your database:

```
# on mac
$ brew install postgresql
$ brew services start postgresql

# on linux
$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release
-cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo
apt-key add - s

$ sudo apt update
$ sudo apt install postgresql postgresql-contrib
$ sudo systemctl start postgresql.service
```

then create a database and a user

```
CREATE DATABASE db_name;
CREATE USER your_username WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE iot_db TO your_username;
```

and setup postgresql connection in Python script

```
db = PooledPostgresqlDatabase(
    'db_name',
    user='your_user',
    password='your_password',
    host='localhost',
    port=5432
)
```

As you run the app, all tables should be created automatically.

## How to run

To run the app you need

1. Install all the nesseccary dependencies

```
pip install -r requirements.txt
```

2. run the `app.py` file

```
python app.py
```

## How to interact with API

1. Working with users

```
# create user
curl -X POST http://localhost:8080/apiuser \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com", "password": "securepassword"}'

# get user
curl -X GET http://localhost:8080/apiuser/{id}

# update user
curl -X PUT http://localhost:8080/apiuser/{id} \
     -H "Content-Type: application/json" \
     -d '{"name": "John Smith", "email": "john.smith@example.com", "password": "newpassword"}'

# delete user
curl -X DELETE http://localhost:8080/apiuser/{id}
```

2. Working with locations

```
# create location
curl -X POST http://localhost:8080/location \
     -H "Content-Type: application/json" \
     -d '{"name": "Office"}'

# get location
curl -X GET http://localhost:8080/location/{id}

# update location
curl -X PUT http://localhost:8080/location/{id} \
     -H "Content-Type: application/json" \
     -d '{"name": "Headquarters"}'


# delete location
curl -X DELETE http://localhost:8080/location/{id}
```

3. Working with devices

```
# create device
curl -X POST http://localhost:8080/device \
     -H "Content-Type: application/json" \
     -d '{"name": "Device1", "type": "Sensor", "login": "user1", "password": "pass", "location_id": 1, "api_user_id": 1}'

# get device
curl http://localhost:8080/device/{id}

# update device
curl -X PUT http://localhost:8080/device/{id} \
     -H "Content-Type: application/json" \
     -d '{"name": "UpdatedDevice1"}'

# delete device
curl -X DELETE http://localhost:8080/device/{id}
```

All the errors and actions are saved in `app.log` file.
