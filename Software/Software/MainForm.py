﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(29, 22)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(212, 49)
        self._label1.TabIndex = 0
        self._label1.Text = "Package A: "
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(29, 77)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(212, 49)
        self._label2.TabIndex = 1
        self._label2.Text = "Package B: "
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(29, 129)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(212, 49)
        self._label3.TabIndex = 2
        self._label3.Text = "Package C: "
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(238, 22)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(475, 49)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(238, 77)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(475, 49)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(238, 129)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(475, 49)
        self._textBox3.TabIndex = 5
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(29, 193)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(684, 148)
        self._label4.TabIndex = 6
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Black
        self._button1.Location = System.Drawing.Point(29, 360)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(352, 90)
        self._button1.TabIndex = 7
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Black
        self._button2.Location = System.Drawing.Point(387, 360)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(321, 45)
        self._button2.TabIndex = 8
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Black
        self._button3.Location = System.Drawing.Point(387, 405)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(321, 45)
        self._button3.TabIndex = 9
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(725, 462)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Software"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label4.Text = ""

    def Button1Click(self, sender, e):
        A = int(self._textBox1.Text)
        if A in range(10, 19):
            A = A - (A * 0.2)
        elif A in range(20, 49):
            A = A - (A * 0.3)
        elif A in range(50, 99):
            A = A - (A * 0.4)
        elif A >= 100:
            A = A - (A * 0.5)
            
            
        B = int(self._textBox2.Text)
        if B in range(10, 19):
            B = B - (B * 0.2)
        elif B in range(20, 49):
            B = B - (B * 0.3)
        elif B in range(50, 99):
            B = B - (B * 0.4)
        elif B >= 100:
            B = B - (B * 0.5)
            
            
        C = int(self._textBox3.Text)
        if C in range(10, 19):
            C = C * 0.2
        elif C in range(20, 49):
            C = C * 0.7
        elif C in range(50, 99):
            C = C * 0.6
        elif C >= 100:
            C = C - (C * 0.5)
            
            
        self._label4.Text = "Package A: " + str(99 * A) + "\n" + "Package B: " + str(199 * B) + "\n" + "Package C: " + str(299 * C) +  "\n" + "Total: " + str((A * 99) + (B* 199) + (C * 299))