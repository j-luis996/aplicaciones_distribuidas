import wx
class MiMarco(wx.Frame):
    """Clase frame que visualiza una imagen."""
    def __init__(self, imagen, padre=None, id=-1,
        pos=wx.DefaultPosition, titulo='Hola solo programadores'):
        """Crea una instancia de Frame y visualiza una imagen."""
        temp = imagen.ConvertToBitmap()
        tamano = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, padre, id, titulo, pos, tamano)
        self.bmp = wx.StaticBitmap(self, -1, temp)

class MiAplic(wx.App):
    """La clase aplicacion."""
    def OnInit(self):
        wx.InitAllImageHandlers()
        imagen = wx.Image('solop.jpg', wx.BITMAP_TYPE_JPEG)
        self.miMarco = MiMarco(imagen)
        self.miMarco.Show()
        self.SetTopWindow(self.miMarco)
        return True



if __name__ == '__main__':
    miAplic = MiAplic()
    miAplic.MainLoop()