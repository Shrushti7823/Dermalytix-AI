from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

from backend.services.ml_service import routine_ml, predict_ml

router = APIRouter()


class RoutineRequest(BaseModel):
    """Simple routine request with skin profile."""
    skin_type: str
    sensitivity: str = "No"
    concern: str
    routine_type: str = "Morning"
    routine_focus: str = "General Care"


@router.post("/routine")
def generate_routine(request: RoutineRequest):
    try:
        # First, get prediction from skin profile
        prediction = predict_ml({
            "skin_type": request.skin_type,
            "sensitivity": request.sensitivity,
            "concern": request.concern
        })
        
        if not prediction or not prediction.get("success", False):
            raise HTTPException(status_code=400, detail=prediction.get("error", "Prediction failed"))
        
        # Build user profile for routine generation
        user_profile = {
            "skin_type": request.skin_type,
            "sensitivity": request.sensitivity,
            "primary_concern": request.concern,
            "age": 25,  # Default age if not provided
            "skin_concerns": [request.concern]
        }
        
        # Generate routine with prediction results
        result = routine_ml({
            "user_profile": user_profile,
            "ml_prediction": prediction,
            "routine_type": request.routine_type,
            "routine_focus": request.routine_focus
        })
        
        if not result or not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Routine generation failed"))

        return {
            "success": True,
            "routine_type": result.get("routine_type"),
            "focus_area": result.get("focus_area"),
            "steps": result.get("steps", []),
            "total_time": result.get("total_time", 0),
            "tips": result.get("tips", []),
            "error": None,
        }
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e)) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal routine error: {str(e)}") from e