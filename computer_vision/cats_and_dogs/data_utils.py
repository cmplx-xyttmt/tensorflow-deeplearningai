import zipfile
import os
from definitions import ROOT_DIR

BASE_DIR = os.path.join(ROOT_DIR, 'data/cats_and_dogs_filtered')
print(ROOT_DIR)


def extract_data():
    if not os.path.exists(BASE_DIR):
        # Unzip the archive
        local_zip = os.path.join(ROOT_DIR, 'data/cats_and_dogs_filtered.zip')
        zip_ref = zipfile.ZipFile(local_zip, 'r')
        zip_ref.extractall(os.path.join(ROOT_DIR, 'data'))


def print_directories():
    print("Contents of base directory:")
    print(os.listdir(BASE_DIR))

    print("Contents of train directory:")
    print(os.listdir(os.path.join(BASE_DIR, 'train')))

    print("Contents of validation directory:")
    print(os.listdir(os.path.join(BASE_DIR, 'validation')))


def get_train_and_validation_directories():
    train_dir = os.path.join(BASE_DIR, 'train')
    validation_dir = os.path.join(BASE_DIR, 'validation')
    return train_dir, validation_dir


if __name__ == '__main__':
    extract_data()
    print_directories()
