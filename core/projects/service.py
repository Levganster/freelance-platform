from datetime import datetime, timedelta
from bson import ObjectId
from core.exceptions import NotFoundException

def create_project(db, project_data):
    project_data['status'] = 'создан'
    project_data['deadline'] = (datetime.now() + timedelta(days=project_data['time_to_complete'])).strftime("%Y %m.%d %H:%M")
    db.projects.insert_one(project_data)
    return project_data

def get_all_projects(db):
    projects = list(db.projects.find())
    for project in projects:
        project['id'] = str(project['_id'])
        del project['_id']
    return projects

def get_project_by_id(db, project_id):
    project = db.projects.find_one({"_id": ObjectId(project_id)})
    if project is None:
        raise NotFoundException()
    return project