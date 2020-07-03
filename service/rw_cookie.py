from get_root_path import root_dir
import os

token_file = os.path.join(root_dir, "nky_cookie")


def write_file(token):
    with open(token_file, "w", encoding="utf-8") as fp:
        fp.write(token)


def read_token():
    with open(token_file,encoding="utf-8") as fp:
        return eval((fp.readlines()[0]))


if __name__ == "__main__":
    # token = "12345"
    # write_file(token)
    print((read_token()))
