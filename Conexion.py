from PyQt5 import QtWidgets, QtSql
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout
import calendar
from datetime import datetime
from kivy.uix.textinput import TextInput
import Conexion
import var

import var
class conexion():
    def db_connect(filename):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(str(filename))
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer conexion.\n'
                                           'Haz Click para Cancelar.', QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexión Establecida')
        return True

    def Altrecor(Rec):
        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into Recordatorios (Fecha, Recordatorio)'
            'VALUES (:Fecha, :Recordatorio)')
        query.bindValue(':Fecha',str(Rec[0]))
        query.bindValue(':Recordatorio',str(Rec[1]))
        if query.exec_():
            print("Insercion correcta")
        else:
            print("Error inserccion:", query.lastError().text())

    def MostrarFacturas(Rec):
        query = QtSql.QSqlQuery()
        print(Rec)
        query.prepare(
            'select Fecha, Recordatorio from Recordatorios where Fecha = :Dia')
        if query.exec_():
            while query.next():
                fecha=query.value(0)
                recordatorio= query.value(1)

            print("Insercion correcta")
        else:
            print("Error inserccion:", query.lastError().text())