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
        self._label6 = System.Windows.Forms.Label()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._button1 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 27)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Option 1"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 103)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Option 2"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 186)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "Option 3"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(284, 186)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 5
        self._label4.Text = "Option 6"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(284, 103)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 4
        self._label5.Text = "Option 5"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(284, 27)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 3
        self._label6.Text = "Option 4"
        # 
        # checkBox1
        # 
        self._checkBox1.Location = System.Drawing.Point(390, 26)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(20, 24)
        self._checkBox1.TabIndex = 6
        self._checkBox1.UseVisualStyleBackColor = True
        # 
        # checkBox2
        # 
        self._checkBox2.Location = System.Drawing.Point(390, 102)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(20, 24)
        self._checkBox2.TabIndex = 7
        self._checkBox2.UseVisualStyleBackColor = True
        # 
        # checkBox3
        # 
        self._checkBox3.Location = System.Drawing.Point(390, 185)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(20, 24)
        self._checkBox3.TabIndex = 8
        self._checkBox3.UseVisualStyleBackColor = True
        # 
        # radioButton1
        # 
        self._radioButton1.Location = System.Drawing.Point(118, 26)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(19, 24)
        self._radioButton1.TabIndex = 9
        self._radioButton1.TabStop = True
        self._radioButton1.UseVisualStyleBackColor = True
        # 
        # radioButton2
        # 
        self._radioButton2.Location = System.Drawing.Point(118, 102)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(19, 24)
        self._radioButton2.TabIndex = 10
        self._radioButton2.TabStop = True
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.Location = System.Drawing.Point(118, 184)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(19, 24)
        self._radioButton3.TabIndex = 11
        self._radioButton3.TabStop = True
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 323)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(240, 126)
        self._button1.TabIndex = 12
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(258, 323)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(215, 126)
        self._button3.TabIndex = 14
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # radioButton4
        # 
        self._radioButton4.Location = System.Drawing.Point(118, 103)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(19, 24)
        self._radioButton4.TabIndex = 15
        self._radioButton4.TabStop = True
        self._radioButton4.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(485, 461)
        self.Controls.Add(self._radioButton4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._checkBox3)
        self.Controls.Add(self._checkBox2)
        self.Controls.Add(self._checkBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Radio"
        self.ResumeLayout(False)


    def Button3Click(self, sender, e):
        Application.Exit()


    def Button1Click(self, sender, e):
        if self._radioButton1.Checked == True:
            MessageBox.Show("You selected Option 1")
        elif self._radioButton4.Checked == True:
            MessageBox.Show("You selected Option 2")
        elif self._radioButton3.Checked == True:
            MessageBox.Show("You selected Option 3")
        elif self._checkBox1.Checked == True:
            MessageBox.Show("You selected Option 4")
        elif self._checkBox2.Checked == True:
            MessageBox.Show("You selected Option 5")
        elif self._checkBox3.Checked == True:
            MessageBox.Show("You selected Option 6")
        else:
            MessageBox.Show("Select an option")