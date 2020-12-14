
import os, time, datetime
from preprocess import PreprocessingPipeline
from random import shuffle


sampling_rate = 125
n_velocity_bins = 32
seq_length = 1024
n_tokens = 256 + sampling_rate + n_velocity_bins

def main():
    pipeline = PreprocessingPipeline(input_dir="data", stretch_factors=[0.975, 1, 1.025],
            split_size=30, sampling_rate=sampling_rate, n_velocity_bins=n_velocity_bins,
            transpositions=range(-2,3), training_val_split=0.9, max_encoded_length=seq_length+1,
                                    min_encoded_length=257)
    pipeline_start = time.time()
    pipeline.run()
    runtime = time.time() - pipeline_start
    print(f"MIDI pipeline runtime: {runtime / 60 : .1f}m")

    print(pipeline.encoded_sequences)

    exit()





if __name__=="__main__":
    main()
