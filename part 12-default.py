def define_gender(sex="unknown"):
    if sex is 'm':
        sex='male'
    elif sex is 'f':
        sex='female'
    print(sex)


define_gender('m')
define_gender('f')
define_gender()