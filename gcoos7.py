import sqlite3
connection = sqlite3.connect("D:\database_new\gcoos_data_v3.sqlite")
crsr = connection.cursor()
# crsr.execute("select s.rowid, 'ioos:sensor:'||o.sname||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid=p.organizationId WHERE o.sname<>'ADCP' AND o.sname <> 'TABS' AND o.sname<>'NDBC' AND o.sname <> 'COAPS' AND o.sname <> 'TCOON' AND o.sname<>'SCCF RECON' AND o.sname<>'NOS' AND o.sname<>'NERRS' AND SUBSTR(p.name, 1, 2) <> '42'  AND SUBSTR(p.name, -2) <> 'F1' AND SUBSTR(p.name, -2) <> 'A1' AND SUBSTR(p.name, -2) <> 'L1'")
# crsr.execute("select s.rowid, 'ioos:sensor:'||'wmo:'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid=p.organizationId WHERE o.sname<>'ADCP' AND o.sname<>'SCCF RECON' AND o.sname<>'NDBC' and o.sname<>'NOS' AND o.sname<>'NERRS' AND SUBSTR(p.name, 1, 2) == '42'")
# crsr.execute("select s.rowid, 'ioos:sensor:NOAA.'||o.sname||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid = p.organizationId where o.sname == 'NERRS'")
# crsr.execute("select s.rowid, 'ioos:sensor:'||SUBSTR(o.sname,1,4)||'_'||SUBSTR(o.sname,6)||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid = p.organizationId where o.sname = 'SCCF RECON'")
# crsr.execute("select s.rowid, 'ioos:sensor:'||'wmo:'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid = p.organizationId where o.sname == 'ADCP' AND SUBSTR(p.name, 1, 2) ==  '42'")
# crsr.execute("select s.rowid, 'ioos:sensor:NOAA.NDBC'||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid = p.organizationId where o.sname == 'ADCP' AND SUBSTR(p.name, 1, 2) <> '42'")
# crsr.execute("select s.rowid, 'ioos:sensor:'||'wmo:'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid = p.organizationId where o.sname == 'NDBC' AND SUBSTR(p.name, 1, 2) == '42'")
# crsr.execute("select s.rowid, 'ioos:sensor:NOAA.'||o.sname||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid=p.organizationId WHERE o.sname == 'NDBC' AND SUBSTR(p.name, 1, 2) <> '42'")
# crsr.execute("select s.rowid, 'ioos:sensor:NOAA.'||o.sname||'.CO-OPS'||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid=p.organizationId WHERE o.sname == 'NOS' AND SUBSTR(p.name, 1, 2) = '87'")
# crsr.execute("select s.rowid, 'ioos:sensor:NOAA.'||o.sname||'.CO-OPS'||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid=p.organizationId WHERE o.sname == 'NOS' AND SUBSTR(p.name, 1, 2) <> '87'")
# crsr.execute("select s.rowid, 'ioos:sensor:'||o.sname||':'||substr(p.name,1,4)||'_'||substr(p.name,6)||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid=p.organizationId WHERE o.sname = 'TABS' AND SUBSTR(p.name, 1, 2) <> '42'")
# crsr.execute("select s.rowid, 'ioos:sensor:'||o.sname||':'||SUBSTR(p.name,7)||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid=p.organizationId WHERE o.sname = 'COAPS' ")
crsr.execute("select s.rowid, 'ioos:sensor:'||o.sname||':'||SUBSTR(p.name,1,3)||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid=p.organizationId WHERE o.sname<>'ADCP' AND o.sname <> 'TABS' AND o.sname<>'NDBC' AND o.sname <> 'COAPS' AND o.sname <> 'TCOON' AND o.sname<>'SCCF RECON' AND o.sname<>'NOS' AND o.sname<>'NERRS' AND SUBSTR(p.name, 1, 2) <> '42'  AND (SUBSTR(p.name, -2) = 'F1' OR SUBSTR(p.name, -2) = 'A1' OR SUBSTR(p.name, -2) = 'L1') ")
# crsr.execute("select s.rowid, 'ioos:sensor:'||o.sname||':DNR_TAMUCC.999.'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid=p.organizationId WHERE o.sname = 'TCOON' and SUBSTR(p.name, -2) <> 'T2' ")
# crsr.execute("select s.rowid, 'ioos:sensor:'||o.sname||':DNR_TAMUCC.999.'||SUBSTR(p.name,1,3)||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber as new_localId, s.localId from sensor s JOIN sensorType st on s.sensorTypeId=st.rowid JOIN platform p on p.rowid = s.platformId JOIN organization o on o.rowid=p.organizationId WHERE o.sname = 'TCOON' and SUBSTR(p.name, -2) = 'T2' ")



x=[]
q=0
ans = crsr.fetchall()
rowId_missing = []
q=0
for k in ans:
    rowId_missing.insert(q,[k[0],k[1]])
    q=q+1

for i in rowId_missing:
    crsr.execute("UPDATE sensor SET localId = '"+i[1]+"' WHERE rowId ="+str(i[0]))


# for i in rowId_missing:
#     print("UPDATE sensor SET localId = '"+i[1]+"' WHERE rowId ="+str(i[0]))

connection.commit()
connection.close()