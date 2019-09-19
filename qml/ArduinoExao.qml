import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.1
import QtCharts 2.3
import QtQuick.Controls.Material 2.0
import QtQuick.Dialogs 1.1





ApplicationWindow {
    id: applicationWindow
    title: qsTr("ArduinoExao")

    minimumWidth: 800
    minimumHeight: 600


    font.family: "Times New Roman"
    font.pointSize: 10

    Material.accent: Material.Cyan


    menuBar: MenuBar {
        id: menuBar1
        font.pointSize: 12
        font.family: "Times New Roman"

        Menu {
            title: qsTr("&File")



            MenuItem {
                text : qsTr("Clear")
                onTriggered: py_MainApp.effacer(lineSeries, lineSeries2,lineSeries3)
            }


            MenuItem {
                text : qsTr("Quit")
                onTriggered: {
                    Qt.quit()
                }
            }


        }

        Menu {
            title: qsTr("&Data")



            MenuItem {
                text: qsTr("Send to notepad")
                onTriggered: py_MainApp.notepad()
            }
/*

            MenuItem {
                text: qsTr("Send to regressi")
                onTriggered: py_MainApp.regressi()
            }


            MenuItem {
                text: qsTr("Send to Edupython")
                onTriggered: py_MainApp.python()
            }
            MenuItem {
                text: qsTr("Save to png")
                onTriggered: {


                    //line.grabToImage(function(result) {
                    // result.saveToFile(fileDialog2.fileUrl);
                    // });

                }
            }


*/

        }
        Menu {
            title: qsTr("&Settings")

/*
            Menu {
                title: qsTr("Language")

                MenuItem {
                    text: qsTr("French")
                    icon.source: "./Images/icon_fr.jpg"
                    icon.color: "transparent"



                    onTriggered: py_MainApp.traductionFr()
                }

                MenuItem {
                    text: qsTr("English")
                    icon.source: "./Images/icon_en.jpg"
                    icon.color: "transparent"



                    onTriggered: py_MainApp.traductionEn()
                }

            }
            MenuItem {
                text: qsTr("Reset Arduino")
                onTriggered:  py_MainApp.reset()


            }




            MenuItem {
                text: qsTr("Select Python IDE")
                onTriggered:  fileDialog.open()


            }


            FileDialog {
                id: fileDialog
                title: "Please select Python IDE"

                nameFilters: [ "Executable (*.exe)" ]
                onAccepted: {

                    py_MainApp.directoryPython(fileDialog.fileUrl)

                }


            }
*/
            MenuItem {
                text: qsTr("About")
                onTriggered: messageDialog.open()

            }


        }
    }
    MessageDialog {
        id: messageDialog
        visible: false
        title: qsTr("About")
        text: "ArduinoExao
V1.0
https://sourceforge.net/projects/arduinoexao/
arduinoexao@gmail.com"
        Material.accent: Material.Cyan
        onAccepted: {

            messageDialog.close()
        }

    }


    GroupBox {
        id: groupBox1
        contentHeight: 600
        contentWidth: 800
        anchors.fill: parent
        title: qsTr("")

        Rectangle {
            id: rectangle2
            color: "#ffffff"
            anchors.bottomMargin: -12
            border.color: "#ffffff"
            anchors.topMargin: -12
            anchors.rightMargin: -12
            anchors.leftMargin: -12
            border.width: 0
            z: -2
            anchors.fill: parent
        }

        GroupBox {
            id: configArduino
            x: 0
            y: 44
            width: 384
            height: 89
            z: 2
            anchors.top: parent.top
            anchors.topMargin: 83
            title: qsTr("")

            Button {
                x: 193
                width: 167
                text: qsTr("Send to arduino")
                id: btnConfig
                anchors.top: parent.top
                anchors.topMargin: 0
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 15
                anchors.right: parent.right
                anchors.rightMargin: 0
                Layout.fillWidth: false
                Layout.fillHeight: false
                Layout.columnSpan: 2
                Material.background: "White"
                onClicked: {
                    py_MainApp.configArduino(comboBox.currentIndex)



                }
            }





            Timer {
                id: delayConfig
                interval: 16000
                running: true;
                repeat: false
                onTriggered: {
                    btnConfig.enabled = true
                    btnstart.enabled = true
                }
            }

            Rectangle {
                id: rectangle1
                color: "#d6d6d6"
                anchors.rightMargin: -12
                anchors.leftMargin: -12
                anchors.bottomMargin: -12
                anchors.topMargin: -12
                z: -1
                anchors.fill: parent
            }

            ComboBox {
                id: comboBox
                width: 176
                anchors.top: parent.top
                anchors.topMargin: 0
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 15
                anchors.left: parent.left
                anchors.leftMargin: 0
                model: ListModel {
                    id: model
                    ListElement { text: qsTr("Analog A0" )}
                    ListElement { text: qsTr("Analog A1" )}
                    ListElement { text: qsTr("Analog A2") }
                    ListElement { text: qsTr("Accelerometer") }
                    /*
                    ListElement { text: qsTr("Distance") }
                    ListElement { text: qsTr("Gyroscope") }
                    */
                    ListElement { text: qsTr("Photodiode") }

                    ListElement { text: qsTr("Temperature") }



                }


            }







        }

        GroupBox {
            id: groupBox
            x: 0
            y: -10
            width: 384
            height: 56
            title: qsTr("")

            Label {
                id: arduinoPort
                x: 8
                y: 0
                width: 84
                height: 32
                text: qsTr("Arduino Port :")
                verticalAlignment: Text.AlignVCenter
            }

            Label {
                id: portCom
                x: 116
                y: 0
                width: 102
                height: 32
                verticalAlignment: Text.AlignVCenter
            }

            Button {
                id: testArduino
                x: 245
                y: -8
                text: qsTr("Test arduino")
                Material.background: "White"
                onClicked: {

                    portCom.text = py_MainApp.testArduino()



                }
            }

            Rectangle {

                color: "#d6d6d6"
                anchors.bottomMargin: -12
                border.color: "#d6d6d6"
                anchors.topMargin: -12
                anchors.rightMargin: -12
                anchors.leftMargin: -12
                border.width: 0
                z: -2
                anchors.fill: parent
            }
        }

        GroupBox {
            id: acquisition
            x: 0
            y: 147
            width: 384
            height: 362
            z: 1
            anchors.top: parent.top
            anchors.topMargin: 178
            title: qsTr("")




            Button {
                y: 169
                width: 197
                height: 48
                text: qsTr("Start ")
                id : btnstart

                objectName: "startButton"
                z: 1
                focusPolicy: Qt.TabFocus
                anchors.left: parent.left
                anchors.leftMargin: 82
                Layout.fillWidth: false
                Layout.fillHeight: false
                Layout.columnSpan: 2
                Material.background: Material.Cyan
                onClicked: {
                    delaySwitch.start()
                    btnstart.enabled = false
                    etatAcquisition.text= "Wait..."
                    py_MainApp.update(lineSeries ,lineSeries2, lineSeries3,axisX ,nombreDePoints.text, tempsDechantillonge.text)

                }
            }
            Timer {
            id: delaySwitch
            interval: (parseInt(nombreDePoints.text) * parseInt(tempsDechantillonge.text))+7000

            onTriggered: {
                btnstart.enabled = true
                delaySwitch.stop()

            }
        }
            Label {
                x: 11
                y: 56
                width: 124
                height: 40
                text: qsTr("Sampling time (ms) :")
            }

            TextInput {
                id: nombreDePoints
                x: 160
                y: 10
                width: 200
                height: 33
                text: "120"
                topPadding: 0
                passwordCharacter: ""
                transformOrigin: Item.Center
                echoMode: TextInput.Normal
                horizontalAlignment: Text.AlignLeft
                focus: true
                Layout.fillWidth: true
                Material.background: "#FFFFFF"
                validator: IntValidator {bottom: 1; top: 999;}
                onTextEdited:
                {
                    totalResult.text= (parseInt(nombreDePoints.text)) * parseInt(tempsDechantillonge.text)/1000
                }
                Rectangle {

                    color: "#ffffff"
                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.bottomMargin:0
                    anchors.topMargin: 0
                    z: -1
                    anchors.fill: parent
                }


            }

            Label {
                x: 11
                y: 10
                width: 124
                height: 40
                text: qsTr("Number of points :")
            }

            TextInput {
                id: tempsDechantillonge
                x: 161
                y: 56
                width: 199
                height: 35
                text: "50"
                horizontalAlignment: Text.AlignLeft
                Layout.fillWidth: true

                onTextEdited:
                {
                    totalResult.text= (parseInt(nombreDePoints.text)) * parseInt(tempsDechantillonge.text)/1000

                }
                Rectangle {

                    color: "#ffffff"
                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.bottomMargin:0
                    anchors.topMargin: 0
                    z: -1
                    anchors.fill: parent
                }
            }

            Label {
                id: etatAcquisition
                x: 149
                y: 303
                width: 140
                height: 40
                text: qsTr("Stop")
            }

            Button {
                id: button
                y: 233
                width: 196
                height: 48
                text: qsTr("Stop")

                Material.background: "#EF9A9A"

                anchors.left: parent.left
                anchors.leftMargin: 83
                onClicked: {

                    delaySwitch.stop()
                    btnstart.enabled = true
                    py_MainApp.stopThread()

                }
            }

            Label {
                id: label
                x: 3
                y: 303
                width: 140
                height: 40
                text: qsTr("State of acquisition:")
            }

            Label {
                id: totalResult
                x: 160
                y: 102
                width: 188
                height: 47
                text: "6"
                verticalAlignment: Text.AlignTop

            }

            Rectangle {
                id: rectangle
                color: "#d6d6d6"
                anchors.rightMargin: -12
                anchors.leftMargin: -12
                anchors.bottomMargin: -12
                anchors.topMargin: -12
                z: -1
                anchors.fill: parent
            }

            Label {
                x: 11
                y: 102
                width: 124
                height: 40
                text: "Total (s) :"
                verticalAlignment: Text.AlignTop
            }



            ComboBox {

                x: 94
                y: 123
                width: 195
                height: 40
                visible: false

                  id: qtquickChartsThemes
                  model: [
                    'ChartThemeLight', 'ChartThemeBlueCerulean',
                    'ChartThemeDark', 'ChartThemeBrownSand',
                    'ChartThemeBlueNcs',
                    'ChartThemeBlueIcy', 'ChartThemeQt'
                  ]
            }







        }

        ChartView {
            id: line
            x: 390
            y: -19
            visible: true
            legend.visible: false
            anchors.topMargin: -10
            anchors.left: parent.left
            anchors.leftMargin: 402
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.top: parent.top
            //theme: ChartView.ChartThemeBlueCerulean
            theme: ChartView.ChartThemeBlueIcy
            //theme: ChartView[qtquickChartsThemes.currentText]



            LineSeries{
                id: lineSeries
                name: "Arduino"
                useOpenGL: true

                axisX: ValueAxis {
                    id: axisX
                    titleText: "Time (s)"
                    min: 0
                    max: 10.0
                }
                axisY: ValueAxis {
                    id: axisY
                    min: 0
                    max: 500
                }
                onPointAdded:{ axisX.max = xaxismax
                    axisY.max = yaxismax
                    axisY.min = yaxismin
                    etatAcquisition.text = etatacquisition
                }

            }
            LineSeries{
                id: lineSeries2

                useOpenGL: true
                axisX: axisX

            }
            LineSeries{
                id: lineSeries3

                useOpenGL: true
                axisX: axisX

            }




        }
    }



}




















/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
