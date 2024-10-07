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
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(21, 14)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(218, 34)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter Number (1-13):"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(21, 52)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(218, 34)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter Number (2-20):"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(21, 104)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(403, 35)
        self._label3.TabIndex = 2
        self._label3.Text = "Sum: "
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(231, 14)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(716, 35)
        self._textBox1.TabIndex = 10
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(231, 51)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(716, 35)
        self._textBox2.TabIndex = 11
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(21, 167)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(403, 35)
        self._label4.TabIndex = 12
        self._label4.Text = "Difference: "
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(21, 236)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(403, 35)
        self._label5.TabIndex = 13
        self._label5.Text = "Product:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(21, 298)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(926, 35)
        self._label6.TabIndex = 14
        self._label6.Text = "Average: "
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(479, 104)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(468, 35)
        self._label7.TabIndex = 15
        self._label7.Text = "Absolute Value: "
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.White
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(479, 167)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(468, 35)
        self._label8.TabIndex = 16
        self._label8.Text = "Maximum: "
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.White
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(479, 236)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(468, 35)
        self._label9.TabIndex = 17
        self._label9.Text = "Minimum: "
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(21, 370)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(192, 47)
        self._button1.TabIndex = 18
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(326, 370)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(253, 47)
        self._button2.TabIndex = 19
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(733, 370)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(214, 47)
        self._button3.TabIndex = 20
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(959, 429)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog88a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        Sum = num1 + num2
        Dif = num1 - num2
        Pro = num1 * num2
        Avg = (num1 + num2) / 2
        Abs = abs(num1 - num2)
        Max = 0
        Min = 0
        if num1 >= num2:
            Max = num1
        else:
            Max = num2
        
        if max == num1: # if Max has the same value of num1 (==)
            Min = num2
        else:
            Min = num1
        self._label3.Text = "Sum: " + str(Sum)
        self._label4.Text = "Difference: " + str(Dif)
        self._label5.Text = "Product: " + str(Pro)
        self._label6.Text = "Average: " + str(Avg)
        self._label7.Text = "Absolute Value: " + str(Abs)
        self._label8.Text = "Maximum: " + str(Max)
        self._label9.Text = "Minimum: " + str(Min)

    def Button2Click(self, sender, e):
        self._label3.Text = "Sum: "
        self._label4.Text = "Difference: "
        self._label5.Text = "Product: "
        self._label6.Text = "Average: "
        self._label7.Text = "Absolute Value: "
        self._label8.Text = "Maximum: "
        self._label9.Text = "Minimum: "
        self._textBox2.Text = ""
        self._textBox1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()