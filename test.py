try:
    with open('utils/data/logs/counting_data.csv', 'w', newline='') as f:
        f.write("Test write\n")
    print("Write test passed!")
except PermissionError:
    print("Permission denied! Cannot write to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
