import sqlite3
connection = sqlite3.connect("D:\database_new_2\gcoos_data_v3.sqlite")
connection2 = sqlite3.connect("D:\database_new_2\gcoos_data_v2.sqlite")
connection3 = sqlite3.connect("D:\database_new_2\gcoos_data_v1.sqlite")
connection4 = sqlite3.connect("D:\database_new_2/ntl_gcoos_20221111.sqlite")
connection5 = sqlite3.connect("D:\database_new_2/ntl_gcoos_2021.sqlite")
connection6 = sqlite3.connect("D:\database_new_2/ntl_gcoos_2020.sqlite")

crsr = connection.cursor()
crsr2 = connection2.cursor()
crsr3 = connection3.cursor()
crsr4 = connection4.cursor()
crsr5 = connection5.cursor()
crsr6 = connection6.cursor()
sensortypeId = [1,2,3,4,5,6,8,9,10,14,15,17,24]
b,g=[],[]
l,q=0,0
z=0
for i in sensortypeId:
    crsr.execute('''SELECT rowId from sensor where (lastObsDate = "" or lastObsDate = NULL) and sensorTypeId ==?''',(i,))
    ans = crsr.fetchall()
    rowId_missing = []
    q=0
    for k in ans:
        rowId_missing.insert(q,k[0])
        q=q+1
    crsr.execute('''SELECT rowId from sensor where (firstObsDate = "" or firstObsDate = NULL) and sensorTypeId ==?''',(i,))
    ans_first = crsr.fetchall()
    rowId_missing_first = []
    q_first=0
    for k in ans_first:
        rowId_missing_first.insert(q,k[0])
        q_first = q_first+1

    if i in (1,2,4,6,8,9,10,14,17):
        crsr.execute('''select typeName from sensorType where rowId = ?''',(i,))
        sensor_name_1= crsr.fetchall()
        sensor_name_2 = sensor_name_1[0][0]
        # print(sensor_name_2)
    elif i == 5:
        sensor_name_2 = 'oceanCurrents'
        # print(sensor_name_2)
    elif i == 3:
        sensor_name_2 = 'wave'
        # print(sensor_name_2)
    elif i == 15:
        sensor_name_2 = 'relhumidity'
        # print(sensor_name_2)
    elif i == 24:
        sensor_name_2 = 'dewPoint'
        # print(sensor_name_2)
    k,m,n,o,p,k1,m1,n1,o1,p1,q1=0,0,0,0,0,0,0,0,0,0,0
    a,c,d,e,f,a1,b1,c1,d1,e1,f1=[],[],[],[],[],[],[],[],[],[],[]
    for j in rowId_missing:
        crsr.execute("select sensorId, max(observationDate) from '" + sensor_name_2 + "' where sensorId ==?",(j,))
        ans2 = (crsr.fetchall())
        if ans2[0][0] == None:
            a.insert(k,j)
            k=k+1
        else:
            b.insert(l,[j,ans2[0][1]])
            l=l+1

    for j in a:
        crsr4.execute("select sensorId, max(observationDate) from '" + sensor_name_2 + "' where sensorId ==?",(j,))
        ans3_ntl = (crsr4.fetchall())
        if ans3_ntl[0][0] == None:
            a1.insert(k1,j)
            k1=k1+1
        else:
            b.insert(l,[j,ans3_ntl[0][1]])
            l=l+1

    for j in a1:
        crsr5.execute("select sensorId, max(observationDate) from '" + sensor_name_2 + "' where sensorId ==?",(j,))
        ans4_ntl = (crsr5.fetchall())
        if ans4_ntl[0][0] == None:
            b1.insert(m1,j)
            m1=m1+1
        else:
            b.insert(l,[j,ans4_ntl[0][1]])
            l=l+1

    for j in b1:
        crsr6.execute("select sensorId, max(observationDate) from '" + sensor_name_2 + "' where sensorId ==?",(j,))
        ans5_ntl = (crsr6.fetchall())
        if ans5_ntl[0][0] == None:
            c1.insert(n1,j)
            n1=n1+1
        else:
            b.insert(l,[j,ans5_ntl[0][1]])
            l=l+1

    for j in c1:
        crsr2.execute("select sensorId, max(observationDate) from '" + sensor_name_2 + "' where sensorId ==?",(j,))
        ans3 = (crsr2.fetchall())
        if ans3[0][0] == None:
            c.insert(m,j)
            m=m+1
        else:
            b.insert(l,[j,ans3[0][1]])
            l=l+1
    for j in c:
        crsr3.execute("select sensorId, max(observationDate) from '" + sensor_name_2 + "' where sensorId ==?",(j,))
        ans4 = (crsr3.fetchall())
        if ans4[0][0] == None:
            b.insert(l,[j,''])
            l=l+1
        else:
            b.insert(l,[j,ans4[0][1]])
            l=l+1



    for z in rowId_missing_first:
        crsr3.execute("select sensorId, min(observationDate) from '" + sensor_name_2 + "' where sensorId ==?",(z,))
        ans2_first = (crsr3.fetchall())
        if ans2_first[0][0] == None:
            d.insert(n,z)
            n=n+1
        else:
            g.insert(q,[z,ans2_first[0][1]])
            q=q+1

    for z in d:
        crsr2.execute("select sensorId, min(observationDate) from '" + sensor_name_2 + "' where sensorId ==?",(z,))
        ans3_first = (crsr2.fetchall())
        if ans3_first[0][0] == None:
            e.insert(o,z)
            o=o+1
        else:
            g.insert(q,[z,ans3_first[0][1]])
            q=q+1

    for z in e:
        crsr6.execute("select sensorId, min(observationDate) from '" + sensor_name_2 + "' where sensorId ==?",(z,))
        ans3_first_ntl = (crsr6.fetchall())
        if ans3_first_ntl[0][0] == None:
            d1.insert(o1,z)
            o1=o1+1
        else:
            g.insert(q,[z,ans3_first_ntl[0][1]])
            q=q+1

    for z in d1:
        crsr5.execute("select sensorId, min(observationDate) from '" + sensor_name_2 + "' where sensorId ==?",(z,))
        ans4_first_ntl = (crsr5.fetchall())
        if ans4_first_ntl[0][0] == None:
            e1.insert(p1,z)
            p1=p1+1
        else:
            g.insert(q,[z,ans4_first_ntl[0][1]])
            q=q+1

    for z in e1:
        crsr4.execute("select sensorId, min(observationDate) from '" + sensor_name_2 + "' where sensorId ==?",(z,))
        ans5_first_ntl = (crsr4.fetchall())
        if ans5_first_ntl[0][0] == None:
            f1.insert(q1,z)
            q1=q1+1
        else:
            g.insert(q,[z,ans5_first_ntl[0][1]])
            q=q+1


    for z in f1:
        crsr.execute("select sensorId, min(observationDate) from '" + sensor_name_2 + "' where sensorId ==?",(z,))
        ans4_first = (crsr.fetchall())
        if ans4_first[0][0] == None:
            g.insert(q,[z,''])
            q=q+1
        else:
            g.insert(q,[z,ans4_first[0][1]])
            q=q+1
h=0
for i in range(len(b)):
    # print(b[i])
    h=h+1
print(h)
r=0
for i in range(len(g)):
    # print(g[i])
    r=r+1
print(r)
v=[]
s=0
for i in range(len(b)):
    for j in range(len(g)):
        if b[i][0] == g[j][0]:
            v.insert(s,[b[i][0],b[i][1],g[j][1]])
            s=s+1

# y=0
# for i in range(len(v)):
#     print("UPDATE sensor SET firstObsDate = '"+str(v[i][2])+"' AND lastObsDate = '"+str(v[i][1])+"' WHERE rowId ="+str(v[i][0]))

for i in range(len(g)):
    for j in (373,374,410,644,650,651,927,1864,2637,2977,2983,2999,3004,3014,3285,3321,3468,3469,3489,3490,3491):
        if g[i][0] == j:
            print("update sensor set firstObsDate = '"+g[i][1]+"' where rowId ="+str(g[i][0]))    


    



connection.close()
connection2.close()
connection3.close()






    
