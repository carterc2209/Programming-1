import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # radioButton1
        # 
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(33, 52)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(180, 29)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Child (12 and Under)"
        self._radioButton1.UseVisualStyleBackColor = True
        # 
        # radioButton2
        # 
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(33, 87)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(180, 29)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Student"
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(33, 122)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(180, 29)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Standard Adult"
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # radioButton4
        # 
        self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.Location = System.Drawing.Point(33, 157)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(180, 29)
        self._radioButton4.TabIndex = 3
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "Senior Citizen"
        self._radioButton4.UseVisualStyleBackColor = True
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(27, 10)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(238, 42)
        self._label1.TabIndex = 4
        self._label1.Text = "Type of Membership"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75)
        self._label2.Location = System.Drawing.Point(325, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(168, 27)
        self._label2.TabIndex = 5
        self._label2.Text = "Options"
        # 
        # checkBox1
        # 
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25)
        self._checkBox1.Location = System.Drawing.Point(325, 52)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(168, 24)
        self._checkBox1.TabIndex = 6
        self._checkBox1.Text = "Yoga"
        self._checkBox1.UseVisualStyleBackColor = True
        # 
        # checkBox2
        # 
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25)
        self._checkBox2.Location = System.Drawing.Point(325, 92)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(168, 24)
        self._checkBox2.TabIndex = 7
        self._checkBox2.Text = "Karate"
        self._checkBox2.UseVisualStyleBackColor = True
        # 
        # checkBox3
        # 
        self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25)
        self._checkBox3.Location = System.Drawing.Point(325, 127)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(168, 24)
        self._checkBox3.TabIndex = 8
        self._checkBox3.Text = "Personal Trainer"
        self._checkBox3.UseVisualStyleBackColor = True
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75)
        self._label3.Location = System.Drawing.Point(33, 207)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(238, 35)
        self._label3.TabIndex = 9
        self._label3.Text = "Membership Length"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(33, 242)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(238, 35)
        self._label4.TabIndex = 10
        self._label4.Text = "Enter # of months:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(33, 280)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(232, 29)
        self._textBox1.TabIndex = 11
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(27, 351)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(244, 95)
        self._button1.TabIndex = 12
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(340, 406)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(244, 40)
        self._button2.TabIndex = 13
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75)
        self._label5.Location = System.Drawing.Point(325, 163)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(259, 52)
        self._label5.TabIndex = 14
        self._label5.Text = "Membership Fees"
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(325, 207)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(259, 23)
        self._label6.TabIndex = 15
        self._label6.Text = "Monthly Fee:"
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(325, 249)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(259, 23)
        self._label7.TabIndex = 16
        self._label7.Text = "Total:"
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(340, 351)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(244, 40)
        self._button3.TabIndex = 17
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(596, 458)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._checkBox3)
        self.Controls.Add(self._checkBox2)
        self.Controls.Add(self._checkBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._radioButton4)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Name = "MainForm"
        self.Text = "MembershipFee"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        Yoga = 0.0
        Karate = 0.0
        PersonalTrainer = 0.0
        Discount = 0.0
        Months = int(self._textBox1.Text)
        BaseFee = 0.0
        
        if Months < 1 or Months > 24:
            MessageBox.Show("ERROR")
        
        if self._radioButton3.Checked == True:
            BaseFee = 40.0
        elif self._radioButton1.Checked == True:
            BaseFee = 20.0
        elif self._radioButton2.Checked == True:
            BaseFee = 25.0
        elif self._radioButton4.Checked == True:
            BaseFee = 30.0
        
        if self._checkBox1.Checked == True:
            Yoga = 10.0
        if self._checkBox2.Checked == True:
            Karate = 30.0
        if self._checkBox3.Checked == True:
            PersonalTrainer = 50.0
        
        if Months <= 3:
            Discount = 0
        elif Months <= 6 and Months > 4:
            Discount = 0.05
        elif Months < 9 and Months > 7:
            Discount = 0.08
        elif Months >= 10:
            Discount = 0.1
       
        
        
        
        Total = (BaseFee + Yoga + Karate + PersonalTrainer)
        TotalFee = ((BaseFee + Yoga + Karate + PersonalTrainer) - (Total * Discount)) * Months
        self._label6.Text = "Monthly Fee: " + str(TotalFee / Months)
        self._label7.Text = "Total: " + str(TotalFee)





    def Button3Click(self, sender, e):
        self._label6.Text = "Monthly Fee: " 
        self._label7.Text = "Total: "

    def Button2Click(self, sender, e):
        Application.Exit()