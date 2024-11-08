from fastapi import APIRouter, status, Depends

from core.projects.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)

from core.projects.dependencies import get_db
from core.projects.service import create_project, get_all_projects, get_project_by_id
from core.projects.schemas import GetProject, Project
from core.auth.utils import admin_required

router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA
)


@router.post("/projects/", dependencies=[Depends(admin_required)], response_model=GetProject)
async def create_project_view(project: Project, db=Depends(get_db)):
    project = create_project(db, project.model_dump())
    return GetProject.model_construct(**project)

@router.get("/projects/", response_model=list[GetProject])
async def get_projects_view(db=Depends(get_db)):
    projects = get_all_projects(db)
    return [GetProject.model_construct(**project) for project in projects]

@router.get("/projects/{project_id}", response_model=GetProject)
async def get_project_view(project_id: str, db=Depends(get_db)):
    project = get_project_by_id(db, project_id)
    return GetProject.model_construct(**project)