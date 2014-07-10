FORMAT: X-1A

# A Python/Flask recipe for REST API with simple API key authentication.
This recipe is a really simple solution for building a REST API, quickly using Flask.

# Installing requirements.
Use virtual environment, please.
* pip install virtualenv
* virtualenv venv/
Activate environment.

Install requirements for the project
* pip install -r requirements.txt


# Authentication

All information resources are protected by authentication.
Authentication for this API is handled by a classic "API key" methodology.
Administrators issues a API key locked to a certain remote IP address or all IP addresses.

manage.py manages authentication keys
* To generate a API key you use ./run.py -g IP -c "this IP is for the engineer on floor 3" (If you define IP as 0.0.0.0 you are allowing the API key to be used from any remote IP)
* To remove a API key you use ./run -d APIKEYID (APIKEYIDs are shown when running run.py with the -a flag)
* To show all issued keys use ./run -a


# Responses tips (unofficial response standards)

I advise to keep responses formats under control and stay consistent. 
You could follow the JSend specification (http://labs.omniti.com/labs/jsend).