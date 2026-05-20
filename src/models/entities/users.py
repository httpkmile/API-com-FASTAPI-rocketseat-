from src .models .settings .metadata import metadata 
from sqlalchemy import Table ,Column ,Integer ,String 

Users =Table (
"users",
metadata ,

Column (
"id",
Integer ,
primary_key =True 
),

Column (
"username",
String ,
nullable =False 
),

Column (
"age",
Integer ,
nullable =False ,

),

Column (
"uf",
String ,
nullable =False 
)
)