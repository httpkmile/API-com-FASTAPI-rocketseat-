from fastapi import FastAPI 
from src .main .routes .users_routes import users_routers 

app =FastAPI ()
app .include_router (users_routers )
