from src.dataset import ProductNERDataset
from tabulate import tabulate


class TestDataset:

    def test_dataset_train(self):
        train_dataset = ProductNERDataset(split="train")
        print(f"\nTrain Columns: {train_dataset.dataframe().columns}")
        print(f"Train Size: {len(train_dataset)}")
        print(tabulate(train_dataset.dataframe().head(), headers='keys', tablefmt='psql', showindex=False))
        assert len(train_dataset) > 0

    def test_dataset_test(self):
        test_dataset = ProductNERDataset(split="test")
        print(f"\nTest Columns: {test_dataset.dataframe().columns}")
        print(f"Test Size: {len(test_dataset)}")
        print(tabulate(test_dataset.dataframe().head(), headers='keys', tablefmt='psql', showindex=False))
        assert len(test_dataset) > 0
