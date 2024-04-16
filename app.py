AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
MAC="68:e4:3b:30:60:79"

import os
import sys
# Example 1: Command Injection
user_input = input("Enter a filename: ")
os.system("cat " + user_input)
