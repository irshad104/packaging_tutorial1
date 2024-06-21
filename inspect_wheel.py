import zipfile
import sys

def list_wheel_contents(wheel_path):
    with zipfile.ZipFile(wheel_path, 'r') as wheel:
        for info in wheel.infolist():
            print(info.filename)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inspect_wheel.py <path_to_wheel>")
        sys.exit(1)

    wheel_path = sys.argv[1]
    list_wheel_contents(wheel_path)
