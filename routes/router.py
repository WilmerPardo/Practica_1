from flask import Blueprint, jsonify, make_response, request, render_template, redirect
from controls.facturaDaoControl import FacturaDaoControl
from controls.retencionDaoControl import RetencionDaoControl

router = Blueprint('api', __name__)

@router.route('/')
def home():
    return render_template('template.html')


@router.route('/historial')
def lista_historial():
    hd = FacturaDaoControl()
    return render_template('factura/lista.html', lista = hd.to_dic())

@router.route('/historial/ver')
def ver_guardad():
    return render_template('factura/guardar.html')


@router.route('/historial/guardar', methods=['POST'])
def guardar_factura():

    factura = FacturaDaoControl()
    factura._factura._usuario = request.form['usuario']
    factura._factura._monto = request.form['monto']
    factura._factura._ruc = request.form['ruc']
    factura._factura._tipo_ruc = request.form['tipo_ruc']
    factura._factura._fecha = request.form['fecha']
    

    return redirect('/historial', code = 302)