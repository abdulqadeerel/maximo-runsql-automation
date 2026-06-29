from psdi.server.MXServer import getMXServer as MXS


def getHeader(rs):
    headerStr = ""    
    for i in range(rs.getMetaData().getColumnCount()):
        headerStr = headerStr + rs.getMetaData().getColumnName(i+1) + ","
    headerStr = headerStr[:-1] + "\r\n"                     # Remove the last "," and add a line break
    
    return headerStr

def getData(rs):
    dataStr = ""
    while (rs.next()):                                      #Loop through rows
        for i in range(rs.getMetaData().getColumnCount()):  #Loop through columns
            dataStr = dataStr + (rs.getString(i+1) or 'null') + ","
        dataStr = dataStr[:-1] + "\r\n"                     # Remove the last "," and add a line break
    
    return dataStr

### MAIN ###
connKey = MXS().getSystemUserInfo().getConnectionKey()
conn = MXS().getDBManager().getConnection(connKey)

method = request.getQueryParam("method").upper()            # SELECT or UPDATE,DELETE,INSERT
sql = request.getQueryParam("sql").upper()
stmt = conn.createStatement()

try:
    if method != 'SELECT':
        stmt.execute(sql)
        responseBody = "Done"
    else:
        rs = stmt.executeQuery(sql)
        headerStr = getHeader(rs)
        dataStr = getData(rs)
        responseBody = headerStr + dataStr
        rs.close()

finally:
    stmt.close()
    conn.commit()
    MXS().getDBManager().freeConnection(connKey)
