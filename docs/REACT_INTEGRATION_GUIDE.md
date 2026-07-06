# GlowGuide Backend - React Integration Guide

## 🔌 Connection Setup

### 1. Start the Backend Server
```bash
cd c:\Users\Nakshatra Rao\GlowGuide
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Configure React Frontend
Add to your React `.env` or API configuration:
```
REACT_APP_API_URL=http://localhost:8000
```

Or in your fetch calls:
```javascript
const API_BASE_URL = "http://localhost:8000/api";
```

---

## 📡 API Endpoints

All endpoints accept JSON and return JSON responses.

### Base URL
```
http://localhost:8000/api
```

---

## 🔍 Endpoint Reference

### 1. Predict Ingredient & Cluster

**Endpoint**: `POST /api/predict`

**Purpose**: Get primary ingredient recommendation and skin cluster for a user profile

**Request**:
```javascript
const response = await fetch("http://localhost:8000/api/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    skin_type: "Oily",      // Required: 'Combination' | 'Dry' | 'Normal' | 'Oily'
    sensitivity: "Yes",     // Optional: 'No' | 'Yes' (default: 'No')
    concern: "Acne"         // Required: see valid concerns below
  })
});
const result = await response.json();
```

**Response (Success)**:
```json
{
  "success": true,
  "ingredient": "Salicylic Acid",
  "cluster_label": "Acne-Prone",
  "cluster_number": 0,
  "confidence": 0.85,
  "ingredient_confidence": 0.87,
  "cluster_confidence": 0.83,
  "error": null
}
```

**Response (Error)**:
```json
{
  "success": false,
  "error": "Unknown skin_type 'Sensitive'. Valid options: ['Combination', 'Dry', 'Normal', 'Oily']",
  "ingredient": null,
  "cluster_label": null
}
```

**Valid Values**:
- `skin_type`: `Combination`, `Dry`, `Normal`, `Oily`
- `sensitivity`: `No`, `Yes`
- `concern`: `Acne`, `Dark Circles`, `Dark Spots`, `Dullness`, `Hyperpigmentation`, `Open Pores`, `Redness`, `Sun Tan`, `Whiteheads / Blackheads`, `Wrinkles`

---

### 2. Get Recommendations

**Endpoint**: `POST /api/recommend`

**Purpose**: Get scored ingredient recommendations for a skin profile

**Request**:
```javascript
const response = await fetch("http://localhost:8000/api/recommend", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    skin_type: "Oily",        // Required: 'Combination' | 'Dry' | 'Normal' | 'Oily'
    concerns: ["Acne"],       // Required: array of concern strings
    age: 24,                  // Optional: integer 13-80 (default: 25)
    preferences: {}           // Optional: empty dict or custom preferences
  })
});
const result = await response.json();
```

**Response (Success)**:
```json
{
  "success": true,
  "recommendations": [
    {
      "ingredient": "Salicylic Acid",
      "score": 4.0,
      "reasoning": [
        "Best for Oily skin",
        "Primary ingredient for acne treatment"
      ]
    },
    {
      "ingredient": "Niacinamide",
      "score": 3.5,
      "reasoning": [
        "Sebum control",
        "Acne prevention support"
      ]
    },
    {
      "ingredient": "Clay",
      "score": 3.0,
      "reasoning": [
        "Oil absorption",
        "Pore cleansing"
      ]
    }
  ],
  "count": 8,
  "error": null
}
```

---

### 3. Full Pipeline (Prediction + Products + Remedies)

**Endpoint**: `POST /api/full`

**Purpose**: Complete skincare solution with ingredient, products, and home remedies

**Request**:
```javascript
const response = await fetch("http://localhost:8000/api/full", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    skin_type: "Normal",       // Required: 'Combination' | 'Dry' | 'Normal' | 'Oily'
    sensitivity: "No",         // Optional: 'No' | 'Yes' (default: 'No')
    concern: "Dark Spots"      // Required: see valid concerns
  })
});
const result = await response.json();
```

**Response (Success)**:
```json
{
  "success": true,
  "ingredient": "Vitamin C",
  "cluster_label": "Dry Skin",
  "products": [
    {
      "name": "Radiant Vitamin C Serum",
      "url": "https://example.com/product1",
      "type": "serum",
      "price": 49.99
    },
    {
      "name": "Brightening Vitamin C Moisturizer",
      "url": "https://example.com/product2",
      "type": "moisturizer",
      "price": 45.00
    }
  ],
  "remedies": [
    {
      "remedy": "Turmeric Mask",
      "benefit": "Natural skin brightening"
    },
    {
      "remedy": "Lemon Face Pack",
      "benefit": "Spot reduction"
    }
  ],
  "confidence": 0.82,
  "error": null
}
```

---

### 4. Personalized Skincare Routine

**Endpoint**: `POST /api/routine`

**Purpose**: Generate personalized morning or evening skincare routine

**Request**:
```javascript
const response = await fetch("http://localhost:8000/api/routine", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    skin_type: "Oily",              // Required: 'Combination' | 'Dry' | 'Normal' | 'Oily'
    sensitivity: "Yes",             // Optional: 'No' | 'Yes' (default: 'No')
    concern: "Acne",                // Required: see valid concerns
    routine_type: "Morning",        // Optional: 'Morning' | 'Evening' (default: 'Morning')
    routine_focus: "Acne Control"   // Optional: routine focus area
  })
});
const result = await response.json();
```

**Response (Success)**:
```json
{
  "success": true,
  "routine_type": "Morning",
  "focus_area": "Acne Control",
  "steps": [
    {
      "step": 1,
      "action": "Cleanse",
      "product": "Gentle Acne Face Wash",
      "duration_minutes": 2,
      "notes": "Use lukewarm water to avoid irritation"
    },
    {
      "step": 2,
      "action": "Tone",
      "product": "Witch Hazel Toner",
      "duration_minutes": 1,
      "notes": "Helps balance skin pH and control sebum"
    },
    {
      "step": 3,
      "action": "Treat",
      "product": "Salicylic Acid Serum",
      "duration_minutes": 2,
      "notes": "Apply to acne-prone areas only"
    },
    {
      "step": 4,
      "action": "Moisturize",
      "product": "Oil-Free Moisturizer",
      "duration_minutes": 2,
      "notes": "Essential even for oily skin"
    },
    {
      "step": 5,
      "action": "Protect",
      "product": "SPF 50 Sunscreen",
      "duration_minutes": 2,
      "notes": "Non-negotiable for oily acne-prone skin"
    }
  ],
  "total_time": 15,
  "tips": [
    "Use non-comedogenic products only",
    "Avoid over-washing face",
    "Never skip sunscreen",
    "Be consistent for 4-6 weeks to see results",
    "Patch test new products on jaw first"
  ],
  "error": null
}
```

---

## 🎯 React Integration Examples

### Example 1: Simple Prediction Hook
```javascript
import { useState } from 'react';

