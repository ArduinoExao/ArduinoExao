from PySide2.QtCore import QObject, Slot, QThread, QTranslator
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
import sys, os
import subprocess, time
from threading import Thread
import serial.tools.list_ports
import threading
import shutil



class MainApp(QObject):
    def __init__(self, context, parent=None):
        super(MainApp, self).__init__(parent)
        self.ctx = context


        self.win = parent



    @Slot(QObject,QObject,QObject)
    def effacer(self, series,series2,series3):

        series.clear()
        series2.clear()
        series3.clear()

    @Slot()
    def text(self):

        None


    @Slot(QObject,QObject, QObject,QObject , str , str )
    def update(self, series,series2,series3, axisX, nombreDePoints, tempsDechantillonage):
        self.text()
        t1 = AcquisitionArduino(nombreDePoints, tempsDechantillonage ,series ,series2,series3, axisX)
        t1.daemon = True
        t1.start()


    @Slot()
    def stopThread(self):
        AcquisitionArduino.arreter(self)

    @Slot(result = str)
    def testArduino(self):
        try:
            arduino_ports = [
                p.device
                for p in serial.tools.list_ports.comports()
                if ('CH340') in p.description
            ]
            if not arduino_ports:
                arduino_ports = [
                    p.device
                    for p in serial.tools.list_ports.comports()
                    if ('Arduino') in p.description
                ]
            if not arduino_ports:
                raise IOError("No Arduino found")

            arduino = serial.Serial(arduino_ports[0], 9600)
            arduino.close()

        except:
            arduino_ports = "error"


        ard = str(arduino_ports)
        ard = ard.replace('[','')
        ard = ard.replace(']', '')
        return  ard


    @Slot(str)
    def configArduino(self,capteur):
        repertoire = "./arduinopc/"
        nomDuFicherDesValeurs = "1.bat"

        emplacementDuFichier = os.path.join(repertoire, nomDuFicherDesValeurs)
        dirpath = (os.path.expanduser(r'~\Documents'))
        shutil.copy(emplacementDuFichier, dirpath)

        nomDuFicherDesValeurs = "analoga0.ino.standard.hex"
        emplacementDuFichier = os.path.join(repertoire, nomDuFicherDesValeurs)
        dirpath = (os.path.expanduser(r'~\Documents'))
        shutil.copy(emplacementDuFichier, dirpath)



        try:
            arduino_ports = [
                p.device
                for p in serial.tools.list_ports.comports()
                if ('CH340') in p.description
            ]
            if not arduino_ports:
                arduino_ports = [
                    p.device
                    for p in serial.tools.list_ports.comports()
                    if ('Arduino') in p.description
                ]
            if not arduino_ports:
                raise IOError("No Arduino found")
        except:
            None

        if capteur == "0" :

            path = (os.path.expanduser(r'~\Documents'))
            with open(path + '1.bat', 'w') as filehandle:
                filehandle.write(
                    '"C:/Program Files (x86)/Arduino/hardware/tools/avr/bin/avrdude" -CC:"/Program Files (x86)/Arduino/hardware/tools/avr/etc/avrdude.conf" -v -patmega328p -carduino -P' +
                    arduino_ports[0] + ' -b115200 -D -Uflash:w:' + path + '/analoga0.ino.standard.hex:i')
            exePath = path + "1.bat"

            subprocess.call([exePath])


        if capteur == "1" :
            nomDuFicherDesValeurs = "analoga1.ino.standard.hex"
            emplacementDuFichier = os.path.join(repertoire, nomDuFicherDesValeurs)
            dirpath = (os.path.expanduser(r'~\Documents'))
            shutil.copy(emplacementDuFichier, dirpath)

            path = (os.path.expanduser(r'~\Documents'))
            with open(path + '1.bat', 'w') as filehandle:
                filehandle.write(
                    '"C:/Program Files (x86)/Arduino/hardware/tools/avr/bin/avrdude" -CC:"/Program Files (x86)/Arduino/hardware/tools/avr/etc/avrdude.conf" -v -patmega328p -carduino -P' +
                    arduino_ports[0] + ' -b115200 -D -Uflash:w:' + path + '/analoga1.ino.standard.hex:i')
            exePath = path + "1.bat"

            subprocess.call([exePath])

        if capteur == "2" :
            nomDuFicherDesValeurs = "analoga2.ino.standard.hex"
            emplacementDuFichier = os.path.join(repertoire, nomDuFicherDesValeurs)
            dirpath = (os.path.expanduser(r'~\Documents'))
            shutil.copy(emplacementDuFichier, dirpath)

            path = (os.path.expanduser(r'~\Documents'))
            with open(path + '1.bat', 'w') as filehandle:
                filehandle.write(
                    '"C:/Program Files (x86)/Arduino/hardware/tools/avr/bin/avrdude" -CC:"/Program Files (x86)/Arduino/hardware/tools/avr/etc/avrdude.conf" -v -patmega328p -carduino -P' +
                    arduino_ports[0] + ' -b115200 -D -Uflash:w:' + path + '/analoga2.ino.standard.hex:i')
            exePath = path + "1.bat"

            subprocess.call([exePath])


        if capteur == "3":
            nomDuFicherDesValeurs = "accx.ino.standard.hex"
            emplacementDuFichier = os.path.join(repertoire, nomDuFicherDesValeurs)
            dirpath = (os.path.expanduser(r'~\Documents'))
            shutil.copy(emplacementDuFichier, dirpath)

            path = (os.path.expanduser(r'~\Documents'))
            with open(path + '1.bat', 'w') as filehandle:
                filehandle.write(
                    '"C:/Program Files (x86)/Arduino/hardware/tools/avr/bin/avrdude" -CC:"/Program Files (x86)/Arduino/hardware/tools/avr/etc/avrdude.conf" -v -patmega328p -carduino -P' +
                    arduino_ports[0] + ' -b115200 -D -Uflash:w:' + path + '/accx.ino.standard.hex:i')
            exePath = path + "1.bat"

            subprocess.call([exePath])

        if capteur == "4":
            nomDuFicherDesValeurs = "photodiode.ino.standard.hex"
            emplacementDuFichier = os.path.join(repertoire, nomDuFicherDesValeurs)
            dirpath = (os.path.expanduser(r'~\Documents'))
            shutil.copy(emplacementDuFichier, dirpath)

            path = (os.path.expanduser(r'~\Documents'))
            with open(path + '1.bat', 'w') as filehandle:
                filehandle.write(
                    '"C:/Program Files (x86)/Arduino/hardware/tools/avr/bin/avrdude" -CC:"/Program Files (x86)/Arduino/hardware/tools/avr/etc/avrdude.conf" -v -patmega328p -carduino -P' +
                    arduino_ports[0] + ' -b115200 -D -Uflash:w:' + path + '/photodiode.ino.standard.hex:i')
            exePath = path + "1.bat"

            subprocess.call([exePath])

        if capteur == "5":
            nomDuFicherDesValeurs = "temperature.ino.standard.hex"
            emplacementDuFichier = os.path.join(repertoire, nomDuFicherDesValeurs)
            dirpath = (os.path.expanduser(r'~\Documents'))
            shutil.copy(emplacementDuFichier, dirpath)

            path = (os.path.expanduser(r'~\Documents'))
            with open(path + '1.bat', 'w') as filehandle:
                filehandle.write(
                    '"C:/Program Files (x86)/Arduino/hardware/tools/avr/bin/avrdude" -CC:"/Program Files (x86)/Arduino/hardware/tools/avr/etc/avrdude.conf" -v -patmega328p -carduino -P' +
                    arduino_ports[0] + ' -b115200 -D -Uflash:w:' + path + '/temperature.ino.standard.hex:i')
            exePath = path + "1.bat"

            subprocess.call([exePath])




        arduino = serial.Serial(arduino_ports[0], 9600)

    @Slot()
    def notepad(self):
        """lancement de notepad"""
        dirpath = (os.path.expanduser(r'~\Documents'))

        try:

            #exePath = "C:/Program Files (x86)/Evariste/Regressi/regressi.exe " + dirpath + '\Arduino.txt'
            exePath = "C:/Windows/system32/notepad.exe "+ dirpath + '\Arduino.txt'
            subprocess.Popen(exePath)


        except:
            print('erreur notepad')

    @Slot()
    def regressi(self):
        """lancement de notepad"""
        dirpath = (os.path.expanduser(r'~\Documents'))

        try:

            exePath = "C:/Program Files (x86)/Evariste/Regressi/regressi.exe " + dirpath + '\Arduino.txt'
            #exePath = "C:/Windows/system32/notepad.exe " + dirpath + '\Arduino.txt'
            subprocess.Popen(exePath)


        except:
            print('erreur notepad')


    @Slot()
    def flush(self):

        time.sleep(0.5)


    @Slot()
    def stop_thread(self):
        self.th.stop()

    @Slot()
    def start_thread(self):
        self.th = thread1(2)

        self.th.setTerminationEnabled(True)
        self.th.start()

    @Slot(str)
    def directoryPython(self, dir):
        """lancement de notepad"""
        dirpath = (os.path.expanduser(r'~\Documents'))
        print(dir)
        dir = dir.replace('file:///', '')
        with open('directoryPython.txt', 'w') as filehandle:
            filehandle.write(dir)

    @Slot()
    def python(self):

        repertoire = ".\Resources"
        nomDuFicherDesValeurs = "arduino.py"

        emplacementDuFichier = os.path.join(repertoire, nomDuFicherDesValeurs)
        dirpath = (os.path.expanduser(r'~\Documents'))
        shutil.copy(emplacementDuFichier, dirpath)

        try:
            fichier = open("directoryPython.txt", "r")

            dir = (fichier.read())
            exePath = dir + " " + dirpath + '\Arduino.py'
            print(exePath)
            # exePath = "C:/Windows/system32/notepad.exe " + dirpath + '\Arduino.txt'
            subprocess.Popen(exePath)


        except:
            print('erreur notepad')

    @Slot()
    def traductionFr(self):
        with open('Resources/language.txt', 'w') as filehandle:
            filehandle.write('french')

    @Slot()
    def traductionEn(self):
        with open('Resources/language.txt', 'w') as filehandle:
            filehandle.write('english')


