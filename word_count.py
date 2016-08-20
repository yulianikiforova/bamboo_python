def word_count(word_list, columns, rows):
	word_count = 0
	word_iterator = 0
	row_iterator = 0
	while row_iterator < rows:
		remaning_columns = columns
		while (remaning_columns > 0) and (len(word_list[word_iterator]) <= remaning_columns):
			word_count += 1
			remaning_columns = remaning_columns - len(word_list[word_iterator]) - 1
			word_iterator += 1
			if word_iterator >= len(word_list):
				word_iterator = 0
		if len(word_list[word_iterator]) > remaning_columns:
				row_iterator += 1
	return word_count
