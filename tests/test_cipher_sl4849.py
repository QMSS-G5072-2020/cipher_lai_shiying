from cipher_sl4849 import cipher_sl4849

def test_cipher_single_word():
    example ='apple'
    expected ="dssoh"
    actual = cipher_sl4849.cipher(text=example, shift=3, encrypt=True)
    assert actual == expected
