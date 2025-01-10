import pymysql

def get_db_connection():
    """
    데이터베이스 연결을 생성하여 반환하는 함수
    """
    return pymysql.connect(
        host='127.0.0.1',
        port=3306,  # 'port'로 수정
        user='root',
        password='do0614',
        database='my_db',
        charset='utf8mb4'  # 한글을 제대로 처리하기 위해 charset 추가
    )

def save_user_to_db(user_id, password, nickname, address, user_type):
    """
    사용자 정보를 데이터베이스에 저장하는 함수
    비밀번호는 해시화하여 저장

    :param user_id: 사용자 ID
    :param password: 사용자 비밀번호
    :param nickname: 사용자 닉네임
    :param address: 사용자 주소
    :param user_type: 사용자 유형
    """
    import bcrypt  # 비밀번호 해시화를 위한 라이브러리
    
    # 비밀번호 해시화
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            # 사용자 데이터를 DB에 삽입하는 쿼리
            query = '''
                INSERT INTO users (id, password, nickname, address, type)
                VALUES (%s, %s, %s, %s, %s)
            '''

            cursor.execute(query, (user_id, hashed_password, nickname, address, user_type))
            conn.commit()  # 변경사항을 커밋하여 저장

    except pymysql.MySQLError as e:
        conn.rollback()  # 오류 발생 시 롤백
        print(f"Database error: {e}")
    finally:
        conn.close()  # 연결 종료
