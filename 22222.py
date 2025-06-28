aa = [i*3 for i in "edcba"]
f = ""
for i in aa:
    f += i
print(f)


print(len(f)%2==0)


f = f[::-1]
print(f[1:-1])


ff = "йцукенгочясмитьбывампиртоьлбдячысвмаипртоьлбдюж"
print(ff.find("п"), ff.rfind("п"))


ff = ff.replace("д", "*", 2)
print(ff)


f = "У самурая нет цели"
b = f.split()
print(b)


c = " ".join(b)
print(c)


a = bin(345)[2:]
a = a.zfill(12)
print(a)

bcd = ["Ноль", "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь", "Восемь", "Девять"]
f = "34увап65кавпрол87фывапро987капро"
for i in range(10):
    f = f.replace(str(i), bcd[i])
print(f)




# a = input()
# b = int(input())
# print(f"{a} {len(a)%b} {len(a)//b}")

cfv = ["мяч", "собака", "рука", "кулер"]
f = "вапромячшгкрсобака6гкгекулеркнлцуорука"
for i in cfv:
    f = f.replace(i, "*"*len(i))
print(f)

gl = list("еаоэяиюё")
gl1 = gl + [""]
yy = []

for i in gl:
    for b in gl1:
        for c in gl1:
            yy.append(f"к{b}{c}р{i}на")
print(yy)


