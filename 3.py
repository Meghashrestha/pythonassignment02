# # 3. Write code that will print out the anagrams (words that use the same
# # letters) from a paragraph of text.

def para_anagram(paragraph):
     list = paragraph.split();
     list1 = []
     print(list)
     for word1 in list:
         for word2 in list:
             if word1!=word2 and (sorted(word1)==sorted(word2)):
                list1.append(word1)
     print(list1)
paragraph = "cat sat tac"
print(para_anagram(paragraph))