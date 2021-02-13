## ADD credentials to git ignore
import pymysql
import credential

def doc_signup(doc_id,doc_username,doc_password,doc_name,qualification,specialization,doc_email,doc_confirmation):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "insert into doctor (doc_id,doc_username,doc_password,doc_name,qualification,specialization,doc_email,doc_confirmation) value (%s,%s,%s,%s,%s,%s,%s,%s)"
            doc_id=int(doc_id)
            doc_confirmation=int(doc_confirmation)
            curr.execute(sql,(doc_id,doc_username,doc_password,doc_name,qualification,specialization,doc_email,doc_confirmation))
            conn.commit()
    except Exception as e:
        print(e)        



def doc_login(doc_email,doc_password):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "select doc_password from doctor where doc_email=(%s)"
            curr.execute(sql,doc_email)
            output = curr.fetchone()
            if (output):
                if doc_password==output[0]:
                    return "correct_password"
                else:
                    return "wrong_password"
            return 'username_dosenot_exist'    
    except Exception as e:
        print(e)               


def doc_update(doc_email):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql="update doctor set doc_confirmation=(%s) where doc_email=(%s)"
            temp=2
            curr.execute(sql,(temp,doc_email))
            conn.commit()
    except Exception as e:
        print(e)     
# def pat_signup():
#     conn=pymysql.connect(
#         host=credential.host,
#         port=credential.port,
#         user=credential.user,
#         password=credential.password,
#         db=credential.databasename
#     )
#     try:
#         with conn.cursor() as curr
    