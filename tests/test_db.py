from hun_args_history.db.utils import read_data
import pandas as pd

def test_read_data():
    r = read_data()
    assert isinstance(r, pd.DataFrame) # db/utils파일에 read_data(r)이(가) 판다스의 데이터 프레임 인스턴스 인지 확인
