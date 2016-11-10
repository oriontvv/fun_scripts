from scripts.csv_utils import read_rows

def test_csv_reader(tmpdir):
	p = tmpdir.mkdir('temp').join('file.csv')
	content = """id,name,price
1,xiaomi redmi note3pro,159.99
2,iphone 7,-100.500
3,"samsung galaxy s3",99.99"""
	p.write(content)

	rows = list(read_rows(str(p), types=(int, str, float)))

	assert rows[0].id == 1
	assert rows[1].price == -100.500
	assert rows[2].price == 99.99
	assert rows[2].name == "samsung galaxy s3"
