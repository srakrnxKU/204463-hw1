import re
import sqlite3
import sys
con = sqlite3.connect('word.db')

def word_freq():
	cursor = con.execute("SELECT TOTAL FROM word GROUP BY TOTAL ORDER BY TOTAL DESC")
	result = cursor.fetchall()
	print("freq\tword")
	for total in result:
		cursor2 = con.execute("SELECT WORD FROM word WHERE TOTAL = "+str(total[0]))
		result2 = cursor2.fetchall()
		arr_word = []
		for a in result2:
			arr_word.append(a[0])
		print("%d\t%s" % (total[0],",".join(arr_word)))

def freq_total():
	cursor = con.execute("SELECT TOTAL,COUNT(TOTAL) AS count FROM word GROUP BY TOTAL ORDER BY count DESC")
	result = cursor.fetchall()
	print("frequency\tcount")
	for all in result:
		print("%d\t%d" % (all[0],all[1]))


def main():
	if len(sys.argv) != 2:
		print("Wrong usage, exit")
		return
	mode = sys.argv[1]
	if str(mode) == "1":
		word_freq()
	elif str(mode) == "2":
		freq_total()
	else:
		print("Wrong mode selection.")

if __name__ == "__main__":
	main()
