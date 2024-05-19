from flask import Blueprint, jsonify, make_response, request, render_template, redirect
router = Blueprint('api', __name__)

@router.route('/')

def home():
    return render_template('index.html')
