from typing import Dict, Any

from ml.predictions import predict_skin_solution
from ml.recommendations import get_recommendations
from ml.integration import generate_full_recommendation
from ml.routine_builder import generate_personalized_routine


def _require_keys(data: Dict[str, Any], keys):
    missing = [k for k in keys if k not in data]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")


def predict_ml(data: Dict[str, Any]):
    _require_keys(data, ["skin_type", "sensitivity", "concern"])
    return predict_skin_solution(
        skin_type=data["skin_type"],
        sensitivity=data["sensitivity"],
        concern=data["concern"]
    )


def recommend_ml(data: Dict[str, Any]):
    _require_keys(data, ["skin_type", "concerns", "age"])
    results = get_recommendations({
        "skin_type": data["skin_type"],
        "concerns": data["concerns"],
        "age": data["age"],
        "preferences": data.get("preferences", {})
    })
    return [
        {
            "ingredient": r.ingredient,
            "score": r.score,
            "reasoning": r.reasoning,
        }
        for r in results
    ]


def full_pipeline_ml(data: Dict[str, Any]):
    _require_keys(data, ["skin_type", "sensitivity", "concern"])
    return generate_full_recommendation(
        skin=data["skin_type"],
        sensitivity=data["sensitivity"],
        concern=data["concern"]
    )


def routine_ml(data: Dict[str, Any]):
    _require_keys(data, ["user_profile", "ml_prediction", "routine_type", "routine_focus"])
    return generate_personalized_routine(
        user_profile=data["user_profile"],
        ml_prediction=data["ml_prediction"],
        routine_type=data["routine_type"],
        routine_focus=data["routine_focus"]
    )