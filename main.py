import os

TEXT = (
    "Are you a software update? Because I keep postponing you, "
    "but deep down I know you'd make everything run better."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
