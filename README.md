# 🚀 AI-Based Sentiment Analysis API

This is a **FastAPI-based** AI-powered Sentiment Analysis API that classifies text as **Positive, Negative, or Neutral**. It is containerized with **Docker** and includes **automated testing & CI/CD**.

## 📌 Features
✅ AI-driven **sentiment analysis** (VADER)  
✅ **FastAPI** for high-performance REST API  
✅ **Dockerized** for easy deployment  
✅ **Unit tests** with `pytest`  
✅ **CI/CD pipeline** using GitHub Actions  

---

## 🛠 Installation

### **Requirements**
- Python 3.10+
- FastAPI
- Uvicorn
- Docker (optional, for containerization)

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/sentiment-api.git
cd sentiment-api
```

### **2️⃣ Create a Virtual Environment**
```sh
conda create --name venv python=3.10 -y
conda activate venv
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the FastAPI Application**
```sh
uvicorn app.main:app --reload
```
API will be available at:  
➡️ **http://127.0.0.1:8000/docs** (Swagger UI)  
➡️ **http://127.0.0.1:8000/redoc** (ReDoc UI)  

---

## 🐓 Docker Setup (Optional)

### **1️⃣ Build the Docker Image**
```sh
docker build -t sentiment-api .
```

### **2️⃣ Run the Container**
```sh
docker run -d -p 8000:8000 sentiment-api
```

Now, visit ➡️ **http://localhost:8000/docs**

---

## 🔗 API Endpoints

### ✅ **Health Check**
```http
GET /v1/health/
```
**Response:**
```json
{"status": "API is healthy ✅"}
```

### 📝 **Sentiment Analysis**
```http
POST /v1/analyze/
```
**Request Body:**
```json
{
  "text": "I love this!"
}
```
**Response:**
```json
{
  "sentiment": "positive",
  "confidence": 0.98
}
```

---

## 🧪 Running Tests

### **1️⃣ Install `pytest`**
```sh
pip install pytest
```

### **2️⃣ Run Tests**
```sh
pytest
```
✅ If tests pass, your API is working fine!

---

## 🚀 CI/CD (GitHub Actions)

This project uses **GitHub Actions** to **automate testing on every push**.

### **Pipeline Includes:**
- ✅ Auto-run `pytest` on each commit  
- ✅ Ensures API is always stable  

### **Setup**
1. Push your code to **GitHub**
2. GitHub Actions will **automatically test the API**  

---

## 🌍 Deployment

### ** Deploy to Railway **
```sh
railway init
railway up
```

### 👨‍💻 **Author**  
- **Rohan Ananthula**  
- **Email:** rohanananthulauk@gmail.com  
- **GitHub:** [@roxn21](https://github.com/roxn21)  

---