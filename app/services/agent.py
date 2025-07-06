from sqlalchemy.orm import Session
from app.models.agent import Agent
from app.schemas.agent import AgentCreate

def create_agent(db: Session, agent_in: AgentCreate) -> Agent:
    agent = Agent(**agent_in.dict())
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent

def get_agent(db: Session, agent_id) -> Agent | None:
    return db.query(Agent).filter(Agent.id == agent_id).first()

def get_all_agents(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Agent).offset(skip).limit(limit).all()