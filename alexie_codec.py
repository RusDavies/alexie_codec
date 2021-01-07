#!/usr/bin/env python3

import sys

class alexie_codec:
    
    _pad = None
    _reverse_pad = None 
    
    def __init__(self, pad = None):
        if pad != None:
            self._pad = pad 
        else: 
            self._pad = {} 
   
        # Build the reverse pad 
        self._reverse_pad = {} 
        for key, value in self._pad.items():
            self._reverse_pad[value]=key       
    
    def codec(self, pad, text): 
        result = "" 
        for c in str(text):  
            if c in pad:
                tmp = pad[c]
            else:
                tmp = c
              
            result = result + tmp 
        return result  
    def debug(self):
        print("pad: " + str(self._pad))
        print("\nrpad: " + str(self._reverse_pad))

    def decode(self, text):
        return self.codec(self._reverse_pad, text)
    
    def encode(self, text):
        return self.codec(self._pad, text)


if __name__ == '__main__':
    pad = { 'a': 'u', 'b': 'v', 'c': 'w', 'd': 'x', 'e': 'y', 'f': 'z', 'g': 'a',
            'h': 'b', 'i': 'c', 'j': 'd', 'k': 'e', 'l': 'f', 'm': 'g', 'n': 'h',
            'o': 'i', 'p': 'j', 'q': 'k', 'r': 'l', 's': 'm', 't': 'n', 'u': 'o',
            'v': 'p', 'w': 'q', 'x': 'r', 'y': 's', 'z': 't',
            'A': 'U', 'B': 'V', 'C': 'W', 'D': 'X', 'E': 'Y', 'F': 'Z', 'G': 'A',
            'H': 'B', 'I': 'C', 'J': 'D', 'K': 'E', 'L': 'F', 'M': 'G', 'N': 'H', 
            'O': 'I', 'P': 'J', 'Q': 'K', 'R': 'L', 'S': 'M', 'T': 'N', 'U': 'O', 
            'V': 'P', 'W': 'Q', 'X': 'R', 'Y': 'S', 'Z': 'T'} 
    codex = alexie_codec(pad)   
    
    result = "" 
    if str(sys.argv[1]) == "encode":
        result = codex.encode( sys.argv[2] )
        print("encoded text is: " + result)         
    elif str(sys.argv[1]) == "decode":
        result = codex.decode( sys.argv[2] )
        print("decoded text is: " + result)     
    else:
        print("ERROR: '" + sys.argv[0] + "' is not neither 'encode' nor 'decode'")    
        