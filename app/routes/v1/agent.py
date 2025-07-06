from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.db import get_db
from app.schemas.agent import AgentCreate, AgentRead
from app.services.agent import create_agent as create_agent_service, get_agent as get_agent_service, get_all_agents as get_all_agents_service

router = APIRouter(prefix="/agents", tags=["Agents"])

@router.post("/", response_model=AgentRead)
def create_agent(agent_in: AgentCreate, db: Session = Depends(get_db)):
    return create_agent_service(db, agent_in)

@router.get("/{agent_id}", response_model=AgentRead)
def get_agent(agent_id: UUID, db: Session = Depends(get_db)):
    agent = get_agent_service(db, agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@router.get("/", response_model=list[AgentRead])
def list_agents(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return get_all_agents_service(db, skip, limit)