import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_olemassa_ei_lounaita(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.maksukortti
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_kateinen_riittava_edullinen(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(260)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(palautus, 20)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateinen_riittava_maukas(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(420)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
        self.assertEqual(palautus, 20)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateinen_ei_riittavasti(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(palautus, 200)

        palautus = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(palautus, 200)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_riittava_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

        boolean = self.maksukortti.ota_rahaa(500)
        self.assertTrue(boolean)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortti_riittava_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

        boolean = self.maksukortti.ota_rahaa(500)
        self.assertTrue(boolean)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortti_ei_riittavasti(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo_euroina(), 2.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

        boolean = self.maksukortti.ota_rahaa(1500)
        self.assertFalse(boolean)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortin_lataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1010.0)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_kortin_lataus_negatiivisella_arvolla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
