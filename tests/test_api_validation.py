#!/usr/bin/env python3
"""
Comprehensive API validation for Skinlytix backend.
Tests all endpoints with valid and edge-case inputs.
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

print("=" * 80)
print("🧪 SKINLYTIX API VALIDATION TEST SUITE")
print("=" * 80)

# Test 1: Health Check
print("\n[TEST 1] GET /health")
print("-" * 80)
response = client.get("/health")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
assert response.status_code == 200
assert response.json()["status"] == "ok"
print("✅ PASS")

# Test 2: Predict with valid input
print("\n[TEST 2] POST /api/predict (valid input)")
print("-" * 80)
predict_payload = {
    "skin_type": "Oily",
    "sensitivity": "Yes",
    "concern": "Acne"
}
print(f"Payload: {predict_payload}")
response = client.post("/api/predict", json=predict_payload)
print(f"Status: {response.status_code}")
result = response.json()
print(f"Response keys: {result.keys()}")
print(f"Success: {result.get('success')}")
print(f"Ingredient: {result.get('ingredient')}")
print(f"Cluster: {result.get('cluster_label')}")
print(f"Confidence: {result.get('confidence')}")
assert response.status_code == 200
assert result.get("success") == True
assert result.get("ingredient") is not None
assert result.get("cluster_label") is not None
print("✅ PASS")

# Test 3: Predict with another valid input
print("\n[TEST 3] POST /api/predict (dry skin, wrinkles)")
print("-" * 80)
predict_payload = {
    "skin_type": "Dry",
    "sensitivity": "No",
    "concern": "Wrinkles"
}
print(f"Payload: {predict_payload}")
response = client.post("/api/predict", json=predict_payload)
print(f"Status: {response.status_code}")
result = response.json()
assert response.status_code == 200
assert result.get("success") == True
print("✅ PASS")

# Test 4: Predict with invalid skin type
print("\n[TEST 4] POST /api/predict (invalid skin_type)")
print("-" * 80)
predict_payload = {
    "skin_type": "Unknown",  # Invalid!
    "sensitivity": "Yes",
    "concern": "Acne"
}
print(f"Payload: {predict_payload}")
response = client.post("/api/predict", json=predict_payload)
print(f"Status: {response.status_code}")
result = response.json()
print(f"Response: {result}")
assert response.status_code == 400
assert result.get("success") is not True
assert "Unknown" in result.get("detail", "")
print("✅ PASS - correctly rejected invalid input")

# Test 5: Predict with invalid sensitivity
print("\n[TEST 5] POST /api/predict (invalid sensitivity)")
print("-" * 80)
predict_payload = {
    "skin_type": "Oily",
    "sensitivity": "Maybe",  # Invalid! Should be Yes/No
    "concern": "Acne"
}
print(f"Payload: {predict_payload}")
response = client.post("/api/predict", json=predict_payload)
print(f"Status: {response.status_code}")
result = response.json()
print(f"Response: {result}")
assert response.status_code == 400
assert result.get("success") is not True
print("✅ PASS - correctly rejected invalid input")

# Test 6: Recommend with valid input
print("\n[TEST 6] POST /api/recommend (valid input)")
print("-" * 80)
recommend_payload = {
    "skin_type": "Oily",
    "concerns": ["Acne"],
    "age": 24,
    "preferences": {}
}
print(f"Payload: {recommend_payload}")
response = client.post("/api/recommend", json=recommend_payload)
print(f"Status: {response.status_code}")
result = response.json()
print(f"Success: {result.get('success')}")
print(f"Recommendation count: {result.get('count')}")
if result.get("recommendations"):
    print(f"First recommendation: {result['recommendations'][0]}")
assert response.status_code == 200
assert result.get("success") == True
assert result.get("count") > 0
assert isinstance(result.get("recommendations"), list)
print("✅ PASS")

# Test 7: Routine with simple input
print("\n[TEST 7] POST /api/routine (simple input)")
print("-" * 80)
routine_payload = {
    "skin_type": "Oily",
    "sensitivity": "Yes",
    "concern": "Acne",
    "routine_type": "Morning",
    "routine_focus": "Acne Control"
}
print(f"Payload: {routine_payload}")
response = client.post("/api/routine", json=routine_payload)
print(f"Status: {response.status_code}")
result = response.json()
print(f"Success: {result.get('success')}")
print(f"Routine type: {result.get('routine_type')}")
print(f"Steps count: {len(result.get('steps', []))}")
print(f"Total time: {result.get('total_time')} minutes")
assert response.status_code == 200
assert result.get("success") == True
assert result.get("routine_type") == "Morning"
print("✅ PASS")

# Test 8: Full pipeline
print("\n[TEST 8] POST /api/full (complete pipeline)")
print("-" * 80)
full_payload = {
    "skin_type": "Normal",
    "sensitivity": "No",
    "concern": "Dark Spots"
}
print(f"Payload: {full_payload}")
response = client.post("/api/full", json=full_payload)
print(f"Status: {response.status_code}")
result = response.json()
print(f"Success: {result.get('success')}")
print(f"Ingredient: {result.get('ingredient')}")
print(f"Products count: {len(result.get('products', []))}")
print(f"Remedies count: {len(result.get('remedies', []))}")
assert response.status_code == 200
assert result.get("success") == True
print("✅ PASS")

# Test 9: Missing required fields
print("\n[TEST 9] POST /api/predict (missing field)")
print("-" * 80)
predict_payload = {
    "skin_type": "Oily",
    "sensitivity": "Yes"
    # Missing 'concern'!
}
print(f"Payload: {predict_payload}")
response = client.post("/api/predict", json=predict_payload)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
assert response.status_code == 422
print("✅ PASS - correctly rejected incomplete request")

# Test 10: Combination skin type
print("\n[TEST 10] POST /api/predict (combination skin)")
print("-" * 80)
predict_payload = {
    "skin_type": "Combination",
    "sensitivity": "No",
    "concern": "Acne"
}
print(f"Payload: {predict_payload}")
response = client.post("/api/predict", json=predict_payload)
print(f"Status: {response.status_code}")
result = response.json()
print(f"Success: {result.get('success')}")
print(f"Ingredient: {result.get('ingredient')}")
assert response.status_code == 200
assert result.get("success") == True
print("✅ PASS")

print("\n" + "=" * 80)
print("✅ ALL TESTS PASSED!")
print("=" * 80)
print("\n📊 Summary:")
print("  • Health check: OK")
print("  • Prediction with valid inputs: OK")
print("  • Prediction error handling: OK")
print("  • Recommendations: OK")
print("  • Routines: OK")
print("  • Full pipeline: OK")
print("  • Request validation: OK")
print("\n🎉 Backend API is fully functional and ready for React integration!")
