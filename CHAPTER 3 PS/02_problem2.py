# Write aprogram to fill in a letter template given below name and date.
# letter ='''
# Dear <|Nmae|>,
# You are selected 
# <|Date|>


letter =''' Dear <|Nmae|>,
            You are selected 
             <|Date|> '''

print(letter.replace("<|Nmae|>", "Ayush").replace("<|Date|>", "27 September 2000"))
