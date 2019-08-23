# import solution
from hashlib import sha256
import subprocess
import sys
from os import listdir
from os.path import join


def hash(data):
    data = str(data)
    m = sha256()
    m.update(str(data))
    return m.hexdigest()


def load(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return data


def check_one(f, input_file, output_file):

    input_data = load(input_file)
    input_data = input_data.encode("utf-8")
    expected_output = load(output_file)

    print(f"Running program with {input_file}")
    result = subprocess.run(
        ["python3", f], input=input_data, stdout=subprocess.PIPE)
    actual_output = result.stdout.decode("utf-8")

    correct = actual_output == expected_output
    if not correct:
        print(f"Expected:\n{expected_output}")
        print(f"Actual:\n{actual_output}")
    else:
        print("CORRECT")
    return correct


def check_all(f, input_files, output_files):
    all_good = True
    total = len(input_files)
    correct = 0
    for i in range(len(input_files)):
        result = check_one(f, input_files[i], output_files[i])
        if result:
            correct += 1
        else:
            all_good = False

    print(f"You passed {correct}/{total} tests")
    return all_good


filename = sys.argv[1]
DATA_DIR = "data"
input_files = sorted(
    [join(DATA_DIR, x) for x in listdir(DATA_DIR) if x.endswith(".in")])
output_files = sorted(
    [join(DATA_DIR, x) for x in listdir(DATA_DIR) if x.endswith(".out")])
check_all(filename, input_files, output_files)
