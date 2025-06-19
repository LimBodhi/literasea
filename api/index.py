import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'literasea.settings')

# Import Django WSGI application
from literasea.wsgi import application

# Export the WSGI application
handler = application 