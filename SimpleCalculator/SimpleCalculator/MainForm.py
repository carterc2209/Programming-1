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
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self._button8 = System.Windows.Forms.Button()
        self._button9 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(300, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(104, 55)
        self._button1.TabIndex = 0
        self._button1.Text = "+"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(422, 12)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(104, 55)
        self._button2.TabIndex = 1
        self._button2.Text = "-"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(532, 12)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(104, 55)
        self._button3.TabIndex = 2
        self._button3.Text = "*"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(532, 86)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(104, 55)
        self._button4.TabIndex = 5
        self._button4.Text = "//"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(422, 86)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(104, 55)
        self._button5.TabIndex = 4
        self._button5.Text = "/"
        self._button5.UseVisualStyleBackColor = True
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(300, 86)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(104, 55)
        self._button6.TabIndex = 3
        self._button6.Text = "^"
        self._button6.UseVisualStyleBackColor = True
        self._button6.Click += self.Button6Click
        # 
        # button7
        # 
        self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button7.Location = System.Drawing.Point(422, 162)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(104, 55)
        self._button7.TabIndex = 6
        self._button7.Text = "MOD"
        self._button7.UseVisualStyleBackColor = True
        self._button7.Click += self.Button7Click
        # 
        # button8
        # 
        self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button8.Location = System.Drawing.Point(12, 351)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(290, 101)
        self._button8.TabIndex = 7
        self._button8.Text = "Clear"
        self._button8.UseVisualStyleBackColor = True
        self._button8.Click += self.Button8Click
        # 
        # button9
        # 
        self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button9.Location = System.Drawing.Point(346, 351)
        self._button9.Name = "button9"
        self._button9.Size = System.Drawing.Size(290, 101)
        self._button9.TabIndex = 8
        self._button9.Text = "Exit"
        self._button9.UseVisualStyleBackColor = True
        self._button9.Click += self.Button9Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 21)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(181, 46)
        self._label1.TabIndex = 9
        self._label1.Text = "Number One: "
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 162)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(181, 47)
        self._label2.TabIndex = 10
        self._label2.Text = "Number Two: "
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 91)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(282, 50)
        self._label3.TabIndex = 11
        self._label3.Text = "Operation: "
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(181, 21)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(113, 47)
        self._textBox1.TabIndex = 12
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(189, 162)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(105, 47)
        self._textBox2.TabIndex = 13
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(648, 464)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button9)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "SimpleCalculator"
        self.ResumeLayout(False)
        self.PerformLayout()

    def Button9Click(self, sender, e):
        Application.Exit()
        

    def Button8Click(self, sender, e):
        self._label3.Text = "Operation: " 

    def Button1Click(self, sender, e):
        self._label3.Text = "Operation: + "
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        Answer = num1 + num2
        MessageBox.Show(str(Answer))

    def Button2Click(self, sender, e):
        self._label3.Text = "Operation: - "
        num1 = self._textBox1.Text
        num2 = self._textBox2.Text
        Answer = int(num1) - int(num2)
        MessageBox.Show(str(Answer))
        
    def Button3Click(self, sender, e):
        self._label3.Text = "Operation: * "
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        Answer = num1 * num2
        MessageBox.Show(str(Answer))

    def Button6Click(self, sender, e):
        self._label3.Text = "Operation: ^ "
        num1 = self._textBox1.Text
        num2 = self._textBox2.Text
        Answer = int(num1) ** int(num2)
        MessageBox.Show(str(Answer))

    def Button5Click(self, sender, e):
        self._label3.Text = "Operation: / "
        num1 = self._textBox1.Text
        num2 = self._textBox2.Text
        Answer = int(num1) / int(num2)
        MessageBox.Show(str(Answer))

    def Button4Click(self, sender, e):
        self._label3.Text = "Operation: // "
        num1 = self._textBox1.Text
        num2 = self._textBox2.Text
        Answer = int(num1) // int(num2)
        MessageBox.Show(str(Answer))

    def Button7Click(self, sender, e):
        self._label3.Text = "Operation: MOD "
        num1 = self._textBox1.Text
        num2 = self._textBox2.Text
        Answer = int(num1) % int(num2)
        MessageBox.Show(str(Answer))