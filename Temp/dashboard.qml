import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls.Styles 1.4

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Dashboard"

    Rectangle {
        anchors.fill: parent
        color: "lightgray"

        ColumnLayout {
            spacing: 10
            anchors.centerIn: parent

            Item {
                width: 50
                height: 50
                Rectangle {
                    width: parent.width
                    height: parent.height
                    color: "blue"
                    radius: width / 2
                }
                Image {
                    anchors.centerIn: parent
                    source: "icons/humidity.png"  // Replace with your humidity icon
                    width: 30
                    height: 30
                }
            }

            Text {
                text: "Humidity"
                font.pixelSize: 16
            }

            Text {
                text: dashboard.humidity + "%"
                font.pixelSize: 16
            }

            Item {
                width: 50
                height: 50
                Rectangle {
                    width: parent.width
                    height: parent.height
                    color: "red"
                    radius: width / 2
                }
                Image {
                    anchors.centerIn: parent
                    source: "icons/temperature.png"  // Replace with your temperature icon
                    width: 30
                    height: 30
                }
            }

            Text {
                text: "Temperature"
                font.pixelSize: 16
            }

            Text {
                text: dashboard.temperature + "°C"
                font.pixelSize: 16
            }

            Item {
                width: 50
                height: 50
                Rectangle {
                    width: parent.width
                    height: parent.height
                    color: "yellow"
                    radius: width / 2
                }
                Image {
                    anchors.centerIn: parent
                    source: "icons/light.png"  // Replace with your light icon
                    width: 30
                    height: 30
                }
            }

            Text {
                text: "Light"
                font.pixelSize: 16
            }

            Text {
                text: dashboard.light + " lux"
                font.pixelSize: 16
            }

            Button {
                text: "Refresh"
                icon.source: "icons/refresh.png"  // Replace with your refresh icon
                icon.width: 20
                icon.height: 20
                onClicked: {
                    // You can add logic here to update dashboard data
                    dashboard.humidity = Math.random() * 100;
                    dashboard.temperature = Math.random() * 30;
                    dashboard.light = Math.random() * 1000;
                }

                style: ButtonStyle {
                    background: Rectangle {
                        implicitHeight: 30
                        implicitWidth: 100
                        color: control.pressed ? "lightgray" : "steelblue"
                        border.color: "darkblue"
                        radius: 15

                        gradient: Gradient {
                            GradientStop {
                                position: 0.0
                                color: control.pressed ? "lightgray" : "steelblue"
                            }
                            GradientStop {
                                position: 1.0
                                color: control.pressed ? "steelblue" : "lightgray"
                            }
                        }
                    }

                    label: Text {
                        text: control.text
                        font.pixelSize: 16
                        color: "white"
                        verticalAlignment: Text.AlignVCenter
                        horizontalAlignment: Text.AlignHCenter
                        anchors.fill: parent
                    }

                    MouseArea {
                        id: mouseArea
                        anchors.fill: parent
                        onClicked: {
                            control.clicked()
                        }

                        onPressedChanged: {
                            if (mouseArea.containsMouse) {
                                background.color = control.pressed ? "lightgray" : "skyblue"
                                background.gradient.stops[0].color = control.pressed ? "lightgray" : "skyblue"
                                background.gradient.stops[1].color = control.pressed ? "skyblue" : "lightgray"
                            } else {
                                background.color = control.pressed ? "lightgray" : "steelblue"
                                background.gradient.stops[0].color = control.pressed ? "lightgray" : "steelblue"
                                background.gradient.stops[1].color = control.pressed ? "steelblue" : "lightgray"
                            }
                        }
                    }
                }
            }
        }
    }
}
