
class Credencial:
    # codeWord = ""
    # user = ""
    # descripcion = ""
    # wordPasswd = ""
    # estatus = ""
    # sitio = ""  #url
    nivel = {"debil", "normal", "fuerte"}

    def __init__(self, codeWord, word, descrip, wordPasswd, estatus,sitio):
        self.codeWord = codeWord
        self.user  = word
        self.descripcion = descrip
        self.wordPasswd = wordPasswd
        self.estatus = estatus
        self.sitio = sitio
