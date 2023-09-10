"""
routers/classification_api.py
-----------------------------
"""
import logging
from fastapi import HTTPException, APIRouter
from Modelling.utils import ModelInference
from pydantic import BaseModel
from config import PROD_MODEL_PATH

##############################################
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/inveniai")
##############################################

class Item(BaseModel):
    text: str

from fastapi.responses import JSONResponse

@router.post("/predict_speciality")
def predict_speciality(item: Item):
    try:
        text = item.text
        clss = ModelInference(model_path = PROD_MODEL_PATH, data = text)
        clss.preprocess_data()
        result_dict = clss.get_model_prediction()
        result_dict['result'] = int(result_dict['result'])
        return JSONResponse(content=result_dict)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    