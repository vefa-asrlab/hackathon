# hackathon
Vefa ASR Lab Hackathon

## Dependencies
* Flask
* Waitress (For deploying to production)

### Installation 
If you want to create a venv (Optional):
```bash
$ python -m venv venv

# To activate venv
$ . venv/bin/activate
```

Install dependencies:
```bash
$ pip install flask
$ pip install waitress
```

## Usage & Dependencies (Deploying to Production)
For safety, after developing your application you should use a dedicated WSGI server or hosting platform.

Run web app by typing:
```bash
$ python main.py app
```

## For developing
In this mode, you should develop locally, it is not safe to make it available publicly to other users.

Run web app in develop mode by typing:
```bash
$ python main.py dev
```
