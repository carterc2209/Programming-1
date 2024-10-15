import System.Drawing
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
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 336)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(247, 84)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(329, 336)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(247, 84)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(641, 336)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(247, 84)
        self._button3.TabIndex = 2
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(533, 38)
        self._label1.TabIndex = 3
        self._label1.Text = "Enter number of copies that need to be printed."
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(522, 9)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(366, 38)
        self._textBox1.TabIndex = 4
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 92)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(876, 47)
        self._label2.TabIndex = 5
        self._label2.Text = "Price per copy:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 193)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(876, 47)
        self._label3.TabIndex = 6
        self._label3.Text = "Total Cost: "
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(900, 432)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "LP4-1"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button2Click(self, sender, e):
        self._label2.Text = "Price Per Copy: "
        self._label3.Text = "Total Price: "

    def Button1Click(self, sender, e):
        copies = int(self._textBox1.Text)
        price = 0
        ttl = 0
        if copies > 0 and copies <= 99:
            price = 0.30
        elif copies > 99 and copies <= 499:
            price = 0.28
        elif copies > 499 and copies <= 749:
            price = 0.27
        elif copies > 749 and copies <= 1000:
            price = 0.26
        elif copies > 1000:
            price = 0.25
        else:
            self._label3.Text = "Invalid amount of copies."
            return
        ttl = price * copies
        self._label2.Text = "Price Per Copy: " + str(price)
        self._label3.Text = "Total Cost: $%.2f" % ttl

    def Button3Click(self, sender, e):
        Application.Exit()