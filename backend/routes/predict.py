from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.services.ml_service import predict_ml

router = APIRouter()


class PredictRequest(BaseModel):
    skin_type: str
    sensitivity: str
    concern: str


@router.post("/predict")
def predict(request: PredictRequest):
    try:
        result = predict_ml(request.dict())
        if not result or not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Prediction failed"))

        return {
            "success": True,
            "ingredient": result.get("ingredient"),
            "cluster_label": result.get("cluster_label"),
            "cluster_number": int(result.get("cluster_number")) if result.get("cluster_number") is not None else None,
            "confidence": float(result.get("overall_confidence", 0) or 0),
            "ingredient_confidence": float(result.get("ingredient_confidence", 0) or 0),
            "cluster_confidence": float(result.get("cluster_confidence", 0) or 0),
            "error": None,
        }
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e)) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal prediction error: {str(e)}") from e