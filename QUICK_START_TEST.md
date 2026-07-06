# 🚀 SKINLYTIX QUICK START - TESTING GUIDE

## ✅ ISSUE FIXED

The "process is not defined" error and blank page have been fixed.

**What was wrong:**
- Line 86 in `frontend/src/app/App.tsx` used `process.env` (Node.js only)
- Vite client-side code must use `import.meta.env` instead

**What was fixed:**
```diff
- {process.env.VITE_API_URL || 'http://localhost:8000'}
+ {import.meta.env.VITE_API_URL || 'http://localhost:8000'}
```

---

## 🚀 START THE APPLICATION

### Terminal 1: Backend

```bash
cd c:\Users\Nakshatra Rao\GlowGuide
python -m uvicorn backend.main:app --reload
```

**Expected output:**
```
INFO:     Application startup complete
Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### Terminal 2: Frontend

```bash
cd c:\Users\Nakshatra Rao\GlowGuide\frontend
npm run dev
# or
pnpm dev
```

**Expected output:**
```
VITE v5.x.x  ready in xxx ms

➜  Local:   http://localhost:5173/
➜  press h to show help
```

---

## 🧪 TEST THE INTEGRATION

### 1. Open Browser
Go to: **http://localhost:5173**

You should see:
- ✅ Hero section with "Skinlytix" title
- ✅ "Analyze My Skin" button
- ✅ NO blank page
- ✅ NO console errors

### 2. Click "Analyze My Skin"
- Page scrolls to form
- Form displays 4 sections

### 3. Fill Out Form
```
Skin Type:      → Select "Oily"
Sensitivity:    → Select "Medium"
Concern:        → Select "Acne"
```

### 4. Click "Get Recommendation"
- ✅ Button shows loading spinner
- ✅ Button text shows "Analyzing..."
- ✅ Button is disabled

### 5. Wait for Response
- Should complete in 1-3 seconds
- ✅ Results section appears
- ✅ Shows actual data from backend:
  - Ingredient name (from ML model)
  - Skin Profile cluster
  - Confidence percentage

### 6. Expected Results Display
```
┌─────────────────────────────────────────────┐
│  Recommended Ingredient: [Ingredient Name]  │
│                                             │
│  Skin Profile: [Cluster Label]              │
│                                             │
│  Confidence Score: [XX]%                    │
└─────────────────────────────────────────────┘
```

---

## 🔍 VERIFY IN DEVELOPER TOOLS

### Check Console
1. Open DevTools: **F12** or **Ctrl+Shift+I**
2. Go to **Console** tab
3. Should see NO errors (only info logs)
4. You may see: `Prediction API error: ...` only if backend is down

### Check Network Tab
1. Go to **Network** tab
2. Click "Get Recommendation"
3. Should see:
   - **POST /api/predict** request
   - Status: **200** (success)
   - URL: `http://localhost:8000/api/predict`
   - Response body shows: `{ "success": true, ... }`

### Check Environment Variable
1. Open **Console** tab
2. Type:
```javascript
import.meta.env.VITE_API_URL
```
3. Should print: `http://localhost:8000` (or your config)

---

## ⚠️ TROUBLESHOOTING

### ❌ Blank Page / "process is not defined"
- **Fixed!** This was the main bug
- Clear browser cache: `Ctrl+Shift+Delete`
- Hard refresh: `Ctrl+Shift+R`

### ❌ Backend Connection Refused
- Verify backend is running on Terminal 1
- Check: `http://localhost:8000/health` in browser
- Should return: `{"status":"ok"}`

### ❌ CORS Error
- Backend CORS is configured for localhost:5173
- Make sure frontend is on **port 5173** (not 3000)
- Check backend console for CORS errors

### ❌ Form Won't Submit
- Make sure all 3 fields are selected
- Button should be enabled when all selected
- Check console for validation errors

### ❌ No Results Appear
- Check Network tab for API response
- If 500 error: check backend console for ML errors
- If network failed: check backend is running

---

## 📊 EXPECTED API RESPONSE

When you click "Get Recommendation", the browser sends:

**Request:**
```json
POST http://localhost:8000/api/predict
{
  "skin_type": "Oily",
  "sensitivity": "Medium",
  "concern": "Acne"
}
```

**Response:**
```json
{
  "success": true,
  "ingredient": "Niacinamide",
  "cluster_label": "Type A - Balanced",
  "cluster_number": 0,
  "confidence": 0.94,
  "ingredient_confidence": 0.92,
  "cluster_confidence": 0.96,
  "error": null
}
```

---

## ✨ SUCCESS INDICATORS

✅ **All of these should be true:**

1. No console errors on page load
2. Form loads with all 3 input sections
3. Button responds to clicks
4. Loading spinner shows during API call
5. Results display with real data (not dummy values)
6. Results scroll into view automatically
7. Can fill form again and get new results
8. Error message shows if backend is down

---

## 🎯 NEXT STEPS

Once testing confirms this works:

1. **ProductRecommendations** - Can integrate API call to `/api/recommend`
2. **RoutineBuilder** - Can integrate API call to `/api/routine`
3. **Add validation** - Better form validation
4. **Add caching** - React Query for request caching
5. **Improve UX** - Loading skeletons, animations

---

## 📞 SUPPORT

If you see any issues:

1. Check **Console** tab (F12) - paste error message
2. Check **Network** tab - verify request/response
3. Verify backend is running: `curl http://localhost:8000/health`
4. Verify frontend is on port 5173: `http://localhost:5173`

---

**Status:** ✅ Ready to Test
**Date:** 2026-04-23
