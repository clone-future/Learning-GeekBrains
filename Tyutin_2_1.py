# Школьники делят n яблок на k человек, сколько яблок достанется каждому
# школьнику если считать, что неделимый остаток не достается никому?
n = int(input())
k = int(input())
apple_count = n // k
if apple_count == 1:
    apple_word = "яблоко"
elif apple_count < 5:
    apple_word = "яблока"
elif apple_count >= 5:
    apple_word = "яблок"
print("Каждому школьнику достанется %s %s" % (apple_count, apple_word))
