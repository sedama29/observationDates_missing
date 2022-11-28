db=".\gcoos_data_v3.sqlite"
sqlite3 ${db} <<EOF
UPDATE sensor SET localId = (SELECT 'ioos:sensor:'||o.sname||':'||SUBSTR(p.name,1,3)||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname<>'ADCP' AND o.sname <> 'TABS' AND o.sname<>'NDBC' AND o.sname <> 'COAPS' AND o.sname <> 'TCOON' AND o.sname<>'SCCF RECON' AND o.sname<>'NOS' AND o.sname<>'NERRS' AND SUBSTR(p.name, 1, 2) <> '42'  AND (SUBSTR(p.name, -2) == 'F1' OR SUBSTR(p.name, -2) == 'A1' OR SUBSTR(p.name, -2) == 'L1') AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname<>'ADCP' AND o.sname <> 'TABS' AND o.sname<>'NDBC' AND o.sname <> 'COAPS' AND o.sname <> 'TCOON' AND o.sname<>'SCCF RECON' AND o.sname<>'NOS' AND o.sname<>'NERRS' AND SUBSTR(p.name, 1, 2) <> '42'  AND (SUBSTR(p.name, -2) == 'F1' OR SUBSTR(p.name, -2) == 'A1' OR SUBSTR(p.name, -2) == 'L1'));
UPDATE sensor SET localId = (SELECT 'ioos:sensor:'||o.sname||':'||SUBSTR(p.name,7)||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname = 'COAPS' AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname = 'COAPS');
UPDATE sensor SET localId = (SELECT 'ioos:sensor:'||o.sname||':'||SUBSTR(p.name,1,4)||'_'||SUBSTR(p.name,6)||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname = 'TABS' AND SUBSTR(p.name, 1, 2) <> '42' AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname = 'TABS' AND SUBSTR(p.name, 1, 2) <> '42');
UPDATE sensor SET localId = (SELECT 'ioos:sensor:TCOON:DNR_TAMUCC'||SUBSTR(SUBSTR(localId,INSTR(localId, '.')),1, INSTR(SUBSTR(localId,INSTR(localId, '.')+1), '.')+1)||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'TCOON' AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'TCOON');
UPDATE sensor SET localId = (SELECT 'ioos:sensor:NOAA.'||o.sname||'.CO-OPS'||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'NOS' AND SUBSTR(p.name, 1, 2) <> '87' AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'NOS' AND SUBSTR(p.name, 1, 2) <> '87');
UPDATE sensor SET localId = (SELECT 'ioos:sensor:NOAA.'||o.sname||'.CO-OPS'||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'NOS' AND SUBSTR(p.name, 1, 2) == '87' AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'NOS' AND SUBSTR(p.name, 1, 2) == '87');
UPDATE sensor SET localId = (SELECT 'ioos:sensor:NOAA.'||o.sname||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'NDBC' AND SUBSTR(p.name, 1, 2) <> '42' AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'NDBC' AND SUBSTR(p.name, 1, 2) <> '42');
UPDATE sensor SET localId = (SELECT 'ioos:sensor:'||'wmo:'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'NDBC' AND SUBSTR(p.name, 1, 2) == '42' AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'NDBC' AND SUBSTR(p.name, 1, 2) == '42');
UPDATE sensor SET localId = (SELECT 'ioos:sensor:NOAA.NDBC'||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'ADCP' AND SUBSTR(p.name, 1, 2) <> '42' AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'ADCP' AND SUBSTR(p.name, 1, 2) <> '42');
UPDATE sensor SET localId = (SELECT 'ioos:sensor:'||'wmo:'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'ADCP' AND SUBSTR(p.name, 1, 2) ==  '42' AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'ADCP' AND SUBSTR(p.name, 1, 2) ==  '42');
UPDATE sensor SET localId = (SELECT 'ioos:sensor:'||SUBSTR(o.sname,1,4)||'_'||SUBSTR(o.sname,6)||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname = 'SCCF RECON' AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname = 'SCCF RECON');
UPDATE sensor SET localId = (SELECT 'ioos:sensor:NOAA.'||o.sname||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'NERRS' AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname == 'NERRS');
UPDATE sensor SET localId = (SELECT 'ioos:sensor:'||'wmo:'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname<>'ADCP' AND o.sname<>'SCCF RECON' AND o.sname<>'NDBC' AND o.sname<>'NOS' AND o.sname<>'NERRS' AND SUBSTR(p.name, 1, 2) == '42' AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname<>'ADCP' AND o.sname<>'SCCF RECON' AND o.sname<>'NDBC' AND o.sname<>'NOS' AND o.sname<>'NERRS' AND SUBSTR(p.name, 1, 2) == '42');
UPDATE sensor SET localId = (SELECT 'ioos:sensor:'||o.sname||':'||p.name||':'||UPPER(SUBSTR(st.dataType, 1, 1)) || SUBSTR(st.dataType, 2)||'.'||s.sensorNumber
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname<>'ADCP' AND o.sname <> 'TABS' AND o.sname<>'NDBC' AND o.sname <> 'COAPS' AND o.sname <> 'TCOON' AND o.sname<>'SCCF RECON' AND o.sname<>'NOS' AND o.sname<>'NERRS' AND SUBSTR(p.name, 1, 2) <> '42'  AND SUBSTR(p.name, -2) <> 'F1' AND SUBSTR(p.name, -2) <> 'A1' AND SUBSTR(p.name, -2) <> 'L1' AND s.rowid=sensor.rowid)
WHERE rowid IN
(
SELECT s.rowid
FROM sensor s
JOIN sensorType st ON s.sensorTypeId=st.rowid
JOIN platform p ON p.rowid = s.platformId
JOIN organization o ON o.rowid = p.organizationId
WHERE o.sname<>'ADCP' AND o.sname <> 'TABS' AND o.sname<>'NDBC' AND o.sname <> 'COAPS' AND o.sname <> 'TCOON' AND o.sname<>'SCCF RECON' AND o.sname<>'NOS' AND o.sname<>'NERRS' AND SUBSTR(p.name, 1, 2) <> '42'  AND SUBSTR(p.name, -2) <> 'F1' AND SUBSTR(p.name, -2) <> 'A1' AND SUBSTR(p.name, -2) <> 'L1');
.exit
EOF
