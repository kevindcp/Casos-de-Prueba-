import unittest
from Pension import Persona


class pensionTest(unittest.TestCase):
	
	def testVaron60anos750cotizaciones(self):
		self.persona = Persona("1/1/1960",'M',750,0)
		self.assertTrue(self.persona._EsPensionado())

	def testVaron59anos750cotizacionesSinAnosInsalubres(self):
		self.persona = Persona("1/1/1961",'M',750,0)
		self.assertFalse(self.persona._EsPensionado())

	def testVaron55anos750cotizacionesCon20anosInsalubres(self):
		self.persona = Persona("1/1/1965",'M',750,20)
		self.assertTrue(self.persona._EsPensionado())

	def testVaron60anos749cotizaciones(self):	
		self.persona = Persona("1/1/1960",'M',749,0)
		self.assertFalse(self.persona._EsPensionado())

	def testMujer55anos750cotizaciones(self):
		self.persona = Persona("1/1/1965",'F',750,0)
		self.assertTrue(self.persona._EsPensionado())

	def testMujer54anos750cotizaciones(self):
		self.persona = Persona("1/1/1966",'F',750,0)
		self.assertFalse(self.persona._EsPensionado())

	def testMujer50anos750cotizacionesCon20anosInsalubre(self):
		self.persona = Persona("1/1/1965",'F',750,20)
		self.assertTrue(self.persona._EsPensionado())

	def testMujer55anos749cotizaciones(self):
		self.persona = Persona("1/1/1965",'F',749,0)
		self.assertFalse(self.persona._EsPensionado())
		
					


 
if __name__ == '__main__':
	unittest.main()

