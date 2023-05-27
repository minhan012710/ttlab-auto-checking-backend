import pandas as pd
from settings import (
    DATA_FACE_DIR,
)

def main():
    df = pd.DataFrame(
        {
            "face": [],
            "email": [],
        }
    )
    df.to_json(DATA_FACE)


if __name__ == "__main__":
    main()
