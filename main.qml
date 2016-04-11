import QtQuick 1.1
import "fa-qml" as Awesome

Rectangle {
    width: 360
    height: 360

    Awesome.Loader {
        id: awesome
        source: "qrc:///fa-qml/fontawesome-webfont.ttf"
    }

    Awesome.Icon {
        anchors.centerIn: parent

        color: "red"
        size: 48
        icon: awesome.fa_at
    }
}
