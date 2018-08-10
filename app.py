from PyQt4.QtGui import (QFileDialog, QMainWindow, QApplication, QListWidget)
from PyQt4.QtCore import (QProcess, QFileInfo, QThread)
import interface
import sys #creo que no va
import os #para acceder al funciones de sistema (para crear directorio en este caso)
from PyQt4.QtCore import (QDir, QMutex, QWaitCondition) #lo mismo que arriba

wait_condition = QWaitCondition()
mutex = QMutex()
mutex2 = QMutex()
contador = 1

class MainWindow(QMainWindow, interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self) #linea para jalar todos los componentes de la interface

        self.bAgregar.clicked.connect(self.funcionAgregar)
        self.bBorrar.clicked.connect(self.funcionBorrar)
        self.bBorrarTodo.clicked.connect(self.funcionBorrarTodo)
        self.bComprimir.clicked.connect(self.funcionComprimir)
        self.a = []
        self.proceso_comando = QProcess(self)

    def funcionAgregar(self):
        homeUsuario = QDir.homePath()
        rutaPdf = QFileDialog.getOpenFileName(self, directory=homeUsuario) #indico que me abra en el home del usuario
        objetoPDF = QFileInfo(rutaPdf)
        #self.listWidget.addItem(QFileDialog.getOpenFileName())
        self.listWidget.addItem(objetoPDF.fileName())

        self.a.append(unicode(rutaPdf))

        print(self.a)
        print("contenido de arreglo a")


    def funcionBorrar(self):
        self.listWidget.takeItem(self.listWidget.currentRow())


    def funcionBorrarTodo(self):
        self.listWidget.clear()


    def funcionComprimir(self):
        global contador
        numHilos = QThread.idealThreadCount()

        user_home = QDir.homePath() #home del usuario

        try:
            os.mkdir(os.path.join(unicode(user_home), 'carpetadeliss'))
            # os.mkdir(user_home+'/micarpeta') #es lo mismo que la linea de arriba
        except (OSError):
            print("Carpeta ya existe.")

        #print("rutaGuardar")
        rutaGuardar = os.path.join(unicode(user_home), 'carpetadeliss')

        #self.proceso_comando.start('cpdf', ['-squeeze', elementoPDF, '-o', os.path.join(rutaGuardar, unicode(pdfName))])
        #self.proceso_comando.start('ls', ['-l'])
        # (comando, ['arg1' ,  'arg2',  'argN'])


        #for _ in self.a : es lo mismo que abajo
        procesos = [] # lista con procesos y lanzar
        for _ in range(0, len(self.a)):
            i = QProcess(self)
            i.finished.connect(self.funcionFinised)
            procesos.append(i)

        while len(self.a) != 0:
            mutex.lock()
            if contador <= 2:

                elementoPDF = self.a.pop()  # hace pop al ultimo elemento de la lista
                pdfName = QFileInfo(elementoPDF).fileName()


                contador = contador + 1
                print("contador 1", contador)
                proceso_me = procesos.pop()
                print("u1")
                mutex.unlock()
                proceso_me.start('cpdf', ['-squeeze', elementoPDF, '-o', os.path.join(rutaGuardar, unicode(pdfName))])
            else:
                print("u2")
                mutex.unlock()
                print("...................")
                mutex2.lock()
                print("mkcbnveoirbvrpobgt---------")
                wait_condition.wait(mutex2)

                print("mutex2")
                mutex2.unlock()



    def funcionFinised(self):
        print("termine!!!!!!!!!!!!!!!!")
        global contador

        mutex.lock()
        contador = contador - 1
        mutex.unlock()
        wait_condition.wakeAll()

#todo hacer que se esperen los procesos-hilos
#todo en funcionFinised hacer que despierte
#en la variable compartida ver cuantos hilos se estan ejecutando





if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Compresor PDF')
    app.setApplicationVersion('1')
    window = MainWindow()
    window.show()
    app.exec_()
