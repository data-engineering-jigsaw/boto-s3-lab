from src.s3_client import *
def test_read_and_upload():
    file_name = './test_data/sample.json'
    # fill in bucket name here
    # bucket_name = ''
    bucket_name = 'jigsawtxdrinks'
    read_and_upload(file_name, bucket_name)
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    text = obj['Body'].read()
    data = json.loads(text)
    assert data == [{'hello': 'world'}, {'hola': 'mundo'}]

def test_store_restaurant_data():
    restaurants = ['HONDURAS MAYA CAFE & BAR LLC', 'FENG KAI CORPORATION']
    bucket_name = 'jigsawtxdrinks'
    # bucket_name = '' # fill in bucket name here
    store_restaurant_data(restaurants, bucket_name)
    response_data = s3.list_objects(Bucket=bucket_name) 
    object_names = [response['Key'] for response in response_data['Contents']]
    
    assert 'honduras_maya_cafe_&_bar_llc.json' in object_names
    assert 'feng_kai_corporation.json' in object_names