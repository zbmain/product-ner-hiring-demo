from modelscope.msdatasets import MsDataset

dataset_id = "winwin_inc/product-ner-hiring-demo"


class ProductNERDataset:

    def __init__(self, split="train"):
        assert split or split in ["train", "test"]
        self.split = split
        self._dataset = None

    @property
    def dataset(self):
        if self._dataset is None:
            self._dataset = MsDataset.load(dataset_id, split=self.split)
        return self._dataset

    def __iter__(self):
        for sample in self.dataset:
            yield sample

    def dataframe(self):
        return self.dataset.to_pandas()

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        return self.dataset[idx]
