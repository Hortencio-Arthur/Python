import unittest
from sistema_academico import calcular_media, verificar_aprovacao

class TestSistemaAcademico(unittest.TestCase):

    def test_notas_negativas(self):
        self.assertEqual(calcular_media([-5.0, -5.0, -5.0]), -5.0)

    def test_notas_zero(self):
        self.assertEqual(calcular_media([0.0, 0.0, 0.0]), 0.0)

    def test_notas_vazias(self):
        self.assertEqual(calcular_media([]), 0.0)

    def test_verificacao_aprovado(self):
        self.assertEqual(verificar_aprovacao(8.0), 'APROVADO')

    def test_verificacao_reprovado(self):
        self.assertEqual(verificar_aprovacao(5.0), 'REPROVADO')

    def test_verificacao_media_negativa(self):
        self.assertEqual(verificar_aprovacao(-1.0), 'REPROVADO')

    def test_verificacao_minima_zero(self):
        self.assertEqual(verificar_aprovacao(0.0, 0.0), 'APROVADO' )

if __name__ == "__main__":
    unittest.main()