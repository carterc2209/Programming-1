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
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 12)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(242, 36)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter Purchase Price: "
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 59)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(253, 38)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter Amount Recieved: "
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 115)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(498, 38)
        self._label3.TabIndex = 2
        self._label3.Text = "Change Due: "
        self._label3.Click += self.Label3Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(608, 9)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(242, 39)
        self._label4.TabIndex = 3
        self._label4.Text = "Dollars: "
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(608, 59)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(242, 39)
        self._label5.TabIndex = 4
        self._label5.Text = "Quarters: "
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(608, 115)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(242, 39)
        self._label6.TabIndex = 5
        self._label6.Text = "Dimes: "
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(608, 167)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(242, 39)
        self._label7.TabIndex = 6
        self._label7.Text = "Nickles: "
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.White
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(608, 220)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(242, 39)
        self._label8.TabIndex = 7
        self._label8.Text = "Pennies: "
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 349)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(253, 76)
        self._button1.TabIndex = 8
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(360, 349)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(253, 76)
        self._button2.TabIndex = 9
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(706, 349)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(253, 76)
        self._button3.TabIndex = 10
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(240, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(270, 38)
        self._textBox1.TabIndex = 11
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(254, 59)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(256, 38)
        self._textBox2.TabIndex = 12
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(971, 437)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog58t"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label3Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        prc = float(self._textBox1.Text)
        rcvd = float(self._textBox2.Text) #recieved
        due = abs(prc - rcvd)
        self._label3.Text = "Change Due: " + str(due)
        dollar = due // 1
        self._label4.Text = "Dollars: " + str(dollar)
        quarter = (due - dollar) //.25
        self._label5.Text = "Quarters: " + str(quarter)
        dime = (due - dollar - (quarter * 0.25)) // 0.10
        self._label6.Text = "Dimes: " + str(dime)
        nickel = (due - dollar - (quarter * 0.25) - (dime * 0.10)) // 0.05
        self._label7.Text = "Nickles: " + str(nickel)
        penny = (due - dollar - (quarter * 0.25) - (dime * 0.10) - (nickel * 0.05)) // 0.01
        self._label8.Text = "Pennies: " + str(penny)

        
        
        
        
    def Button2Click(self, sender, e):
        self._label3.Text = "Change Due: "
        self._label4.Text = "Dollars: "
        self._label5.Text = "Quarters: "
        self._label6.Text = "Dimes: "
        self._label7.Text = "Nickles: "
        self._label8.Text = "Pennies: "
        self._textBox1.Text = ""
        self._textBox2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()
        