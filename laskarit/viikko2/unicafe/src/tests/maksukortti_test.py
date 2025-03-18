import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.maksukortti

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 15.0)

    def test_rahan_otto_kun_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_rahan_otto_kun_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahanotto_boolean(self):
        boolean = self.maksukortti.ota_rahaa(500)

        self.assertTrue(boolean)

        boolean = self.maksukortti.ota_rahaa(1500)

        self.assertFalse(boolean)

    def test_str_toimii(self):

       self.assertEqual(self.maksukortti.__str__(), "Kortilla on rahaa 10.00 euroa")