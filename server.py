from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('mongodb+srv://yigyuseok:Rbtjr1693!@cluster0.fvajf.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
