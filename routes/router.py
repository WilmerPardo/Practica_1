from flask import Blueprint, jsonify, make_response, request, render_template, redirect
from controls.facturaDaoControl import FacturaDaoControl
from controls.retencionDaoControl import RetencionDaoControl

router = Blueprint('api', __name__)

@router.route('/')

def home():
    return render_template('template.html')


@router.route('/historial')

def lista_historial():
    hd = RetencionDaoControl()
    return render_template('factura/lista.html', lista = hd.to_dict())

