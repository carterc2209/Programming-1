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
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 348)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(396, 98)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(414, 348)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(364, 50)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(414, 404)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(364, 42)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(17, 14)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(232, 40)
        self._label1.TabIndex = 3
        self._label1.Text = "Enter # of monthly sales: "
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(237, 14)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 40)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(669, 14)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 40)
        self._textBox2.TabIndex = 6
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(449, 14)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(232, 40)
        self._label2.TabIndex = 5
        self._label2.Text = "Advance pay awarded: "
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(17, 72)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(752, 65)
        self._label3.TabIndex = 7
        self._label3.Text = "Commission rate:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(17, 150)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(752, 65)
        self._label4.TabIndex = 8
        self._label4.Text = "Commission:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(17, 229)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(752, 65)
        self._label5.TabIndex = 9
        self._label5.Text = "Net pay:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(799, 458)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Commision"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label3.Text = "Commission rate: "
        self._label4.Text = "Commission: "
        self._label5.Text = "Net pay: "

    def Button1Click(self, sender, e):
        monthly = int(self._textBox1.Text)
        advance = int(self._textBox2.Text)
        comrate = 0.0
        com = 0.0
        net = 0.0
        if monthly < 10000:
            comrate = 0.05
        elif monthly >= 10000 and monthly < 15000:
            comrate = 0.10
        elif monthly >= 15000 and monthly < 18000:
            comrate = 0.12
        elif monthly >= 18000 and monthly < 22000:
            comrate = 0.14
        if monthly < 22000:
            comrate = 0.15
        com = monthly * comrate
        net = com - advance
        
        
        self._label3.Text = "Commis ion rate: " + str(round(comrate, 2))
        self._label4.Text = "Commission" + str(round(com, 2))
        self._label5.Text = "Net pay: " + str(round(net, 2))