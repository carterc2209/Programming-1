import System.Drawing
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
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 74)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(165, 38)
        self._label1.TabIndex = 0
        self._label1.Text = "Runner 1:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 127)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(165, 38)
        self._label2.TabIndex = 1
        self._label2.Text = "Runner 2:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(14, 178)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(165, 38)
        self._label3.TabIndex = 2
        self._label3.Text = "Runner 3:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(171, 9)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(150, 54)
        self._label4.TabIndex = 3
        self._label4.Text = "Name"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(356, 9)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(191, 62)
        self._label5.TabIndex = 4
        self._label5.Text = "Finishing Time    (in seconds)"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(171, 74)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(150, 38)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(171, 127)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(150, 38)
        self._textBox2.TabIndex = 6
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(171, 178)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(150, 38)
        self._textBox3.TabIndex = 7
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(356, 74)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(191, 38)
        self._textBox4.TabIndex = 8
        # 
        # textBox5
        # 
        self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.Location = System.Drawing.Point(356, 127)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(191, 38)
        self._textBox5.TabIndex = 9
        # 
        # textBox6
        # 
        self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox6.Location = System.Drawing.Point(356, 178)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(191, 38)
        self._textBox6.TabIndex = 10
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 230)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(309, 50)
        self._button1.TabIndex = 11
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(344, 230)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(309, 50)
        self._button2.TabIndex = 12
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(659, 230)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(292, 50)
        self._button3.TabIndex = 13
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(610, 21)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(341, 42)
        self._label6.TabIndex = 14
        self._label6.Text = "First:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(610, 88)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(341, 42)
        self._label7.TabIndex = 15
        self._label7.Text = "Second:"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.White
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(610, 157)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(341, 42)
        self._label8.TabIndex = 16
        self._label8.Text = "Third:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self.ClientSize = System.Drawing.Size(963, 302)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Race"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label6.Text = "First: "
        self._label7.Text = "Second: "
        self._label8.Text = "Third: "

    def Button1Click(self, sender, e):
        r1n = str(self._textBox1.Text)
        r2n = str(self._textBox2.Text)
        r3n = str(self._textBox3.Text)
        r1t = str(self._textBox4.Text)
        r2t = str(self._textBox5.Text)
        r3t = str(self._textBox6.Text)
        if r1t < r2t and r1t < r3t:
            self._label6.Text = "First: " + r1n +  "   " + r1t
            if r2t > r3t:
                self._label7.Text = "Second: " + r2n +  "   " + r2t
                self._label8.Text = "Third: " + r3n +  "   " + r3t
            elif r3t < r2t:
                self._label7.Text = "Second: " + r3n +  "   " + r3t
                self._label8.Text = "Third: " + r2n +  "   " + r2t
        elif r2t < r1t and r2t < r3t:
            self._label6.Text = "First: " + r2n +  "   " + r2t
            if r1t < r3t:
                self._label7.Text = "Second: " + r1n +  "   " + r1t
                self._label8.Text = "Third: " + r3n +  "   " + r3t
            elif r3t < r1t:
                self._label7.Text = "Second: " + r3n +  "   " + r3t
                self._label8.Text = "Third: " + r1n +  "   " + r1t
        elif r3t < r1t and r3t < r2t:
            self._label6.Text = "First: " + r3n +  "   " + r3t
            if r1t < r2t:
                self._label7.Text = "Second: " + r1n +  "   " + r1t
                self._label8.Text = "Third: " + r2n +  "   " + r2t
            elif r2t < r1t:
                self._label7.Text = "Second: " + r2n +  "   " + r2t
                self._label8.Text = "Third: " + r1n +  "   " + r1t