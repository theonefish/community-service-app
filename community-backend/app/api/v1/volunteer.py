from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.volunteer import VolunteerProject, VolunteerRecord
from app.schemas.volunteer import VolunteerProjectOut
from app.schemas import resp_ok

router = APIRouter(prefix="/volunteer", tags=["志愿服务"])


@router.get("/projects", summary="获取志愿项目列表")
async def get_volunteer_projects(
    category: str = Query("", description="分类筛选"),
    db: AsyncSession = Depends(get_db),
):
    query = select(VolunteerProject).where(VolunteerProject.status != "ended").order_by(VolunteerProject.created_at.desc())

    if category:
        query = query.where(VolunteerProject.category == category)

    result = await db.execute(query)
    projects = result.scalars().all()

    data = [VolunteerProjectOut.model_validate(p).model_dump() for p in projects]
    return resp_ok(data=data)


@router.post("/projects/{project_id}/join", summary="报名参加志愿项目")
async def join_volunteer_project(
    project_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(VolunteerProject).where(VolunteerProject.id == project_id))
    project = result.scalar_one_or_none()

    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="项目不存在")

    if project.status == "full":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="项目名额已满")

    # 检查是否已报名
    existing = await db.execute(
        select(VolunteerRecord).where(VolunteerRecord.user_id == user.id, VolunteerRecord.project_id == project_id)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="已报名该项目")

    record = VolunteerRecord(user_id=user.id, project_id=project_id)
    db.add(record)

    project.current_count = (project.current_count or 0) + 1
    if project.max_count > 0 and project.current_count >= project.max_count:
        project.status = "full"

    return resp_ok(message="报名成功")


@router.get("/my-hours", summary="获取我的志愿时长")
async def get_my_volunteer_hours(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(func.sum(VolunteerRecord.hours)).where(VolunteerRecord.user_id == user.id)
    )
    total_hours = float(result.scalar() or 0)

    return resp_ok(data={"total_hours": total_hours})


@router.get("/my-projects", summary="获取我参加的志愿项目")
async def get_my_volunteer_projects(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(VolunteerProject)
        .join(VolunteerRecord, VolunteerRecord.project_id == VolunteerProject.id)
        .where(VolunteerRecord.user_id == user.id)
        .order_by(VolunteerRecord.joined_at.desc())
    )
    projects = result.scalars().all()

    data = [VolunteerProjectOut.model_validate(p).model_dump() for p in projects]
    return resp_ok(data=data)