function usePrediction() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const predict = async (skinType, sensitivity, concern) => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch("http://localhost:8000/api/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          skin_type: skinType,
          sensitivity: sensitivity,
          concern: concern
        })
      });
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      
      const data = await response.json();
      
      if (!data.success) {
        setError(data.error);
        return null;
      }
      
      return data;
    } catch (err) {
      setError(err.message);
      return null;
    } finally {
      setLoading(false);
    }
  };

  return { predict, loading, error };
}

export default usePrediction;
```

### Example 2: Error Handling Pattern
```javascript
async function getRecommendations(skinType, concerns, age) {
  try {
    const response = await fetch("http://localhost:8000/api/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        skin_type: skinType,
        concerns: concerns,
        age: age,
        preferences: {}
      })
    });

    // Handle HTTP errors
    if (!response.ok) {
      if (response.status === 422) {
        return {
          success: false,
          error: "Invalid input format"
        };
      } else if (response.status === 400) {
        return {
          success: false,
          error: "Invalid input values"
        };
      } else if (response.status === 500) {
        return {
          success: false,
          error: "Server error"
        };
      }
    }

    const data = await response.json();
    return data;
  } catch (err) {
    return {
      success: false,
      error: `Network error: ${err.message}`
    };
  }
}
```

---

## 📋 Valid Input Values

### Skin Types
```javascript
const SKIN_TYPES = ["Combination", "Dry", "Normal", "Oily"];
```

### Sensitivities
```javascript
const SENSITIVITIES = ["No", "Yes"];
```

### Concerns
```javascript
const CONCERNS = [
  "Acne",
  "Dark Circles",
  "Dark Spots",
  "Dullness",
  "Hyperpigmentation",
  "Open Pores",
  "Redness",
  "Sun Tan",
  "Whiteheads / Blackheads",
  "Wrinkles"
];
```

### Routine Types
```javascript
const ROUTINE_TYPES = ["Morning", "Evening"];
```

---

## ⚠️ Error Handling

### Status Codes
- **200**: Success
- **400**: Business logic error (e.g., invalid concern value)
- **422**: Validation error (e.g., missing required field, wrong type)
- **500**: Server error

### Response Format
All errors follow this format:
```json
{
  "success": false,
  "error": "Human-readable error message",
  "detail": "Additional technical details (if available)"
}
```

### Common Errors
```javascript
// Unknown skin type
{
  "success": false,
  "error": "Unknown skin_type 'Sensitive'. Valid options: ['Combination', 'Dry', 'Normal', 'Oily']"
}

// Missing required field
{
  "success": false,
  "error": "422 Validation Error",
  "detail": [
    {
      "loc": ["body", "concern"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}

// Invalid age range
{
  "success": false,
  "error": "Age must be integer between 13-80, got 150"
}
```

---

## 🧪 Testing with cURL

### Test Prediction
```bash
curl -X POST http://localhost:8000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"skin_type":"Oily","sensitivity":"Yes","concern":"Acne"}'
```

### Test Recommendations
```bash
curl -X POST http://localhost:8000/api/recommend \
  -H "Content-Type: application/json" \
  -d '{"skin_type":"Oily","concerns":["Acne"],"age":24}'
```

### Test Routine
```bash
curl -X POST http://localhost:8000/api/routine \
  -H "Content-Type: application/json" \
  -d '{"skin_type":"Oily","concern":"Acne","routine_type":"Morning"}'
```

---

## 🚀 Deployment Notes

### Production Checklist
- [ ] Update CORS `allow_origins` to restrict to your frontend domain
- [ ] Set environment variable for API URL in React build
- [ ] Test all endpoints with various inputs before deploying
- [ ] Monitor backend logs for errors
- [ ] Set up database for storing user preferences (optional)
- [ ] Implement authentication if needed

### Update CORS for Production
```python
# In backend/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📞 Support

If you encounter any issues:
1. Check API_VALIDATION_REPORT.md for expected behavior
2. Verify all required fields are present in requests
3. Check that values match the valid options list
4. Review backend logs for detailed error information
