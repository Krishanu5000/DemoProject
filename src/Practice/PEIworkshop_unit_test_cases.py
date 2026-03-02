from src.Practice.PEIworkshop_raw_data_load import RawExtractAndLoad  # Replace with actual module name


def test_customer_file_read_schema(spark):
    # Arrange
    extractor = RawExtractAndLoad()

    # Act
    df = extractor.customer_file_read()

    # Assert: check that the DataFrame has expected columns
    expected_columns = [
        "Customer_ID", "Customer_Name", "email", "phone", "address",
        "Segment", "Country", "City", "State", "Postal_Code", "Region"
    ]
    assert df.columns == expected_columns
