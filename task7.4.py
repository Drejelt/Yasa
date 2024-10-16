week_days =  {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
week_days_void = []

for i, day in week_days.items():
    week_days_void += [day, i]

print(week_days, "\n", week_days_void)
input ("Нажми Enter дабы завершить выполнение програмы: ")