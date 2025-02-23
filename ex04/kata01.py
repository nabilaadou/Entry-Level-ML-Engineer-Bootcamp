kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for key, value in kata.items():
	print("{p_lang} was created by {creator}".format(p_lang=key, creator=value))