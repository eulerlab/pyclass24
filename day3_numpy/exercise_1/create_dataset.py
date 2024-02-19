import numpy as np


def main():
    np.random.seed(42)

    arr = np.random.normal(np.array([3, 4, 5]), np.array([1, 2, 3]), size=(100, 3))
    arr[:, 0] = arr[:, 0] ** 1.1
    arr[:, 1] = np.clip(arr[:, 1], 2, 6) ** 0.9
    arr[90:, 2] = np.nan

    chars = 'abcdefghijklmnopqrstuvwxyz'

    names = np.apply_along_axis(lambda d: "".join(d), -1,
                                np.random.choice([c for c in chars], size=(100, 3, 10)))

    assert np.unique(names).size == names.size

    names[~np.isfinite(arr)] = ""

    np.save(file='data', arr=arr, allow_pickle=True)
    np.save(file='names', arr=names, allow_pickle=True)


if __name__ == '__main__':
    main()
