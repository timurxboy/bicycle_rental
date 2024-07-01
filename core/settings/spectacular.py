import os

SPECTACULAR_SETTINGS = {
    'TITLE': os.environ.get('APP_NAME') or "Energy",
    'SERVERS': [
        {
            'url': 'http://localhost:8000'
        },
    ],
    'VERSION': '1.0.0',
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'COMPONENT_SPLIT_REQUEST': True,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
    },
    'DEFAULT_CONTENT_TYPE': 'application/x-www-form-urlencoded', # Set the default content type
}
