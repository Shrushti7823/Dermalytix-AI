from ml.model_loader import ModelLoader
import numpy as np

print("\n🔍 Running MRE Pipeline Test...\n")

# Load models
loader = ModelLoader()
loader.load_all()

# Test encoders
print("\n🔐 Testing Encoders...")
try:
    skin = loader.le_skin.transform(["Combination"])
    sens = loader.le_sens.transform(["No"])
    concern = loader.le_concern.transform(["Acne"])

    print("✅ Encoders working")
except Exception as e:
    print("❌ Encoder error:", e)

# Test KNN model
print("\n🤖 Testing KNN Model...")
try:
    sample_input = np.array([[skin[0], sens[0], concern[0]]])
    pred = loader.knn_model.predict(sample_input)

    print("✅ KNN Prediction:", pred)
except Exception as e:
    print("❌ KNN error:", e)

# Test KMeans
print("\n📊 Testing KMeans...")
try:
    cluster = loader.kmeans_model.predict(sample_input)
    print("✅ Cluster:", cluster)
except Exception as e:
    print("❌ KMeans error:", e)

print("\n🎯 MRE Test Completed\n")