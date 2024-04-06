grade_full = ['A+','A0','B+','B0','C+','C0','D+','D0','F','P']
grade_score = ['4.5','4.0','3.5','3.0','2.5','2.0','1.5','1.0','0.0']
hap = 0
hak_hap = 0
for i in range(20):
    a = 0
    name,hak,grade = input().split()
    hak = float(hak)
    a = grade_full.index(grade)
    if a == 9:
        continue
    hap += hak * float(grade_score[a])
    hak_hap += hak
print(hap/hak_hap)