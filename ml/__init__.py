"""Skinlytix ML package with lazy exports.

This avoids importing Streamlit-dependent modules at package import time,
which prevents backend startup side effects when using FastAPI.
"""

from importlib import import_module


_EXPORTS = {
    # Recommendations (Block 1)
    'get_recommendations': ('ml.recommendations', 'get_recommendations'),
    'explain_recommendation': ('ml.recommendations', 'explain_recommendation'),
    'get_ingredient_score_mapping': ('ml.recommendations', 'get_ingredient_score_mapping'),
    'RecommendationResult': ('ml.recommendations', 'RecommendationResult'),
    # Dataset Loading (Block 3)
    'load_skincare_dataset': ('ml.loaders', 'load_skincare_dataset'),
    'validate_skincare_dataset': ('ml.loaders', 'validate_skincare_dataset'),
    'get_feature_matrix_and_labels': ('ml.loaders', 'get_feature_matrix_and_labels'),
    'get_dataset_summary': ('ml.loaders', 'get_dataset_summary'),
    'get_dataset_statistics': ('ml.loaders', 'get_dataset_statistics'),
    # ML Model (Block 4)
    'predict_ingredient': ('ml.ml_model', 'predict_ingredient'),
    'initialize_model': ('ml.ml_model', 'initialize_model'),
    'get_model_info': ('ml.ml_model', 'get_model_info'),
    'compare_with_block1': ('ml.ml_model', 'compare_with_block1'),
    'get_model_performance_report': ('ml.ml_model', 'get_model_performance_report'),
    # Coordinator (Block 8)
    'UserProfile': ('ml.coordinator', 'UserProfile'),
    'MLUserProfile': ('ml.coordinator', 'MLUserProfile'),
    'RecommendationResults': ('ml.coordinator', 'RecommendationResults'),
    'build_user_profile': ('ml.coordinator', 'build_user_profile'),
    'convert_to_ml_profile': ('ml.coordinator', 'convert_to_ml_profile'),
    'get_combined_recommendations': ('ml.coordinator', 'get_combined_recommendations'),
    'validate_sidebar_inputs': ('ml.coordinator', 'validate_sidebar_inputs'),
    'get_dataset_info': ('ml.coordinator', 'get_dataset_info'),
    'get_model_status': ('ml.coordinator', 'get_model_status'),
    # Routine Builder
    'generate_personalized_routine': ('ml.routine_builder', 'generate_personalized_routine'),
    'generate_routine_insights': ('ml.routine_builder', 'generate_routine_insights'),
    'get_routine_products_from_dataset': ('ml.routine_builder', 'get_routine_products_from_dataset'),
}


def __getattr__(name):
    if name in _EXPORTS:
        module_name, attr_name = _EXPORTS[name]
        module = import_module(module_name)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module 'ml' has no attribute '{name}'")

__all__ = [
    # Recommendations (Block 1)
    'get_recommendations',
    'explain_recommendation',
    'get_ingredient_score_mapping',
    'RecommendationResult',
    
    # Dataset Loading (Block 3)
    'load_skincare_dataset',
    'validate_skincare_dataset',
    'get_feature_matrix_and_labels',
    'get_dataset_summary',
    'get_dataset_statistics',
    
    # ML Model (Block 4)
    'predict_ingredient',
    'initialize_model',
    'get_model_info',
    'compare_with_block1',
    'get_model_performance_report',
    
    # Coordinator (Block 8)
    'UserProfile',
    'MLUserProfile',
    'RecommendationResults',
    'build_user_profile',
    'convert_to_ml_profile',
    'get_combined_recommendations',
    'validate_sidebar_inputs',
    'get_dataset_info',
    'get_model_status',
    
    # Routine Builder
    'generate_personalized_routine',
    'generate_routine_insights',
    'get_routine_products_from_dataset',
]
