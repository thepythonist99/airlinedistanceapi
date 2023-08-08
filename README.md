# Airline Distance Calculator API

## Between two(2) railway stations of type FV (Fernverkehr)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Bitbucket](https://img.shields.io/badge/bitbucket-%230047B3.svg?style=for-the-badge&logo=bitbucket&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![openSUSE](https://img.shields.io/badge/openSUSE-%2364B345?style=for-the-badge&logo=openSUSE&logoColor=white)

### How to use

- Clone this repo (Either on Bitbucket or GitHub)

```
git clone https://github.com/thepythonist99/airlinedistanceapi.git
```

or

```
git clone https://cassius95@bitbucket.org/cassius95/airlinedistanceapi.git
```

- Change into the cloned repo

```
cd airlinedistanceapi
```

- Create a Python Virtual Environment (with Python 3.9+)
```
python3 -m venv venv
```

- Activate the Virtual Environment

```
source venv/bin/activate
```

- Create a .env file which hosts the environment variables necessary for the app

```
vi .env
```

- Add these environment variables

```
export API_HOST="0.0.0.0"
export API_PORT="8000"
export API_RELOAD=True
export SECRET_KEY=<secretkey>
export COORDINATE_FILE="D_Bahnhof_2020_alle.csv"
```

**Note:** A secret key can be obtained by running the following command:

```
openssl rand -hex 32
```

- Install app requirements

```
pip install -r requirements.txt
```

- Source the .env file

```
source .env
```

- Launch the app

```
python main.py
```

- Open a browser and navigate to

```
0.0.0.0:8000/docs
```

or 

```
0.0.0.0:8000/redoc
```