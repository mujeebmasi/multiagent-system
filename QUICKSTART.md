# 🚀 Quick Start Guide

## 📁 Project Structure Created

Your project is now organized with a **full-stack architecture**:

```
Langchain Project/
├── backend/              # FastAPI server
│   ├── app/             # Application code (models, routes, services)
│   ├── core/            # Research logic (agents, tools, pipeline)
│   ├── main.py          # FastAPI app
│   ├── run.py           # Server runner
│   └── requirements.txt
│
├── frontend/            # React + TypeScript + Tailwind
│   ├── src/
│   │   ├── components/  # Reusable components
│   │   ├── pages/       # Page components
│   │   ├── services/    # API client
│   │   ├── types/       # TypeScript types
│   │   └── styles/      # Tailwind CSS
│   ├── package.json
│   └── index.html
│
└── README.md            # Full documentation
```

## ⚡ Quick Setup (5 minutes)

### 1️⃣ Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
# or: source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
copy .env.example .env
# Edit .env and add your API keys:
# - GOOGLE_API_KEY (from Google Cloud)
# - TAVILY_API_KEY (from Tavily)

# Start server
python run.py
```

**Backend runs at:** `http://localhost:8000`

### 2️⃣ Frontend Setup (New Terminal)

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

**Frontend runs at:** `http://localhost:5173`

## ✨ Features

✅ **Search**: Web search using Tavily  
✅ **Scrape**: Extract content from URLs using BeautifulSoup  
✅ **Analyze**: Process with LangChain agents  
✅ **Report**: Generate reports with Gemini AI  
✅ **Feedback**: Get critique on generated reports  

## 🎨 UI Components

- **SearchBar** - Topic input with search
- **ResultsPanel** - Tabbed results view (Report, Feedback, Search, Scraped)
- **LoadingSpinner** - Processing indicator
- **Alert** - Error/success notifications
- **Cards** - Content containers

## 📡 API Endpoints

```
GET  /api/health                  # Health check
POST /api/research                # Conduct research
GET  /docs                        # Swagger UI
GET  /redoc                       # ReDoc
```

## 🔧 Configuration

### Backend Files to Customize
- `backend/app/config.py` - CORS origins, API settings
- `backend/.env` - API keys and environment variables

### Frontend Files to Customize
- `frontend/src/services/apiClient.ts` - API base URL (currently localhost:8000)
- `frontend/tailwind.config.js` - Styling customization

## 📦 Tech Stack

**Backend:**
- FastAPI + Uvicorn
- LangChain + Gemini AI
- Tavily Search
- BeautifulSoup
- Pydantic

**Frontend:**
- React 18
- TypeScript
- Tailwind CSS
- Vite
- Axios

## 🐛 Common Issues

**"Can't connect to backend"**
- Make sure backend is running on port 8000
- Check CORS settings in `backend/app/config.py`

**"API key errors"**
- Verify `.env` file exists and has correct keys
- Restart backend after updating `.env`

**"npm install fails"**
- Delete `node_modules` and `package-lock.json`, try again
- Ensure Node.js 16+ is installed

## 📚 Code Organization

The codebase follows these principles:

- **Separation**: Backend and frontend are independent
- **Modularity**: Each component has single responsibility
- **Type Safety**: Full TypeScript support
- **Scalability**: Easy to add new routes/components
- **Best Practices**: Proper error handling and logging

## 🎯 Next Steps

1. ✅ Install dependencies
2. ✅ Configure API keys
3. ✅ Run both servers
4. ✅ Test with a research topic
5. 🎨 Customize styling with Tailwind
6. 🚀 Add more features or deploy

## 📖 Full Documentation

See `README.md` for comprehensive documentation including:
- Detailed setup instructions
- API documentation
- Deployment guides
- Troubleshooting

---

**Happy researching! 🚀**
