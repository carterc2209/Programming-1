﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(3, 339)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(277, 79)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(330, 339)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(277, 79)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(677, 339)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(277, 79)
        self._button3.TabIndex = 2
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(10, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(403, 29)
        self._label1.TabIndex = 3
        self._label1.Text = "Enter radius of the circle:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(290, 8)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(664, 31)
        self._textBox1.TabIndex = 4
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(7, 59)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(935, 118)
        self._label2.TabIndex = 5
        self._label2.Text = "Area:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(7, 191)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(935, 118)
        self._label3.TabIndex = 6
        self._label3.Text = "Circumference:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(952, 416)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog54C"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        pi = 3.14159
        r = float(self._textBox1.Text)
        cir = 2 * pi * r
        area = pi * r**2
        self._label2.Text = "Area: " + str(area)
        self._label3.Text = "Circumference: " + str(cir)

    def Button2Click(self, sender, e):
        self._label2.Text = ""
        self._label3.Text = ""
        self._textBox1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()