from PyQt5 import QtWidgets, QtSql
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
            'insert to Recordatorios (Fecha, Recordatorio)'
            'VALUES (:Fecha, :Recordatorio)')
        query.bindValue(':fecha',str(Rec[0]))
        query.bindValue(':Recordatorio',str(Rec[1]))
        if query.exec_():
            print("Insercion correcta")
        else:
            print("Error:", query.lastError().text())