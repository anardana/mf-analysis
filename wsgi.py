'''Server entry point for WSGI application (gunicorn)'''
from mf_analysis.api.controller import APP as application

if __name__ == "__main__":
    application.run()
