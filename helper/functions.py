import pandas as pd


def report_DataFrame(report):

    class_report_RF = report
    new_report = list()

    a = class_report_RF.split("\n")

    del a[1]; del a[3]; del a[4] # deleting unwanted whitespaces

    for i in range(0, len(a)):
        a[i] = a[i].strip()

    # fix first line
    tmp = a[0].split(' ')
    del tmp[5]; del tmp[1]; del tmp[2]; del tmp[1]; del tmp[3]; del tmp[3] # deleting unwanted whitespaces

    for i in range(0, len(tmp)):
        new_report.append(tmp[i])


    # fix second line
    tmp = a[1].split('    ')
    for i in range(0, len(tmp)):
        tmp[i] = tmp[i].strip()

    for i in range(0, len(tmp)):
        new_report.append(tmp[i])

    # fix third line
    tmp = a[2].split('    ')
    for i in range(0, len(tmp)):
        tmp[i] = tmp[i].strip()

    for i in range(0, len(tmp)):
        new_report.append(tmp[i])

    # fix fourth line
    tmp = a[3].split('    ')
    for i in range(0, len(tmp)):
        tmp[i] = tmp[i].strip()

    for i in range(0, len(tmp)):
        new_report.append(tmp[i])

    # convert string values to float
    for i in range(0, len(new_report)):
        try:
            new_report[i] = float(new_report[i])
        except:
            continue

    # creating the dataFrame
    df_report = pd.DataFrame(columns=new_report[:4])

    df_report.loc[0] = new_report[5:9]
    df_report.loc[1] = new_report[10:14]

    return df_report
