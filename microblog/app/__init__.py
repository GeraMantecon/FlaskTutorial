from flask  import Flask
from config import Config

app = Flask(__name__)
#Since we now have a configuration class we import it and load it.
app.config.from_object(Config)

from app import routes
