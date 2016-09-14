import sys

from app import app

try: 
    import settings
except ImportError:   
    print ("Please copy settings-dist.py to settings.py and update your API key.")
    syst.exit()

app.config.from_object(settings)

app.run(debug=True)