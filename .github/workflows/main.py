
# Import test_directory package
import test_directory

# Import modules
import test_directory.module1
import test_directory.module2
import test_directory.ingest_data.py

# Invoke functions
test_directory.module1.func1()
test_directory.module2.func2()
df_2 = test_directory.module2.ingest_data()
df_2.info()
