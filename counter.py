from fnmatch import filter
import os

def listDir(path) :
	""" Рекрусивно обходим вложенные файлы, выдаем полный относительный путь. """
	
	for dirname, dirnames, filenames in os.walk('.') :
	
		for subdirname in dirnames :
			yield os.path.join(dirname, subdirname)
		for filename in filenames:
			yield os.path.join(dirname, filename)

def deListeze(arr) :
	""" Преобразует дерево (много вложенных списков) в список. """
	
	res = []
	
	for i in arr :
	
		if isinstance(i, list) :
			res.extend(deListeze(i))
		else :
			res.append(i)
			
	return res
	
def countLines(path) :
	""" Считаем строки в файле. """
	try :
		return len(open(path).readlines())
	except :
		return 0
		
def count(paths) :
	""" Считаем строки в файлАХ. """
	
	return sum(( countLines(p) for p in paths ))
	
if __name__ == "__main__" :

	### Статистика по файлам

	all_files = listDir(".")
		# Все файлы текущего каталога (рекурсивно обходя подпапки)
	all_files = deListeze(all_files)
	all_rst_files =  filter(all_files, "*.rst") # Все файлы для перевода
	translated = open("WHATS-TRANSLATED").read().split("\n")
	not_translated = [ x for x in all_rst_files if x not in translated ]

	print( "Всего файлов : %d" % len(all_rst_files) )
	print( "Переведено : %d" % len(translated) )
	print( "Не переведено : %d"  % len(not_translated) )
	print( "Процент переведенного (по файлам) : %d%%" %
		round(len(translated) / len(all_rst_files) * 100) )
		
	### Статистика по строкам
		
	translated_lines = count(translated)
	not_translated_lines = count(not_translated)
	all_lines = translated_lines + not_translated_lines
	
	print( "Всего строк : %d" % all_lines )
	print( "Переведено : %d" % translated_lines )
	print( "Не переведено : %d"  % not_translated_lines )
	print( "Процент переведенного (по строкам) : %d%%" %
		round(translated_lines / all_lines * 100) )
		
	
