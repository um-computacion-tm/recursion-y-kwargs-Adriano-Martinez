import unittest

def buscar_datos(*args, **kwargs):
    args_set = set(args)
    for persona, info in database.items():
        valores_persona = set(info.values())
        if valores_persona <= args_set:
            return persona
    return None
       
database = {
     "persona1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso"
    },
    "persona2": {
        "primer_nombre": "Elio",
        "primer_apellido": "Anzi"
    },
    "persona3": {
        "primer_nombre": "Lucca",
        "primer_apellido": "Ciro",
        "segundo_apellido": "Goria"
    },
    "persona4": {
        "primer_nombre": "Adriano",
        "segundo_nombre": "Salvador",
        "primer_apellido": "Martinez",
        "segundo_apellido": "Barbuzza"
    },
    "persona5": {
        "primer_nombre": "Damian",
        "segundo_nombre": "Emiliano",
        "primer_apellido": "Martinez"
    }  
}      


class TestBuscarDatos(unittest.TestCase):
    def test_buscar_datos_persona1(self):
        result = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(result, "persona1")

    def test_buscar_datos_persona2(self):
        result = buscar_datos("Elio", "Anzi", **database)
        self.assertEqual(result, "persona2")
        
    def test_buscar_datos_persona3(self):
       result = buscar_datos("Lucca", "Ciro", "Goria", **database)
       self.assertEqual(result, "persona3") 
       
    def test_buscar_datos_persona4(self):
       result = buscar_datos("Adriano", "Salvador", "Martinez", "Barbuzza", **database)
       self.assertEqual(result, "persona4") 
       
    def test_buscar_datos_persona5(self):
       result = buscar_datos("Damian", "Emiliano", "Martinez", **database)
       self.assertEqual(result, "persona5")


if __name__ == '__main__':
 unittest.main()
       