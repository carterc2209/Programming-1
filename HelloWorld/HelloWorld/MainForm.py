import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._Show = System.Windows.Forms.Button()
        self._Clear = System.Windows.Forms.Button()
        self._Quit = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._label1.Location = System.Drawing.Point(35, 42)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(870, 246)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # Show
        # 
        self._Show.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._Show.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._Show.Location = System.Drawing.Point(-1, 375)
        self._Show.Name = "Show"
        self._Show.Size = System.Drawing.Size(235, 66)
        self._Show.TabIndex = 1
        self._Show.Text = "Show"
        self._Show.UseVisualStyleBackColor = False
        self._Show.Click += self.Button1Click
        # 
        # Clear
        # 
        self._Clear.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._Clear.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._Clear.Location = System.Drawing.Point(316, 375)
        self._Clear.Name = "Clear"
        self._Clear.Size = System.Drawing.Size(291, 66)
        self._Clear.TabIndex = 2
        self._Clear.Text = "Clear"
        self._Clear.UseVisualStyleBackColor = False
        self._Clear.Click += self.Button2Click
        # 
        # Quit
        # 
        self._Quit.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._Quit.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._Quit.Location = System.Drawing.Point(698, 375)
        self._Quit.Name = "Quit"
        self._Quit.Size = System.Drawing.Size(257, 66)
        self._Quit.TabIndex = 3
        self._Quit.Text = "Quit"
        self._Quit.UseVisualStyleBackColor = False
        self._Quit.Click += self.QuitClick
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.White
        self.ClientSize = System.Drawing.Size(953, 440)
        self.Controls.Add(self._Quit)
        self.Controls.Add(self._Clear)
        self.Controls.Add(self._Show)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "HelloWorld"
        self.ResumeLayout(False)
    
    def Button1Click(self, sender, e):
        self._label1.Text = "Hello, World!"

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def QuitClick(self, sender, e):
        Application.Exit()