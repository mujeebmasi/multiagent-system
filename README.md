# Research Assistant

A modern AI-powered research automation system with a full-stack architecture.

## 🏗️ Project Structure

```
├── backend/                    # FastAPI backend
│   ├── app/                   # Application code
│   │   ├── models/           # Pydantic models (schemas)
│   │   ├── routes/           # API routes
│   │   ├── services/         # Business logic
│   │   └── config.py         # Configuration
│   ├── core/                 # Core research logic
│   │   ├── agents.py         # LangChain agents
│   │   ├── tools.py          # LangChain tools
│   │   └── pipeline.py       # Research pipeline
│   ├── main.py              # FastAPI app initialization
│   ├── run.py               # Server runner
│   ├── requirements.txt      # Python dependencies
│   └── .env.example         # Environment template
│
├── frontend/                 # React TypeScript frontend
│   ├── src/
│   │   ├── components/      # Reusable React components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API client services
│   │   ├── types/          # TypeScript types
│   │   ├── styles/         # Global styles
│   │   ├── App.tsx         # Root component
│   │   └── main.tsx        # Entry point
│   ├── package.json        # Node dependencies
│   ├── vite.config.ts      # Vite configuration
│   ├── tailwind.config.js  # Tailwind configuration
│   └── tsconfig.json       # TypeScript configuration
│
└── README.md               # This file
```

## ⚙️ Features

### Backend
- **FastAPI** - Modern, fast Python web framework
- **LangChain** - Framework for building LLM applications
- **Gemini AI** - Advanced language model
- **Tavily Search** - Web search API
- **Web Scraping** - BeautifulSoup for content extraction
- **CORS Support** - Cross-origin resource sharing enabled

### Frontend
- **React** - UI framework
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Vite** - Lightning-fast build tool
- **Axios** - HTTP client
- **React Markdown** - Markdown rendering

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- API Keys: Google Gemini, Tavily Search

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
# Edit .env with your API keys
```

5. Run the server:
```bash
python run.py
```

Server runs on http://localhost:8000

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm run dev
```

Open http://localhost:5173 in your browser

## 📚 API Endpoints

### Health Check
```
GET /api/health
```

### Conduct Research
```
POST /api/research
Content-Type: application/json

{
  "topic": "Your research topic"
}
```

### Interactive Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔄 How It Works

1. **Search Phase**: Uses Tavily to search the web for the topic
2. **Scraping Phase**: Scrapes and extracts content from relevant URLs
3. **Analysis Phase**: Combines search and scraped data
4. **Report Generation**: Generates detailed research report using Gemini
5. **Feedback Phase**: Provides critique and suggestions for the report

## 🛠️ Development

### Backend Development
```bash
cd backend
python run.py  # Runs with auto-reload
```

### Frontend Development
```bash
cd frontend
npm run dev
```

### Type Checking (Frontend)
```bash
npm run type-check
```

### Build for Production

Backend:
```bash
# No build needed - runs directly
```

Frontend:
```bash
npm run build  # Creates optimized dist/
```

## 📦 Project Organization

The codebase follows these principles:

- **Separation of Concerns**: Backend and frontend are independent
- **Modular Structure**: Each component has a single responsibility
- **Type Safety**: Full TypeScript support
- **CORS Enabled**: Frontend and backend can run on different ports
- **Environment Configuration**: Sensitive data in .env files
- **API Documentation**: Automatic Swagger/ReDoc generation

## 🔐 Security Notes

- Never commit `.env` files
- API keys are private - use environment variables
- CORS is configured for localhost development only
- Update CORS origins for production deployment

## 📝 Environment Variables

### Backend (.env)
```
DEBUG=True
HOST=0.0.0.0
PORT=8000
GOOGLE_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
FRONTEND_URL=http://localhost:5173
```

### Frontend
- API endpoint: `http://localhost:8000/api` (hardcoded, customize in `src/services/apiClient.ts`)

## 🐛 Troubleshooting

**Frontend can't connect to backend**
- Ensure backend is running on port 8000
- Check CORS origins in `backend/app/config.py`
- Check browser console for CORS errors

**Backend API errors**
- Check `.env` file for missing API keys
- Verify internet connection for web search
- Check logs in terminal for detailed errors

**Module import errors (Backend)**
- Ensure you're in the correct virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

## 🚀 Deployment

### Backend (Heroku/Railway)
```bash
# Ensure Procfile exists with: web: uvicorn main:app --host 0.0.0.0 --port $PORT
# Deploy to your platform
```

### Frontend (Vercel/Netlify)
```bash
npm run build
# Deploy the dist/ folder
```

## 📄 License

MIT

## 🤝 Contributing

Contributions welcome! Feel free to improve the structure or add features.
