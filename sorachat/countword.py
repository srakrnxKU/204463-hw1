import re
import sqlite3
import sys
con = sqlite3.connect('word.db')
def read_file(filename):
	print("Read file %s" % (filename))
	file = open(filename,"r")
	for line in file:
		line = line.lower()
		split_word(line)
def split_word(line):
	x = re.split("""[-.?,\s"”0-9]""",line)
	for word in x:
		if word != "":
			count_word(word)
def count_word(word2):
	word = word2.strip().replace("'","")
	cursor = con.execute("""SELECT * FROM word WHERE WORD = '"""+word+"""'""")
	result = cursor.fetchall()
	if len(result) == 0:
		con.execute("""INSERT INTO word (WORD,TOTAL) VALUES ('"""+word+"""',1)""")
	else:
		con.execute("""UPDATE word SET total = total + 1 WHERE WORD = '"""+word+"""'""")

def init_db():
	print("Create database")
	con.execute("CREATE TABLE IF NOT EXISTS word (WORD TEXT PRIMARY KEY NOT NULL, TOTAL INT)")
	con.execute("DELETE FROM word")
	con.commit()
def main():
	if len(sys.argv) != 2:
		print("Please specific input file in argument, exit.")
	init_db()
	read_file(sys.argv[1])
	con.commit()
	con.close()
	print("Finish, exit")

if __name__ == "__main__":
	main()
