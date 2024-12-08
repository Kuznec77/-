
class WordsFinder:


    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open( i, encoding='utf-8') as file:
                words = []
                for line in file:
                    words += self.trim_line(line).split()
            all_words[i] = words
        return all_words
    def trim_line(self,line):
        trim_chars = [',', '.', '=', '!', '?', ';', ':', ' - ']
        line = line.lower()
        for i in trim_chars:
            line = line.replace(i, '')
        return line

    def find(self, word):
            res = {}
            for key, value in self.get_all_words().items():
                for i in range(len(value)):
                    if value[i].lower() == word.lower():
                        res[key] = i + 1
                        break
            return res

    def count(self, word):
        res = {}
        for names, words in self.get_all_words().items():
            count = words.count(word.lower())
            res[names] = count

        return res

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
# test_file.txt( It's a text for task Найти везде,Используйте его для самопроверки.Успехов в решении задачи!text text text )
