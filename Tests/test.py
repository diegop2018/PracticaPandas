from establish_connection import establish_connection

def test_establish_connection():
    conn = establish_connection()
    assert conn is not None, "Connection should not be None"
    assert conn.is_connected(), "Connection should be established"
    conn.close()
    print("test_establish_connection passed.")