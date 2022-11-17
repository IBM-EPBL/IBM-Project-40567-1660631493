from venv import create
from hello import create_app

if _name_ == "_main_":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)