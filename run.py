import sys
import logging
import importlib.util

logging.basicConfig(level=logging.INFO)

class ImportLogger:
    def find_spec(self, fullname, path, target=None):
        if not fullname.startswith('_'):
            logging.info(f"Importing module: {fullname}")
        return None

sys.meta_path.insert(0, ImportLogger())

from app import create_app, socketio

app = create_app()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)


# source venv/bin/activate
