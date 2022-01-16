#!/usr/bin/env python3

from pathlib import Path
import torch
from kanachan.iterator_adaptor_base import IteratorAdaptorBase


class IteratorAdaptor(IteratorAdaptorBase):
    def __init__(self, path: Path, num_dimensions: int) -> None:
        super(IteratorAdaptor, self).__init__(path, num_dimensions)

    def __next__(self):
        sparse, numeric, positional, candidates, index, results = super(IteratorAdaptor, self).__next__()
        round_delta_of_score = results[1]
        # From the game records of the 82215309 rounds crawled from July 2020
        # to June 2021, the mean of the score round deltas is calculated to be
        # -1.1618527 and the standard deviation \sigma = 4940.5010.  Since the
        # mean is much smaller than the standard deviation, the following code
        # approximate it to 0 and scale the score round deltas so that the
        # 3\sigma range corresponds to [-1, 1].
        #
        # Even after the scaling as described above, there are still many large
        # outliers due to Yiman (役満), etc.  Therefore, Huber loss is used as
        # the loss function instead of MSE.
        round_delta_of_score /= (3.0 * 4940.0)
        round_delta_of_score = torch.tensor(
            round_delta_of_score, device='cpu', dtype=torch.float32)
        return (sparse, numeric, positional, candidates, index, round_delta_of_score)
