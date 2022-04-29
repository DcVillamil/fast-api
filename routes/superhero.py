from fastapi import APIRouter
from config.db import conn
from schemas.superhero import superEntity,supersEntity
from pymongo import MongoClient
from bson import ObjectId
from models.superhero import Super

superhero = APIRouter()


client = MongoClient("mongodb+srv://dcvillamil:dcvillamil12345@cluster0.w4fa5.mongodb.net/laboratorio?retryWrites=true&w=majority")
db = client.test

mydb = client["laboratorio"]
mycol = mydb["superheros"]

@superhero.get('/superheros')
def find_all():
    return supersEntity(mycol.find())

@superhero.get('/superhero/{id}')
def find_superhero(id:str):
    return superEntity(mycol.find_one({"_id":ObjectId(id)}))

@superhero.post('/crear')
def crear(super:Super):
    new_super = dict(super)
    mycol.insert_one(new_super)
    return "recibido"