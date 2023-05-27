import os
import shutil
import sys
import pandas as pd

df = pd.read_json("./training/datasets/face/processed/data_face.json")


def delete_user(email):
    members = df[df["email"] != email]
    members.to_json("./training/datasets/face/processed/data_face.json")
    # shutil.rmtree("./training/datasets/face/raw/" + email)
    # os.remove('Dataset/FaceData/raw/' + name)
