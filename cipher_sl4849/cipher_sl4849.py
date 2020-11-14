def cipher(text, shift, encrypt=True):
    """
    Encrypt or Decrypt a string based on Caesar cipher.Each letter is replaced by a letter some fixed number of position down the alphabet.

    Parameters
    ----------
    text : string
         A string you wish to encrypt or decrypt.
    shift : integer
          A integer that you wish to change the position of your original text.
          if the integer is positive, each letter in text will be replaced by the letter that this integer after this letter. 
          if the integer is negative, each letter in text will be replaced by the letter that this integer before this letter.
    encrypt : bool
            A boolean that decides the function to encrypt(True) or decrypt(False) the text.

    Returns
    -------
    String
        The new encrypted or decrypted string.

    Examples
    --------
    >>> from cipher_sl4849 import cipher_sl4849
    >>> cipher_sl4849.cipher(text="apple", shift=3, encrypt=True)
        'dssoh'
    >>> cipher_sl4849.cipher(text="apple", shift=3, encrypt=False)
        'Xmmib'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        #if it is a symbol keep it unchanged
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            # just return the new index
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
