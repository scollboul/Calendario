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

    def EliminarRecordatorios(self):
        query = QtSql.QSqlQuery()
        query.prepare(
            'delete from Recordatorios')
        if query.exec_():
            while query.next():
                print("Eliminación correcta")
        else:
            print("Error eliminacion:", query.lastError().text())
    def EliminarRecordatorio(Date):
        query = QtSql.QSqlQuery()
        query.prepare(
            'delete from Recordatorios where Fecha=:Date')
        if query.exec_():
            while query.next():
                print("Eliminación correcta")
        else:
            print("Error eliminacion:", query.lastError().text())

    def MostrarRecordatorios(self):
        query=QtSql.QSqlQuery()
        query.prepare('select * from Recordatorios')
        if query.exec_():
            while query.next():
                    var.Mostrar = BoxLayout(orientation="horizontal", size_hint=(1, None), height=40)
                    var.Mostrar.add_widget(Label(text=str(query.value(1))))
                    var.Mostrar.add_widget(Label(text=str(query.value(0))))
                    self.root.add_widget(var.Mostrar)
        else:
            print("erro Mostrar", query.lastError().text())