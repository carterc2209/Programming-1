import math
import System.Drawing
import System.Windows.Forms

from math import *
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
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(7, 7)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(265, 65)
        self._label1.TabIndex = 0
        self._label1.Text = "A"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(325, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(265, 65)
        self._label2.TabIndex = 1
        self._label2.Text = "B"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(661, 9)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(265, 65)
        self._label3.TabIndex = 2
        self._label3.Text = "C"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(7, 73)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(265, 44)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(325, 73)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(265, 44)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(661, 73)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(265, 44)
        self._textBox3.TabIndex = 5
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(11, 138)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(903, 190)
        self._label4.TabIndex = 6
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Location = System.Drawing.Point(12, 352)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(260, 68)
        self._button1.TabIndex = 7
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Location = System.Drawing.Point(325, 352)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(265, 68)
        self._button2.TabIndex = 8
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Location = System.Drawing.Point(661, 352)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(253, 68)
        self._button3.TabIndex = 9
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(938, 432)
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
        self.Text = "Prog58B"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        A = float(self._textBox1.Text)
        B = float(self._textBox2.Text)
        C = float(self._textBox3.Text)
        Plus = (-B + sqrt(B ** 2 - (4 * A * C))) / 2 * A
        Min = (-B - sqrt(B ** 2 - (4 * A * C))) / 2 * A
        self._label4.Text = "Answer: " + (str(Plus) + str(Min))

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label4.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()