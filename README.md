# Pyomo + Django Rest Framework + Docker
The technologies required to formulate and solve optimisation problems can be tricky to configure on different operating systems. This repository provides a template to simplify the process.

Docker is used to install a solver and associated dependencies. Pyomo is used to construct a mathematical program, while Django REST Framework provides users an interface through which they can interact with the model. Model parameters are updated via POST requests to an API endpoint, with the solution returned as a JSON object. 

Decoupling the model's construction from the method by which parameters are updated makes this setup language agnostic. You can submit model data using whatever programming language you like, so long as the language accomodates POST requests.

**Note: this is a minimal working example which is not intended to be used in production.**

## Quickstart
1. Set `DJANGO_SECRET_KEY` within `config/secret-template.env`. Rename file to `config/secret.env`
2. Run `docker-compose -f docker-compose.yml up --build`. This starts a development server running on port 8000. 
3. Send a POST request containing model parameters:

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"PARAMETER_1": 300, "PARAMETER_2": 100, "PARAMETER_3": 500}' \
  http://localhost:8000/api/run
```

Response:

```
{"x": 300,"y": 2}
```

## Mathematical program
The program being solved is contained within the `construct_model` function within `project/api/optimisation/model.py` and has the following form:

```
minimise x + y
s.t.
x >= PARAMETER_1
x + (y * PARAMTER_2) >= PARAMETER_3
```

This model is a placeholder - replace it with your own.