from scripts.csv_reader import read_rows

def test_csv_reader(tmpdir):
	p = tmpdir.mkdir('temp').join('file.csv')
	content = """id,name,price
1,xiaomi redmi note3pro,150
2,iphone 7,100500
-1,"samsung galaxy s3", 100"""
	p.write(content)

	rows = list(read_rows(str(p)))

	assert rows[0].id == '1'
	assert rows[1].price == '100500'
	assert rows[2].id == '-1'
	assert rows[2].name == "samsung galaxy s3"
