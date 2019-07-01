import os

# db connection
DB_ADAPTER = os.environ.get("DB_ADAPTER", "adapters.mongodb.MongoDBAdapter")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", 27017))
DB_NAME = os.environ.get("DB_NAME", "reporting")
DB_USERNAME = os.environ.get("DB_USERNAME", "admin")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "changeme")

# webserver
WEBSERVER_HOST = os.environ.get("WEBSERVER_HOST", "0.0.0.0")
WEBSERVER_PORT = os.environ.get("WEBSERVER_PORT", "8080")
