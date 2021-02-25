from django.conf import settings
from tensorflow.keras import models
import numpy as np


def predict_mood(tokenized):
    base_url = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
    model_url = base_url + 'final_model_ver7.h5'
    model=models.load_model(model_url, compile=False)

    predict_result = np.argmax(model.predict(tokenized))
    return predict_result


