# Main.py
import uvicorn
from .api.api import app

# Running
if __name__ == "__main__":
    uvicorn.run(app)