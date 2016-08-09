def string_shift(input_string, shift):
	alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	output_string = []
	for char in input_string:
		if char in alphabet_list:
			index = alphabet_list.index(char)
			if index-shift < 0:
				char = alphabet_list[len(alphabet_list)+(index-shift)]
			else:
				char = alphabet_list[index-shift]
			output_string.append(char)
		else:
			output_string.append(char
	return ''.join(output_string)


def decoded_string(encoded_string, decoded_word):
	alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	encoded_list = encoded_string.split()
	comparison_list = []
	shift = 0
	for word in encoded_list:
		if len(word) == len(decoded_word):
			comparison_list.append(word)
	decoded_indices = []
	for char in decoded_word:
		decoded_indices.append(alphabet_list.index(char))
	for word in comparison_list:
		encoded_indices = []
		for char in word:
			encoded_indices.append(alphabet_list.index(char))
		for i in range(len(encoded_indices)-1):
			if (decoded_indices[i]-encoded_indices[i]) == (decoded_indices[i+1]-encoded_indices[i+1]):
				shift = abs((decoded_indices[i]-encoded_indices[i]))
	return string_shift(encoded_string, shift)

    
