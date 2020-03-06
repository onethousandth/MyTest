/********************************************************************************
** Form generated from reading UI file 'redbluegreen.ui'
**
** Created by: Qt User Interface Compiler version 5.13.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef REDBLUEGREEN_H
#define REDBLUEGREEN_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QWidget *widget;
    QHBoxLayout *horizontalLayout;
    QGridLayout *gridLayout;
    QLabel *Red;
    QSpinBox *spinBox;
    QSlider *verticalSlider;
    QGridLayout *gridLayout_2;
    QLabel *label_2;
    QSpinBox *spinBox_2;
    QSlider *verticalSlider_2;
    QGridLayout *gridLayout_3;
    QLabel *label_3;
    QSpinBox *spinBox_3;
    QSlider *verticalSlider_3;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(462, 375);
        widget = new QWidget(Form);
        widget->setObjectName(QString::fromUtf8("widget"));
        widget->setGeometry(QRect(60, 20, 341, 321));
        horizontalLayout = new QHBoxLayout(widget);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        Red = new QLabel(widget);
        Red->setObjectName(QString::fromUtf8("Red"));
        Red->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(Red, 0, 0, 1, 1);

        spinBox = new QSpinBox(widget);
        spinBox->setObjectName(QString::fromUtf8("spinBox"));
        spinBox->setMaximum(255);

        gridLayout->addWidget(spinBox, 1, 0, 1, 1);

        verticalSlider = new QSlider(widget);
        verticalSlider->setObjectName(QString::fromUtf8("verticalSlider"));
        verticalSlider->setOrientation(Qt::Vertical);

        gridLayout->addWidget(verticalSlider, 2, 0, 1, 1);


        horizontalLayout->addLayout(gridLayout);

        gridLayout_2 = new QGridLayout();
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        label_2 = new QLabel(widget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(label_2, 0, 0, 1, 1);

        spinBox_2 = new QSpinBox(widget);
        spinBox_2->setObjectName(QString::fromUtf8("spinBox_2"));
        spinBox_2->setMaximum(255);

        gridLayout_2->addWidget(spinBox_2, 1, 0, 1, 1);

        verticalSlider_2 = new QSlider(widget);
        verticalSlider_2->setObjectName(QString::fromUtf8("verticalSlider_2"));
        verticalSlider_2->setOrientation(Qt::Vertical);

        gridLayout_2->addWidget(verticalSlider_2, 2, 0, 1, 1);


        horizontalLayout->addLayout(gridLayout_2);

        gridLayout_3 = new QGridLayout();
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        label_3 = new QLabel(widget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setAlignment(Qt::AlignCenter);

        gridLayout_3->addWidget(label_3, 0, 0, 1, 1);

        spinBox_3 = new QSpinBox(widget);
        spinBox_3->setObjectName(QString::fromUtf8("spinBox_3"));
        spinBox_3->setMaximum(255);

        gridLayout_3->addWidget(spinBox_3, 1, 0, 1, 1);

        verticalSlider_3 = new QSlider(widget);
        verticalSlider_3->setObjectName(QString::fromUtf8("verticalSlider_3"));
        verticalSlider_3->setOrientation(Qt::Vertical);

        gridLayout_3->addWidget(verticalSlider_3, 2, 0, 1, 1);


        horizontalLayout->addLayout(gridLayout_3);


        retranslateUi(Form);
        QObject::connect(verticalSlider, SIGNAL(valueChanged(int)), spinBox, SLOT(setValue(int)));
        QObject::connect(verticalSlider_2, SIGNAL(valueChanged(int)), spinBox_2, SLOT(setValue(int)));
        QObject::connect(verticalSlider_3, SIGNAL(valueChanged(int)), spinBox_3, SLOT(setValue(int)));

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QCoreApplication::translate("Form", "RedBlueHreenForm", nullptr));
        Red->setText(QCoreApplication::translate("Form", "Red", nullptr));
        label_2->setText(QCoreApplication::translate("Form", "Blue", nullptr));
        label_3->setText(QCoreApplication::translate("Form", "Green", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // REDBLUEGREEN_H
