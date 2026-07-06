import pickle 
import os 
models_dir = 'models' 
files = ['le_skin.pkl', 'le_sens.pkl', 'le_concern.pkl'] 
for f_name in files: 
    path = os.path.join(models_dir, f_name) 
    with open(path, 'rb') as f: 
        le = pickle.load(f) 
        print(f"--- {f_name} ---") 
        print(le.classes_) 
