from fastapi.testclient import TestClient  
  
from backend.main import app  
  
client = TestClient(app)  
  
def test_endpoints():  
    print("Testing /health")  
    r_health = client.get("/health")  
    print(f"Status: {r_health.status_code}, Body: {r_health.json()}")  
  
    print("Testing /api/predict")  
    r_predict = client.post("/api/predict", json={"skin_type": "Oily", "sensitivity": "No", "concern": "Acne"})  
    print(f"Status: {r_predict.status_code}")  
    if r_predict.status_code != 200: print(f"Error: {r_predict.text}")  
    else: print(f"Body: {r_predict.json()}")  
  
    print("Testing /api/recommend")  
    r_recommend = client.post("/api/recommend", json={"skin_type": "Oily", "concerns": ["Acne"], "age": 25})  
    print(f"Status: {r_recommend.status_code}")  
    if r_recommend.status_code != 200: print(f"Error: {r_recommend.text}")  
  
    print("Testing /api/routine")  
    r_routine = client.post("/api/routine", json={"user_profile": {"skin_type": "Oily"}, "ml_prediction": {"ingredient": "Niacinamide"}, "routine_type": "Night", "routine_focus": "Hydration"})  
    print(f"Status: {r_routine.status_code}")  
    if r_routine.status_code != 200: print(f"Error: {r_routine.text}")  
  
if __name__ == "__main__":  
    test_endpoints() 
