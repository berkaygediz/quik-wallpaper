using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace wannacrypt0r
{
    public partial class Main : Form
    {
        public Main()
        {
            InitializeComponent();
        }

        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        private static extern Int32 SystemParametersInfo(UInt32 action, UInt32 uParam, String vParam, UInt32 winIni);

        public void SetWallpaper(String path)
        {
            SystemParametersInfo(0x14, 0, path, 0x01 | 0x02);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SetWallpaper("");
            Application.Exit();
        }
    }
}
