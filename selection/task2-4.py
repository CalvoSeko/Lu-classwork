attendance=int(input("attendance rate? "))
exam=int(input("exam? "))
grade=""
if attendance<90:
    grade="fail"
#endif
elif exam>90:
    grade="A"
#endif
elif exam<=90 and exam>80:
    grade="B"
#endif
else:
    grade="fail"
#endelse