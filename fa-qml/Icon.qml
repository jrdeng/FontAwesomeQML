import QtQuick 1.1

Text {
    property string icon: ""
    property int size: 48

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter
    font.family: awesome.name

    color: "white"
    text: icon
    font.pointSize: size
}
