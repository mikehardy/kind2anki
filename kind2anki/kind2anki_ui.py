# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kind2anki_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_kind2ankiDialog(object):
    def setupUi(self, kind2ankiDialog):
        kind2ankiDialog.setObjectName("kind2ankiDialog")
        kind2ankiDialog.resize(376, 199)
        self.vboxlayout = QtWidgets.QVBoxLayout(kind2ankiDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox = QtWidgets.QGroupBox(kind2ankiDialog)
        self.groupBox.setObjectName("groupBox")
        self.toplayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.toplayout.setObjectName("toplayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.deckArea = QtWidgets.QWidget(self.groupBox)
        self.deckArea.setObjectName("deckArea")
        self.gridLayout_2.addWidget(self.deckArea, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.toplayout.addLayout(self.gridLayout_2)
        self.importMode = QtWidgets.QComboBox(self.groupBox)
        self.importMode.setObjectName("importMode")
        self.importMode.addItem("")
        self.importMode.addItem("")
        self.importMode.addItem("")
        self.toplayout.addWidget(self.importMode)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.includeUsage = QtWidgets.QCheckBox(self.groupBox)
        self.includeUsage.setObjectName("includeUsage")
        self.gridLayout.addWidget(self.includeUsage, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(169, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.importDays = QtWidgets.QSpinBox(self.groupBox)
        self.importDays.setMinimum(1)
        self.importDays.setMaximum(1000)
        self.importDays.setProperty("value", 10)
        self.importDays.setObjectName("importDays")
        self.gridLayout.addWidget(self.importDays, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.languageSelect = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.languageSelect.sizePolicy().hasHeightForWidth())
        self.languageSelect.setSizePolicy(sizePolicy)
        self.languageSelect.setToolTipDuration(-6)
        self.languageSelect.setEditable(True)
        self.languageSelect.setObjectName("languageSelect")
        self.languageSelect.addItem("")
        self.languageSelect.addItem("")
        self.languageSelect.addItem("")
        self.languageSelect.addItem("")
        self.languageSelect.addItem("")
        self.languageSelect.addItem("")
        self.gridLayout.addWidget(self.languageSelect, 1, 1, 1, 2)
        self.doTranslate = QtWidgets.QCheckBox(self.groupBox)
        self.doTranslate.setChecked(True)
        self.doTranslate.setObjectName("doTranslate")
        self.gridLayout.addWidget(self.doTranslate, 0, 1, 1, 2)
        self.toplayout.addLayout(self.gridLayout)
        self.vboxlayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(kind2ankiDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Help)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(kind2ankiDialog)
        self.languageSelect.setCurrentIndex(0)
        self.buttonBox.accepted.connect(kind2ankiDialog.accept)
        self.buttonBox.rejected.connect(kind2ankiDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(kind2ankiDialog)

    def retranslateUi(self, kind2ankiDialog):
        _translate = QtCore.QCoreApplication.translate
        kind2ankiDialog.setWindowTitle(_translate("kind2ankiDialog", "Import"))
        self.groupBox.setTitle(_translate("kind2ankiDialog", "Kind2anki options"))
        self.label_2.setText(_translate("kind2ankiDialog", "Deck"))
        self.importMode.setItemText(0, _translate("kind2ankiDialog", "Update existing notes when first field matches"))
        self.importMode.setItemText(1, _translate("kind2ankiDialog", "Ignore lines where first field matches existing note"))
        self.importMode.setItemText(2, _translate("kind2ankiDialog", "Import even if existing note has same first field"))
        self.label.setText(_translate("kind2ankiDialog", "Language"))
        self.includeUsage.setText(_translate("kind2ankiDialog", "Include usage examle"))
        self.label_3.setText(_translate("kind2ankiDialog", "Import words not older than"))
        self.label_4.setText(_translate("kind2ankiDialog", "days"))
        self.languageSelect.setCurrentText(_translate("kind2ankiDialog", "pl"))
        self.languageSelect.setItemText(0, _translate("kind2ankiDialog", "pl"))
        self.languageSelect.setItemText(1, _translate("kind2ankiDialog", "de"))
        self.languageSelect.setItemText(2, _translate("kind2ankiDialog", "lt"))
        self.languageSelect.setItemText(3, _translate("kind2ankiDialog", "pt"))
        self.languageSelect.setItemText(4, _translate("kind2ankiDialog", "en"))
        self.languageSelect.setItemText(5, _translate("kind2ankiDialog", "es"))
        self.doTranslate.setText(_translate("kind2ankiDialog", "Translate words"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kind2ankiDialog = QtWidgets.QDialog()
    ui = Ui_kind2ankiDialog()
    ui.setupUi(kind2ankiDialog)
    kind2ankiDialog.show()
    sys.exit(app.exec_())

