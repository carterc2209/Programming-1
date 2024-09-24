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
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(0, 359)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(259, 85)
        self._button1.TabIndex = 0
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(305, 359)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(340, 85)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(700, 359)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(258, 85)
        self._button3.TabIndex = 2
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._label1.Location = System.Drawing.Point(12, 20)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(928, 302)
        self._label1.TabIndex = 3
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.White
        self.ClientSize = System.Drawing.Size(956, 442)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "PhoneNumbers"
        self.ResumeLayout(False)

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        self._label1.Text = "911 \n 608-795-7521 \n 608-754-4096 \n 608-792-0100 \n 608-752-1744"

    def Button2Click(self, sender, e):
        self._label1.Text = ""