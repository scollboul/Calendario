from PyQt5 import QtWidgets, QtSql
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
        print(Rec)
        query.prepare(
            'insert into Recordatorios (Fecha, Recordatorio)'
            'VALUES (:Fecha, :Recordatorio)')
        query.bindValue(':Fecha',str(Rec[0]))
        query.bindValue(':Recordatorio',str(Rec[1]))
        if query.exec_():
            print("Insercion correcta")
            conexion.MostrarRecorddatorios()
        else:
            print("Error inserccion:", query.lastError().text())

    def MostrarRecorddatorios():
        query = QtSql.QSqlQuery()
        query.prepare(
            'select Fecha, Recordatorio from Recordatorios where Fecha = :Dia')
        if query.exec_():
            while query.next():
                recordatorio=query.value(1)

            print("Insercion correcta")
        else:
            print("Error inserccion:", query.lastError().text())