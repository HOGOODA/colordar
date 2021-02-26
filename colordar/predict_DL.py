from django.conf import settings
from tensorflow.keras import models
import numpy as np
import ktrain
from ktrain import text



def predict_mood(tokenized):
    base_url = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
    model_url = base_url + 'final_model_ver7.h5'
    model=models.load_model(model_url, compile=False)

    predict_result = model.predict(tokenized)
    return predict_result

def predict_emotion(tokenized):
    base_url = settings.MEDIA_ROOT_URL + settings.MEDIA_URL # == './media/'
    model_url = base_url + 'ktrain_bert_model'

    p = ktrain.load_predictor(model_url)
    predict = p.predict(tokenized)

    return predict