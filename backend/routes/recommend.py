from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict

from backend.services.ml_service import recommend_ml, full_pipeline_ml

router = APIRouter()


class RecommendRequest(BaseModel):
    skin_type: str
    concerns: List[str]
    age: int
    preferences: Optional[Dict] = {}


class FullRequest(BaseModel):
    skin_type: str
    sensitivity: str
    concern: str


@router.post("/recommend")
def recommend(request: RecommendRequest):
    try:
        result = recommend_ml(request.dict())
        return {
            "success": True,
            "recommendations": result,
            "count": len(result),
            "error": None,
        }
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e)) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal recommendation error: {str(e)}") from e


@router.post("/full")
def full_pipeline(request: FullRequest):
    try:
        result = full_pipeline_ml(request.dict())
        if not result or not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Full pipeline failed"))

        return {
            "success": True,
            "ingredient": result.get("ingredient"),
            "cluster_label": result.get("cluster_label"),
            "products": result.get("products", []),
            "remedies": result.get("remedies", []),
            "confidence": result.get("overall_confidence", 0),
            "error": None,
        }
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e)) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal full-pipeline error: {str(e)}") from e