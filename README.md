# A simple recipe for a RESTful API packaged with an API key authentication.
This recipe is a really simple seed for a RESTful API, powered by Flask and SQLALchemy.
It's a perfect starting point if you are in need of an API, quickly... At least I think so!

The recipe includes the following features:
* A naive method of API versioning.
* Ability to switch between a development and Default application config, by using environmental variables.
* Simple test cases in a form of unit tests.
* Authentication component which you can decorate API methods with.
    * Manage.py, manages keys and allowed IPs (where 0.0.0.0 is considered all IPs).
    * The decorator *@require_app_key*, from *restapi.components.auth.decorators* then only allows keys generated with manage.py
* API control, run.py:
    * *-r* runs a development server
    * *-i* initializes the database based on imported SQLALchemy models
    * *-z* creates a interactive console, with flask app imported.

# Quick Start
Use virtual environment, please.
```
$> pip install virtualenv
$> virtualenv venv/
```
Activate environment.
```
$> . venv/bin/active
```
Install requirements for the project
```
$> pip install -r requirements.txt
```
Init the default SQLite database:
```
$> python run.py -i
```
Run the development server
```
$> python run.py -r
```

# Create you first API key
Generate an key for localhost (127.0.0.1)
```
$> python manage.py -g 127.0.0.1 "localhost Development Key"
```
You should get an output like:
```
Issued a key 'eMtUDd3ZF19M9Dk7fOgSKmpuqX0KV6sHDwfrydiN0gk' for the IP '127.0.0.1' (localhost development key) with KEY ID: 2.
```

Next, try to insert a cake object to the database (it's authentication protected by default) by using *curl*:
```
$> curl -X POST -d "cakename=Test Cake&baker=Haukur Kristinsson&price=200" http://localhost:5000/api/v1.1/cakes/?key=eMtUDd3ZF19M9Dk7fOgSKmpuqX0KV6sHDwfrydiN0gk
```
You should get an status=success (Remember JSEND standard) output:
```
{
  "data": {
    "cakes": {
      "bakername": "Haukur Kristinsson",
      "cakename": "Test Cake",
      "id": 6,
      "price": 200.0,
      "price_range": "expensive"
    }
  },
  "status": "success"
}
```

# Authentication Method

Authentication for this API is handled by a classic "API key" methodology which allows the client to pass the key as an URL parameter *key* (i.e. http://api/?key=KEY).
Nothing fancy about that... But its should be noted that this method is only secure while using encrypted channels between clients and the web server.

When issuing a API key, you can either specify a IP address that is to be allowed when using the key, or by using the IP 0.0.0.0 to allow all IP addresses.

Summary of manage.py (authentication manager):
* To generate a API key you use
    ```
    ./run.py -g IP -c "this IP is for the engineer on floor 3" (If you define IP as 0.0.0.0 you are allowing the API key to be used from any remote IP)
    ```
* To remove a API key you use
    ```
    ./run -d APIKEYID (APIKEYIDs are shown when running run.py with the -a flag)
    ```
* To show all issued keys use
    ```
    ./run -a
    ```

# JSON responses

I advise to keep responses formats under control and to stay consistent at all times.
You could follow the JSend specification (http://labs.omniti.com/labs/jsend), or at least base you output format from there.

# Example API methods
I included 2 API methods, just as an example of how you can use it:
* cakes modules (/api/v<float:version/cakes)
* weather module (/api/v<float:version>/weather)

I'm not going to into detail of each one, you should just look at the source code.