class AcquisitionArduino(threading.Thread):

    """Thread chargé simplement d'afficher une lettre dans la console."""
    global running

    running = True

    def __init__(self, arg1, arg2,series,series2,series3, axisX):
        super(AcquisitionArduino, self).__init__()
        Thread.__init__(self)
        self.tableau = []
        self.series = series
        self.series2 = series2
        self.series3 = series3

        self.axisX = axisX
        self.arg1 = arg1
        self.arg2 = arg2

    def run(self ):
        """Code à exécuter pendant l'exécution du thread."""

        py_mainapp.ctx.setContextProperty("retour", "temps")

        try:
            arduino_ports = [
                p.device
                for p in serial.tools.list_ports.comports()
                if ('CH340') in p.description
            ]
            if not arduino_ports:
                arduino_ports = [
                    p.device
                    for p in serial.tools.list_ports.comports()
                    if ('Arduino') in p.description
                ]
            if not arduino_ports:
                raise IOError("No Arduino found")

            arduino = serial.Serial(arduino_ports[0], 9600)
            arduino.setDTR(True)

            time.sleep(3)





        except:
            print("arduino errreur")


        self.series.clear()
        self.series2.clear()
        self.series3.clear()

        global running

        running = True
        while running == True:




            """----------------------------------------------------------------------------------"""
            """         Variables           """

            resultat = []
            tableauTemps = []
            tableauDonnee1 = []
            tableauDonnee2 = []
            tableauRegressi = []

            t = 0

            """----------------------------------------------------------------------------------"""


            """Envoi du temps d'echantillonnage"""

            tempsDechantillonnage = self.arg2
            nombreDePoints = self.arg1
            arduino.flush()
            commandeArduino = tempsDechantillonnage + ',' + nombreDePoints

            """envoi sur le port serie"""

            arduino.write(commandeArduino.encode())
            arduino.flush()
            arduino.flushInput()
            time.sleep(0.2)

            """lecture des resultats"""
            global language
            if language == "french":
                py_mainapp.ctx.setContextProperty("etatacquisition", "Acquisition en cours")
            else:
                py_mainapp.ctx.setContextProperty("etatacquisition", "Acquisition in progress")



            nombreDePoints = int(self.arg1)

            for i in range(nombreDePoints):
                if running == False:
                    break
                else:
                    try:
                        donneesArduino = arduino.readline()
                        donneesArduino = donneesArduino.decode("utf-8")
                        donneesArduino = donneesArduino.replace('\r\n', '')

                        val = donneesArduino.split(',')
                        if t == 0:
                            temps0 = val[0]
                            t = 1
                        val[0] = float(val[0]) - float(temps0)

                        val[0] = float(val[0])
                        val[0] = val[0] /1000000

                        self.series.append(float(val[0]),float(val[1]))


                        if len(val)==3:

                            self.series2.append(float(val[0]),float(val[2]))

                        if len(val) == 4:
                            self.series2.append(float(val[0]), float(val[2]))
                            self.series3.append(float(val[0]),float(val[3]))




                        print(donneesArduino)
                        py_mainapp.ctx.setContextProperty("xaxismax",val[0])


                        tableauTemps.append(float(val[0]))
                        tableauDonnee1.append(float(val[1]))





                        if (len(val))==2 :

                            tableauRegressi.append(str(val[0]) + ' ' + str(val[1]))
                        if len(val)== 3 :
                            tableauRegressi.append(str(val[0]) + ' ' + str(val[1])+ ' ' + str(val[2]))
                            tableauDonnee1.append(float(val[1]))
                            tableauDonnee2.append(float(val[2]))

                        if len(val)== 4 :
                            tableauRegressi.append(str(val[0]) + ' ' + str(val[1])+ ' ' + str(val[2]) +' ' + str(val[3]))
                            tableauDonnee2.append(float(val[2]))
                            tableauDonnee1.append(float(val[1]))



                        x = max(tableauDonnee1) + 2
                        y = min(tableauDonnee1) - 2


                        try:
                            x1 = max(tableauDonnee2)+2


                            if x1>x :
                                x= x1
                            y1 = min(tableauDonnee2)-2


                            if y1 < y:
                                y = y1

                        except:
                            None

                        py_mainapp.ctx.setContextProperty("yaxismax", str(x))
                        py_mainapp.ctx.setContextProperty("yaxismin", str(y))



                        resultat.append(tableauRegressi)
                    except:
                        print('donnees erronnees')
            py_mainapp.ctx.setContextProperty("etatacquisition", "Stop")


            """Ecrire les donnees dans un fichier texte"""

            try:

                dirpath = (os.path.expanduser(r'~\Documents'))

                with open(dirpath + '\Arduino.txt', 'w') as filehandle:
                    if (len(val)) == 2:
                        filehandle.write('%s\n' % 'Time Data')
                    if len(val) == 3:
                        filehandle.write('%s\n' % 'Time Data Data1')

                    if len(val) == 4:
                        filehandle.write('%s\n' % 'Time Data Data1 Data2')

                    filehandle.write('%s\n' % 's')
                    for listitem in tableauRegressi:
                        filehandle.write('%s\n' % listitem)

            except:
                print('erreur file')



            running = False
            arduino.close()


        running = False
        py_mainapp.ctx.setContextProperty("etatacquisition", "Stop")
        arduino.close()



    def arreter(self):
        global running
        running = False
        py_mainapp.ctx.setContextProperty("etatacquisition", "Stop")



class thread1(QThread):

    def __init__(self, x):
        QThread.__init__(self)
        self.x = x

    def run(self):
        for i in range(100):
            self.x = i
            print(i)
            time.sleep(0.5)

    def stop(self):
        self.terminate()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"

    global language


    try:
        fichier = open("resources\language.txt", "r")

        language = (fichier.read())
        print(language)
        if language == "french":
            translator = QTranslator(app)
            translator.load('resources/french', os.path.dirname(__file__))
            app.installTranslator(translator)
        else:
            None
        fichier.close()
    except:
        None


    engine = QQmlApplicationEngine()
    engine.load("qml/ArduinoExao.qml")



    win = engine.rootObjects()[0]

    ctx = engine.rootContext()
    py_mainapp = MainApp(ctx,win)
    ctx.setContextProperty("py_MainApp", py_mainapp)

    # Load the qml file into the engine
    win.showMaximized()



    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
