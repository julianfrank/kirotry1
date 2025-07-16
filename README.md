# JFGlobalExpress Courier Bot Website

A comprehensive global courier service website with an intelligent interactive bot that replaces traditional forms. Built with React frontend, FastAPI backend, Windmill for AI orchestration, and local Ollama for AI processing.

## Project Structure

```
├── frontend/           # React.js frontend application
├── backend/            # FastAPI backend server
├── fastmcp/            # FastMCP server for courier services
├── docker/
│   └── nginx/          # Nginx reverse proxy configuration
├── .kiro/
│   └── specs/          # Project specifications and requirements
├── docker-compose.yml  # Docker Compose configuration
├── .env                # Environment variables
└── README.md           # This file
```

## Services Architecture

- **Frontend**: React.js with TypeScript (Port 3000)
- **Backend API**: FastAPI with Python (Port 8000)
- **Nginx**: Reverse proxy (Port 80)
- **Windmill**: Workflow orchestration (Port 8001)
- **Ollama**: Local AI inference (Port 11434)
- **FastMCP**: Model Context Protocol server (Port 8002)
- **Redis**: Caching and sessions (Port 6379)
- **PostgreSQL**: Windmill database (Port 5432)
- **DuckDB**: Main application database (embedded)

## Quick Start

1. **Clone and setup**:
   ```bash
   git clone <repository>
   cd courier-bot-website
   ```

2. **Start all services**:
   ```bash
   docker-compose up -d
   ```

3. **Access the application**:
   - Website: http://localhost
   - Windmill Admin: http://localhost/windmill
   - API Documentation: http://localhost/api/docs

4. **Stop all services**:
   ```bash
   docker-compose down
   ```

## Development

### Environment Variables

Copy `.env.example` to `.env` and adjust values as needed:
```bash
cp .env.example .env
```

### Service Dependencies

The services start in the following order:
1. PostgreSQL, Redis, DuckDB
2. Ollama (AI models)
3. FastMCP (courier services)
4. Windmill (workflow orchestration)
5. Backend API
6. Frontend
7. Nginx (reverse proxy)

### Data Persistence

- **DuckDB**: Application data stored in `duckdb_data` volume
- **Ollama**: AI models stored in `ollama_data` volume
- **Redis**: Cache data stored in `redis_data` volume
- **PostgreSQL**: Windmill data stored in `postgres_data` volume

## Features

- **Intelligent Bot**: Conversational interface for courier services
- **Real-time Tracking**: Interactive maps with live location updates
- **Multi-AI Support**: Switch between Ollama, AWS Bedrock, Google Gemini, Azure OpenAI, ChatGPT
- **Admin Interface**: Courier management and reporting dashboard
- **Global Analytics**: World map with shipment and revenue visualization
- **Containerized**: Complete Docker Compose deployment

## Requirements

- Docker and Docker Compose
- At least 4GB RAM (for Ollama AI models)
- 10GB disk space (for AI models and data)

## Next Steps

This is the initial project structure. The following tasks will implement:
1. Database schema and seed data
2. FastAPI backend with core endpoints
3. FastMCP server for courier services
4. Windmill workflows for AI orchestration
5. React frontend with bot widget
6. Admin interface and reporting
7. Real-time features and WebSocket integration
8. AI model setup and multi-provider support
9. Security and authentication
10. Comprehensive testing
11. Final integration and deployment testing