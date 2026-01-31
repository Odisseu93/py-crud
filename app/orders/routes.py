from fastapi import APIRouter

orders_router = APIRouter(
  prefix='/orders',
  tags='[orders]'
  )
"""
Routes for those responsible for managing user requests.
"""

