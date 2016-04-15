import QtQuick 1.1
import "fa-qml" as Awesome

Rectangle {
    width: 360
    height: 360
    color: "gray"

    Awesome.Loader {
        id: awesome
        source: "qrc:///fa-qml/fontawesome-webfont.ttf"
    }

    Grid {
        anchors.centerIn: parent
        spacing: 20
        columns: 3

        Awesome.Icon {
            color: "red"
            icon: awesome.fa_at
        }

        Awesome.Icon {
            icon: awesome.fa_question_circle_o
        }

        Awesome.Icon {
            icon: awesome.fa_apple
        }

        Awesome.Icon {
            icon: awesome.fa_american_sign_language_interpreting
        }

        Awesome.Icon {
            icon: awesome.fa_heart
        }

        Awesome.Icon {
            icon: awesome.fa_cc_visa
        }

        Awesome.Icon {
            icon: awesome.fa_fire
            color: "red"
        }
    }
}
